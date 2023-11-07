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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Port = 1234
Host = socket.gethostname()
s.connect((Host, Port))

root = tk.Tk()
root.title("Shared Document Client")

text = tk.Text(root, wrap="word", width=40, height=15)
text.pack()

pull_button = tk.Button(root, text="Pull", command=pull_document)
pull_button.pack()

save_button = tk.Button(root, text="Save", command=save_document)
save_button.pack()

client_socket = s

root.mainloop()
