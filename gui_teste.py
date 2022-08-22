import tkinter as tk
from tkinter import filedialog
from tkinter import *
#from PIL import Image,ImageTk


root = Tk()
root.title("Odara")
root.geometry("500x300+400+200")

LeftMenu = Frame(root, bd=2, relief=RIDGE, bg="blue")
LeftMenu.place(x=0, y=102, width=200, height=550)

btn_feedstock = Button(LeftMenu, compound=LEFT, text="Estoque",
                      font=("times new roman", 18, "bold"), bg="white", cursor="hand2", bd=2, padx=5, anchor="w",
                      height=40).pack(side=TOP, fill=X)


root.resizable(False, False)

root.mainloop()