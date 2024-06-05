import sys
#v=sys.python_version
import tkinter as tk
from tkinter import filedialog, Menu, Menubutton, IntVar

root = tk.Tk()
root.title("Text Editor")

text = tk.Text(root)
text.grid(row=0, column=0, columnspan=2)

def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if savelocation:
        with open(savelocation, "w") as file1:
            file1.write(t)

button = tk.Button(root, text="Save", command=saveas)
button.grid(row=1, column=0)

def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

def FontTimesNewRoman():
    global text
    text.config(font="Times New Roman")

font = Menubutton(root, text="Font")
font.grid(row=1, column=1)
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu
helvetica = IntVar()
courier = IntVar()
times_new_roman = IntVar()
font.menu.add_checkbutton(label="Courier", variable=courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command=FontHelvetica)
font.menu.add_checkbutton(label="Times New Roman", variable=times_new_roman, command=FontTimesNewRoman)

root.mainloop()