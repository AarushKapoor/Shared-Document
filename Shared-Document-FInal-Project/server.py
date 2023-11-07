# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:45:50 2023

@authors: Aarush Kapoor, Jenny Li Wang, Ayman Ali
Server
"""

import tkinter as tk
import socket
import threading

received_messages = []

def accept_connections():
    while True:
        cs, addr = s.accept()
        message_listbox.insert("end", f"Connected to {addr}")
        threading.Thread(target=handle_client, args=(cs, addr)).start()

def handle_client(client_socket, client_address):
    while True:
        received_message = client_socket.recv(2048).decode()
        if received_message == 'end':
            client_socket.close()
            message_listbox.insert("end", f"Connection with {client_address} closed")
            break
        received_messages.append(f"Client {client_address}: {received_message}")
        message_listbox.insert("end", f"Client {client_address}: {received_message}")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Port = 1234
s.bind(('', Port))
s.listen(20)

root = tk.Tk()
root.title("Server")

root.geometry("500x200")

message_listbox = tk.Listbox(root, bg="white")
message_listbox.pack()

accept_thread = threading.Thread(target=accept_connections)
accept_thread.daemon = True
accept_thread.start()

root.mainloop()
