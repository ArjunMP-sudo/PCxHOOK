# PCxHOOK

**PCxHOOK** is a Python-based remote command execution tool that lets you control a server PC from anywhere. Whether you're across the room or across the country, you can send commands from a client device and have them executed silently on the server's command line.

## 🚀 Features

- 🔧 Remote command execution via TCP
- 🔄 Server auto-starts on system boot
- 🌐 Works over LAN or WAN with port forwarding
- 🧠 Lightweight and easy to configure
- 🖥️ Executes any command (e.g., `start notepad`, `ipconfig`, `dir`, `start https://www.google.com`)

## 🛠️ Setup Instructions

### Server (server.py)

1. Place `server.py` on the target PC.
2. Ensure Python is installed.
3. Create a `.bat` file to auto-run on boot:
   ```bat
   @echo off
   pythonw "C:\path\to\server.py"
