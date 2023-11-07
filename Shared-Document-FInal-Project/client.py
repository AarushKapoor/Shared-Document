# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:28:01 2023

@author: aarus
"""
import tkinter as tk
import socket

#while True:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Port = 1234
Host = socket.gethostname()
    
s.connect((Host, Port))

while True:
    
    # Sending message to server
    message = input('message: ')
    s.sendall(message.encode())
    if message == 'end':
        break
        s.close()
    
    # Recieving message from server
    recievedMessage = s.recv(2048).decode()
    print('server:', recievedMessage)
    if recievedMessage == 'end':
        break
        s.close()