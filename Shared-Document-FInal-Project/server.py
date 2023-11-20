# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:45:50 2023

@authors: Aarush Kapoor, Jenny Li Wang, Ayman Ali
Server
"""

import socket
import threading

shared_document = ""  # Shared document content

# Function that handles communication with the client
def handle_client(client_socket):
    global shared_document
    while True:
        request = client_socket.recv(1024).decode()
        #If client request to pull the document
        if request == "pull":
            # Send the share document to the client
            client_socket.send(shared_document.encode())
        # If the client request to save the document
        elif request.startswith("save:"):
            data = request.split(":", 1)[1]
            shared_document = data
            # Message to the client that document has been saved
            client_socket.send(b"Saved")
        # If client request to exit the commention    
        elif request == "exit":
            # Close the client socket
            client_socket.close()
            break

# Set up a socket and begin listening to the client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Port = 1234
s.bind(('', Port))
s.listen(20)

print("Server is listening for clients...")

while True:
    # Accept client connection
    client_socket, addr = s.accept()
    print(f"Accepted connection from {addr}")
    # A thread is created that handles client's requests
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start() #Thread starts handling the client

