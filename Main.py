import subprocess
import tkinter 
from tkinter import filedialog
import customtkinter 
import os
import json
import time

#path to settings json file
settings_file = os.path.expanduser("~/Documents/Youtube_Downloader_Settings.json")

#default settings dictionary
default_settings = {
    "path": os.path.expanduser("~/Documents/Youtube_Downloader_Settings.json")
}


#Load settings from the JSON file. or create if non existant
if os.path.exists(settings_file):
    print(f"Settings file found: {settings_file}")
    with open(settings_file, 'r') as file:
        settings = json.load(file)
        print("Settings file loaded successfully.")
else:
    print(f"Settings file not found. Creating new settings file at: {settings_file}")
    settings = default_settings
    with open(settings_file, 'w') as file:
        json.dump(default_settings, file)
    
def save_settings(settings):
    """Save settings to the JSON file."""
    with open(settings_file, 'w') as file:
        json.dump(settings, file, indent=4)


def file_select():
    folder_selected = filedialog.askdirectory()
    
    if folder_selected:
        folder_label.configure(text=f"Download folder: {folder_selected}")
        settings['download_folder'] = folder_selected
        save_settings(settings)
        return folder_selected
    else:
        folder_label.configure(text="No folder selected.")
        return None
    

def startDownload(download_type):
    folder = settings.get('download_folder', None)
    
    if not folder:
        folder = file_select()
    if folder:
            ytlink = link.get()
            output_path = f"{folder}/%(title)s.%(ext)s"
            if download_type == 'mp3':
                command = ['./yt-dlp.exe', ytlink,"-f", "bestaudio", "-o", output_path,  "--extract-audio", "--audio-format", "mp3", "--yes-playlist"]

            elif download_type == 'webm':
                command = ['./yt-dlp.exe', ytlink, "-f", "bestvideo+bestaudio", "-o", output_path,  "--yes-playlist"]

            #legacy code when yt-dlp is in PATH
            # process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
            process = subprocess.run(command, stdout=subprocess.PIPE)
            
            if process.returncode == 0:
                fade_text.configure(text="Downloaded!!!!!")
                
            else:
                print("ur not gettign process return code 0")

def fade_label(label, current_alpha=1.0, step=0.05,delay=100):
    if current_alpha <= 0:
        label.configure(text="")
        return

# Calculate new color by reducing opacity (fade effect)
    current_alpha = max(0, current_alpha - step)
    color_value = int(255 * current_alpha)  # Convert alpha to 0-255 range
    
    # Set label text color
    label.configure(text_color=f"#{color_value:02x}{color_value:02x}{color_value:02x}")
    # Call fade_label again after a delay
    label.after(delay, fade_label, label, current_alpha)



#sys settings 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


#app frame

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")


# Create a label
fade_text = customtkinter.CTkLabel(app, text="")
fade_text.pack()

# Start fading after 2 seconds
app.after(3000, fade_label, fade_text)  # Delay of 2000ms before starting the fade


#adding ui elements

title = customtkinter.CTkLabel(app, text="Insert link")
title.pack(padx=10, pady=5)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()



# Create a frame to hold the buttons side by side
button_frame = customtkinter.CTkFrame(app)
button_frame.pack(pady=20)
#download options

videoOption = customtkinter.CTkButton(button_frame, text="Download as WEBM Video", command=lambda: startDownload("webm"))
videoOption.pack(padx=5, pady=5, side="left")

audioOption = customtkinter.CTkButton(button_frame, text="Download as MP3 Audio", command=lambda: startDownload("mp3") )
audioOption.pack(padx=5, pady=5,side="right")




# Folder Selection Button and Label
folder_button = customtkinter.CTkButton(app, text="Select Download Folder", command=file_select)
folder_button.pack(pady=10)

loaded_folder = settings.get('download_folder', "No folder selected.")  # Load saved folder or default
folder_label = customtkinter.CTkLabel(app, text=f"Download folder: {loaded_folder}")
folder_label.pack(pady=10)


# Status Label
status_label = customtkinter.CTkLabel(app, text="")
status_label.pack()


#run app

app.mainloop()

