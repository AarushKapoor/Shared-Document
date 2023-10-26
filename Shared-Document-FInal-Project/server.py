# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:45:50 2023

@author: Aarush Kapoor, Jenny Li Wang, Ayman Ali
"""

import tkinter as tk
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Port = 1234

s.bind(('',Port))
s.listen(20)

cs, addr = s.accept()
print(addr)
while True:
    
    # Recieving message from client
    recievedMessage = cs.recv(2048).decode()
    print('message:', recievedMessage)
    if recievedMessage == 'end':
        break
        cs.close()
    
    # Sending message to client
    reply = input('reply: ')
    cs.send(bytes(reply, 'utf-8'))
    if reply == 'end':
        break
        cs.close()