import tkinter 
import customtkinter 
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution
        video.download()  
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(text="Download Error")
    

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

#download button

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx = 10, pady=10)


#run app

app.mainloop()

