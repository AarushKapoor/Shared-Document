# Shared Document

A real-time collaborative text editor built with Python. Multiple clients can connect to a central server to share, edit, and download a common document.

**Authors:** Aarush Kapoor, Jenny Li Wang, Ayman Ali

---

## How It Works

The project follows a client-server architecture:

- The **server** hosts the shared document and manages connections from multiple clients simultaneously using threads.
- Each **client** connects to the server and can push or pull the latest version of the document through a simple GUI.

---

## Features

- Pull the latest document from the server
- Save/push local edits back to the server
- Download the document as a `.txt` file
- Text formatting: **Bold**, *Italic*, Underline
- Highlight selected text in yellow
- Add bullet points
- Change text color from a dropdown menu

---

## Requirements

- Python 3.x
- `tkinter` (included with most Python installations)
- `socket` and `threading` (standard library, no install needed)

---

## Setup & Usage

### 1. Start the Server

Run `server.py` on the machine that will host the document:

```bash
python server.py
```

The server will begin listening for connections on port **1234**.

### 2. Connect a Client

On each client machine, open `client.py` and update the `Host` variable to match the server's IP address:

```python
Host = "YOUR_SERVER_IP_HERE"
```

Then run:

```bash
python client.py
```

A GUI window will open. Multiple clients can connect at the same time.

---

## File Overview

| File | Description |
|---|---|
| `server.py` | Hosts the shared document, handles client connections via threads |
| `client.py` | GUI application for viewing and editing the shared document |

---

## Notes

- The server must be running before any clients attempt to connect.
- All clients share the same single document on the server. Saving overwrites the current version for everyone.
- The server listens on port `1234` by default. Make sure this port is open/accessible on the host machine.
