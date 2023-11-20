# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:28:01 2023

@authors: Aarush Kapoor, Jenny Li Wang, Ayman Ali
Client
"""

import tkinter as tk
import socket

def save_document():
    global shared_document
    shared_document = text.get("1.0", "end")
    client_socket.send(f"save:{shared_document}".encode())
    response = client_socket.recv(1024).decode()
    if response == "Saved":
        print("Document saved on the server")

def pull_document():
    global shared_document
    client_socket.send(b"pull")
    shared_document = client_socket.recv(4096).decode()
    text.delete("1.0", "end")
    text.insert("1.0", shared_document)

def download_document():
    global shared_document
    file_path = "downloaded_document.txt"
    with open(file_path, "w") as file:
        file.write(shared_document)
    print(f"Document downloaded as {file_path}")

def make_text_bold():
    current_tags = text.tag_names("sel.first")
    if "bold" in current_tags:
        text.tag_remove("bold", "sel.first", "sel.last")
    else:
        text.tag_add("bold", "sel.first", "sel.last")
        text.tag_configure("bold", font=(font_family, font_size, "bold"))

def make_text_italic():
    current_tags = text.tag_names("sel.first")
    if "italic" in current_tags:
        text.tag_remove("italic", "sel.first", "sel.last")
    else:
        text.tag_add("italic", "sel.first", "sel.last")
        text.tag_configure("italic", font=(font_family, font_size, "italic"))

def make_text_underlined():
    current_tags = text.tag_names("sel.first")
    if "underline" in current_tags:
        text.tag_remove("underline", "sel.first", "sel.last")
    else:
        text.tag_add("underline", "sel.first", "sel.last")
        text.tag_configure("underline", underline=True)

def add_bullet_point():
    text.insert(tk.INSERT, "\u2022 ")  # Unicode character for bullet point
    
def highlight_text():
    try:
        start_pos = text.index("sel.first")
        end_pos = text.index("sel.last")
        if "highlight" in text.tag_names(start_pos):
            text.tag_remove("highlight", start_pos, end_pos)
        else:
            text.tag_add("highlight", start_pos, end_pos)
            text.tag_configure("highlight", background="yellow")
    except tk.TclError:
        pass
    
def change_text_color(color):
    text.config(foreground=color)
    color_menu_button.config(text=color)
    
# Set default font family and font size
font_family = "Times New Roman"
font_size = 12

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Port = 1234
Host = "10.220.45.216"
s.connect((Host, Port))

root = tk.Tk()
root.title("Shared Document Client")

# Frame to organize the buttons at the top
button_frame = tk.Frame(root)
button_frame.pack(side="top", fill="x")

# Buttons for actions
pull_button = tk.Button(button_frame, text="Save", command=save_document)
pull_button.pack(side="left")

save_button = tk.Button(button_frame, text="Pull", command=pull_document)
save_button.pack(side="left")

download_button = tk.Button(button_frame, text="Download", command=download_document)
download_button.pack(side="left")

bold_button = tk.Button(button_frame, text="Bold", command=make_text_bold)
bold_button.pack(side="left")

italic_button = tk.Button(button_frame, text="Italic", command=make_text_italic)
italic_button.pack(side="left")

underline_button = tk.Button(button_frame, text="Underline", command=make_text_underlined)
underline_button.pack(side="left")

bullet_button = tk.Button(button_frame, text="Bullet Point", command=add_bullet_point)
bullet_button.pack(side="left")

# Highlighter button
highlight_button = tk.Button(button_frame, text="Highlight", command=highlight_text)
highlight_button.pack(side="left")

# Dropdown menu for text color selection (Custom dropdown)
color_label = tk.Label(button_frame, text="Text Color:")
color_label.pack(side="left")

selected_color = tk.StringVar(root)
selected_color.set("Black")  # Default color

color_options = ["Black", "Red", "Green", "Blue", "Cyan", 
                 "Yellow", "Orange", "Pink", "Gray"]  # Additional basic color options

color_menu_button = tk.Menubutton(button_frame, text="Black", relief="raised", direction="below")
color_menu_button.pack(side="left")

color_menu = tk.Menu(color_menu_button, tearoff=False)
color_menu_button.config(menu=color_menu)

for color in color_options:
    color_menu.add_command(label=color, command=lambda c=color: change_text_color(c))
    

# Text widget for document content
text = tk.Text(root, wrap="word", width=80, height=40, font=(font_family, font_size))
text.pack()

client_socket = s

root.mainloop()