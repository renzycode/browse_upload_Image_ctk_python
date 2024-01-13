import customtkinter
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import ImageTk, Image
import os
import shutil
import random  
import string
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.title("Python Custom Tkinter Upload Image")
app.geometry("480x380")

frame=customtkinter.CTkLabel(app,text="")
frame.grid(row=0,column=0,sticky="w",padx=50,pady=20)

def setPreviewPic(filepath):
    global img
    img = Image.open(filepath)
    img = img.resize((250,250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    lbl_show_pic = tk.Label(frame, bg='#1F6AA5',image=img)
    lbl_show_pic.grid(row=1, column=0, columnspan=3,pady=5,ipady=0,sticky="nswe")
    pathEntry.insert(0, filepath)

def selectPic():
    global filename
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(), 
        title="Select Image",
        filetypes=[("images files","*.png *.jpg *.jpeg"),]
    )
    setPreviewPic(filename)

def savePic():
    filenameSplitted = filename.split('.')
    randomText = ''.join((random.choice(string.ascii_lowercase) for x in range(12)))
    shutil.copy(filename, f"./images/{randomText}.{filenameSplitted[1]}")
    setPreviewPic("./images/default.png")
    messagebox.showinfo("Success", "Uploaded Successfully")

selectBtn=customtkinter.CTkButton(frame,text="Browse Image",width=50,command=selectPic)
pathEntry=customtkinter.CTkEntry(frame,width=200)
saveBtn=customtkinter.CTkButton(frame,text="Upload",width=50,command=savePic)
lbl_show_pic = tk.Label(frame, bg='#1F6AA5')

setPreviewPic("./images/default.png")

selectBtn.grid(row=0,column=0,padx=1,pady=5,ipady=0,sticky="e")
pathEntry.grid(row=0,column=1,padx=1,pady=5,ipady=0,sticky="e")
saveBtn.grid(row=0,column=2,padx=1,pady=5,ipady=0,sticky="e")
lbl_show_pic.grid(row=1, column=0, columnspan=3,pady=5,ipady=0,sticky="nswe")

app.resizable(False, False) 
app.mainloop()