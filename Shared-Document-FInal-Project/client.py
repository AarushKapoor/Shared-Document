# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:28:01 2023

@authors: Aarush Kapoor, Jenny Li Wang, Ayman Ali
Client
"""
import tkinter as tk
import socket

def send_message():
    message = message_entry.get()
    s.sendall(message.encode())
    message_listbox.insert("end", f"Client: {message}")
    if message == 'end':
        s.close()
        message_listbox.insert("end", "Connection closed")
    message_entry.delete(0, "end")  # Clear the input field

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Port = 1234
Host = socket.gethostname()

s.connect((Host, Port))

root = tk.Tk()
root.title("Client")

message_listbox = tk.Listbox(root, bg="white")
message_listbox.pack()

message_entry = tk.Entry(root)
message_entry.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()