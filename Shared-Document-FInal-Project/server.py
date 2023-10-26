# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:45:50 2023

@author: Aarush Kapoor, Jenny Li Wang, Ayman Ali
"""

import tkinter as tk

root = tk.Tk()
root.title("Text Editor") 

text = tk.Text(root)
text.pack()

def save():
    with open("doc.txt", "w") as f:
        f.write(text.get("1.0", "end"))

button = tk.Button(root, text="Save", command=save)
button.pack()

root.mainloop()