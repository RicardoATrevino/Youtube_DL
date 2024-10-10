import subprocess
import tkinter 
from tkinter import filedialog
import customtkinter 
import yt_dlp
import os
import json

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
    

def startDownload():
    folder = settings.get('download_folder', None)
    
    if not folder:
        folder = file_select()
    if folder:
        try:
            ytlink = link.get()
            output_path = f"{folder}/%(title)s.%(ext)s"
            command = ["yt-dlp", ytlink,"-f", "bestaudio", "-o", output_path,  "--extract-audio", "--audio-format", "mp3"]
            process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                status_label.config(text="Download")
            else:
                print(f"Error: {stderr.decode()}")
        except Exception as e: print(e)

        #finishLabel.configure(text="Download Error", text_color="red")


#sys settings 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


#app frame

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#adding ui elements

title = customtkinter.CTkLabel(app, text="Insert link")
title.pack(padx=10, pady=5)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()


#download options

videoOption = customtkinter.CTkButton(app, text="Click here for Video")
videoOption.pack(padx=20, pady=10)

audioOption = customtkinter.CTkButton(app, text="Click here for just audio" )
audioOption.pack(padx=15, pady=10)




# Folder Selection Button and Label
folder_button = customtkinter.CTkButton(app, text="Select Download Folder", command=file_select)
folder_button.pack(pady=10)

loaded_folder = settings.get('download_folder', "No folder selected.")  # Load saved folder or default
folder_label = customtkinter.CTkLabel(app, text=f"Download folder: {loaded_folder}")
folder_label.pack(pady=10)

# Status Label
status_label = customtkinter.CTkLabel(app, text="")
status_label.pack()

#download button

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx = 10, pady=5)

#finished downloading

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#run app

app.mainloop()

