# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:28:01 2023

@authors: Aarush Kapoor, Jenny Li Wang, Ayman Ali
Client
"""

import tkinter as tk
import socket

# Function to save the documetn on the server
def save_document():
    # Access the global variable shared_document
    global shared_document
    shared_document = text.get("1.0", "end")
    # Send the document to the server and encode it
    client_socket.send(f"save:{shared_document}".encode())
    # Receive acknoledgement from the server and decode it
    response = client_socket.recv(1024).decode()
    # If server's respond is "Saved," print a message indicating that it was successfully saved
    if response == "Saved":
        print("Document saved on the server")

#Function to pull the document from the server
def pull_document():
    # Access the global variable shared_document
    global shared_document
    # Send to server a request to pull the document
    client_socket.send(b"pull")
    # Receive the updated document content from server and decode it
    shared_document = client_socket.recv(4096).decode()
    # Clear the cotent of the text widget
    text.delete("1.0", "end")
    # Inset/open the pulled document into the text widget
    text.insert("1.0", shared_document)

# Function to download the document as ".txt" file
def download_document():
    # Access the global variable shared_document
    global shared_document
    file_path = "downloaded_document.txt"
    with open(file_path, "w") as file:
        # Write the shared document content into the file
        file.write(shared_document)
    print(f"Document downloaded as {file_path}") # Successful download message

# Function to bold text or remove the bold
def make_text_bold():
    # Retrieve the existing text formatting for the selected text
    current_tags = text.tag_names("sel.first")
    # If text is already in bold
    if "bold" in current_tags:
        # Remove the bold formatting
        text.tag_remove("bold", "sel.first", "sel.last")
    # If not applied
    else:
        # Apply bold formatting
        text.tag_add("bold", "sel.first", "sel.last")
        text.tag_configure("bold", font=(font_name, font_size, "bold"))

# Function to make text italic
def make_text_italic():
    # Retrieve the existing text formatting for the selected text
    current_tags = text.tag_names("sel.first")
    # If text is already in italic
    if "italic" in current_tags:
        # Remove the italic formatting
        text.tag_remove("italic", "sel.first", "sel.last")
    # If not applied
    else:
        # Apply italic formatting
        text.tag_add("italic", "sel.first", "sel.last")
        text.tag_configure("italic", font=(font_name, font_size, "italic"))

# Function to underline text or remove the underline
def make_text_underlined():
    # Retrieve the existing text formatting for the selected text
    current_tags = text.tag_names("sel.first")
    # If text is already underlined
    if "underline" in current_tags:
        # Remove underline formatting
        text.tag_remove("underline", "sel.first", "sel.last")
    # If not applied
    else:
        # Apply underline formatting
        text.tag_add("underline", "sel.first", "sel.last")
        text.tag_configure("underline", underline=True)

# Function to add bullet points
def add_bullet_point():
    # Insert bullet point at the current position of the cursor
    text.insert(tk.INSERT, "\u2022 ")

# Used chatGPT 3.5 for the highlight_text() function
# Function to highlight specific text or remove highlight    
def highlight_text():
    try:
        # Retrieves the beginning and ending position of the selected text to highlight
        start_pos = text.index("sel.first")
        end_pos = text.index("sel.last")
        # If text is already highlighted
        if "highlight" in text.tag_names(start_pos):
            # Remove the highlight 
            text.tag_remove("highlight", start_pos, end_pos)
        # If not applied
        else:
            # Add yellow highlight to the selected text
            text.tag_add("highlight", start_pos, end_pos)
            text.tag_configure("highlight", background="yellow")
    # If no text is selected, then ignore this error and continue running the program
    except tk.TclError:
        pass

# Function to change the text color
def change_text_color(color):
    # Change the text color to the color that the client chose
    text.config(foreground=color)
    # Update the displayed text on the  text color menu to the color that the client chose
    color_menu_button.config(text=color)
    
# Set default font and font size
font_name = "Times New Roman"
font_size = 12

# Connection setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Port = 1234
Host = "10.220.43.245"
s.connect((Host, Port))

root = tk.Tk()  # GUI window
root.title("Shared Document Client")    # Window title

# Frame to organize the buttons at the top
button_frame = tk.Frame(root)
button_frame.pack(side="top", fill="x")

# Buttons for actions
# Save button to save the document to the server
pull_button = tk.Button(button_frame, text="Save", command=save_document)
pull_button.pack(side="left")

# Button to look for the document from the server
save_button = tk.Button(button_frame, text="Pull", command=pull_document)
save_button.pack(side="left")

# Download button to download the document as ".txt" file
download_button = tk.Button(button_frame, text="Download", command=download_document)
download_button.pack(side="left")

# Button to make text bold
bold_button = tk.Button(button_frame, text="Bold", command=make_text_bold)
bold_button.pack(side="left")

# Button to make the text italic
italic_button = tk.Button(button_frame, text="Italic", command=make_text_italic)
italic_button.pack(side="left")

# Button to underline text
underline_button = tk.Button(button_frame, text="Underline", command=make_text_underlined)
underline_button.pack(side="left")

# Button to create a bullet point in the document at the current position of the cursor
bullet_button = tk.Button(button_frame, text="Bullet Point", command=add_bullet_point)
bullet_button.pack(side="left")

# Highlighter button to higlight the selected text
highlight_button = tk.Button(button_frame, text="Highlight", command=highlight_text)
highlight_button.pack(side="left")

#Used chatGPT 3.5 to create the dropdown menu for the text color change option
# Dropdown menu for text color selection

# Name label of each color option to change text color
color_label = tk.Label(button_frame, text="Text Color:")
color_label.pack(side="left")

# Default color
selected_color = tk.StringVar(root)
selected_color.set("Black")

# Color options to change text color
color_options = ["Black", "Red", "Green", "Blue", "Cyan", 
                 "Yellow", "Orange", "Pink", "Gray"]

# Button for text color otpions
color_menu_button = tk.Menubutton(button_frame, text="Black", relief="raised", direction="below")
color_menu_button.pack(side="left")

# Menu for the color options (dropdown menu)
color_menu = tk.Menu(color_menu_button, tearoff=False)
color_menu_button.config(menu=color_menu)

# Color options in the dropdown menu
for color in color_options:
    color_menu.add_command(label=color, command=lambda c=color: change_text_color(c))
    

# Text widget for document content
text = tk.Text(root, wrap="word", width=80, height=40, font=(font_name, font_size))
text.pack() # Pack the text widget into the root window

client_socket = s   # Client socket

root.mainloop() # Start the main loop for the GUI, and handles user interactions