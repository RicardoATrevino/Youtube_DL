import tkinter as tk
import customtkinter 
from pytube import YouTube as yt

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
link = customtkinter.CTkEntry(app, width=350, height=40)
link.pack()

#run app

app.mainloop()

