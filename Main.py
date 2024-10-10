import subprocess
import tkinter 
import customtkinter 

import yt_dlp

def startDownload():
    try:
        ytlink = link.get()
        output_path = "C:/Users/Yt_MP3/%(title)s.%(ext)s"
        command = ["yt-dlp", ytlink, "-o", output_path ]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            print("Download complete.")
        else:
            print(f"Error: {stderr.decode()}")
    except Exception as e: print(e)
        

        #finishLabel.configure(text="Download Error", text_color="red")
""" 
        ytObject = yt(ytLink, on_progress_callback=on_progress)       
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per+'%')
    pPercentage.update
    
    #update progress bar
    progressBar.set(float(percentage_of_completion) / 100)
    """

#sys settings 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# our app frame

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube DL -> mp3")

#adding ui elements

title = customtkinter.CTkLabel(app, text="insert yt link")
title.pack(padx=10, pady=10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#finished downloading

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

"""#progress percentage

pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10,pady=10)
"""
#download button

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx = 10, pady=10)


#run app

app.mainloop()

