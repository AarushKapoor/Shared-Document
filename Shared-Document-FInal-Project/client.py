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
    
def change_font_size(slider_value):
    global text
    new_font_size = int(slider_value)
    text.config(font=("Arial", new_font_size))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Port = 1234
Host = "10.220.45.216"
s.connect((Host, Port))

root = tk.Tk()
root.title("Shared Document Client")

text = tk.Text(root, wrap="word", width=40, height=15)
text.pack()

pull_button = tk.Button(root, text="Pull", command=pull_document)
pull_button.pack()

save_button = tk.Button(root, text="Save", command=save_document)
save_button.pack()

download_button = tk.Button(root, text="Download", command=download_document)
download_button.pack()

font_size_scale = tk.Scale(root, from_=8, to=24, orient=tk.HORIZONTAL, label="Font Size", command=change_font_size)
font_size_scale.pack()

client_socket = s

root.mainloop()
