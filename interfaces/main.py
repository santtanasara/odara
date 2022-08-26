from tkinter import *
from tkinter import ttk

def run():
    root = Tk()
    root.title("Odara Nature")
    root.geometry("1000x600")

    Label(root, text="Odara Nature", bg="#D3D3D3", pady=30, font=("Arial", 25)).grid(column=0, row=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    run()