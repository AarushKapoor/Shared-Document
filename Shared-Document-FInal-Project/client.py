# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:28:01 2023

@authors: Aarush Kapoor, Jenny Li Wang, Ayman Ali
Client
"""
import tkinter as tk
import socket

def pull_document():
    global shared_document
    client_socket.send(b"pull")
    shared_document = client_socket.recv(4096).decode()
    text.delete("1.0", "end")
    text.insert("1.0", shared_document)

def save_document():
    global shared_document
    shared_document = text.get("1.0", "end")
    client_socket.send(f"save:{shared_document}".encode())
    response = client_socket.recv(1024).decode()
    if response == "Saved":
        print("Document saved on the server")

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

def change_font_size(event=None):
    global font_size
    try:
        new_size = float(font_size_var.get())
        if new_size > 0:
            font_size = new_size
            text.configure(font=(font_family, font_size))
    except ValueError:
        pass  # Ignore if the user enters a non-numeric value

# Set default font family and font size
font_family = "Helvetica"
font_size = 10

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
pull_button = tk.Button(button_frame, text="Pull", command=pull_document)
pull_button.pack(side="left")

save_button = tk.Button(button_frame, text="Save", command=save_document)
save_button.pack(side="left")

download_button = tk.Button(button_frame, text="Download", command=download_document)
download_button.pack(side="left")

bold_button = tk.Button(button_frame, text="Bold", command=make_text_bold)
bold_button.pack(side="left")

italic_button = tk.Button(button_frame, text="Italic", command=make_text_italic)
italic_button.pack(side="left")

underline_button = tk.Button(button_frame, text="Underline", command=make_text_underlined)
underline_button.pack(side="left")

# Font size entry
font_size_label = tk.Label(button_frame, text="Font Size:")
font_size_label.pack(side="left")

font_size_var = tk.StringVar()
font_size_var.set(str(font_size))
font_size_entry = tk.Entry(button_frame, textvariable=font_size_var)
font_size_entry.pack(side="left")
font_size_entry.bind("<Return>", change_font_size)

# Text widget for document content
text = tk.Text(root, wrap="word", width=40, height=15, font=(font_family, font_size))
text.pack()

client_socket = s

root.mainloop()

