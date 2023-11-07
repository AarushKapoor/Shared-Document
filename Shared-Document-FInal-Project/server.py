# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:45:50 2023

@authors: Aarush Kapoor, Jenny Li Wang, Ayman Ali
Server
"""

import socket
import threading

shared_document = ""  # Shared document content

def handle_client(client_socket):
    global shared_document
    while True:
        request = client_socket.recv(1024).decode()
        if request == "pull":
            client_socket.send(shared_document.encode())
        elif request.startswith("save:"):
            data = request.split(":", 1)[1]
            shared_document = data
            client_socket.send(b"Saved")
        elif request == "exit":
            client_socket.close()
            break

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Port = 1234
s.bind(('', Port))
s.listen(20)

print("Server is listening for clients...")

while True:
    client_socket, addr = s.accept()
    print(f"Accepted connection from {addr}")
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()

