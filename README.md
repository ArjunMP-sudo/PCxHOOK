# PCxHOOK

![PCxHOOK Logo]([https://via.placeholder.com/600x150?text=PCxHOOK+Remote+Command+Tool](https://as1.ftcdn.net/v2/jpg/06/59/19/60/1000_F_659196081_1ruqvVm3L3i1l7sPbHS1GrwlOJX9Uqsl.jpg))

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

**PCxHOOK** is a Python-based remote command execution tool that lets you control a server PC from anywhere. Whether you're across the room or across the country, you can send commands from a client device and have them executed silently on the server's command line.

---

# 🚀 Features

- 🔧 Remote command execution via TCP
- 🔄 Server auto-starts on system boot
- 🌐 Works over LAN or WAN with port forwarding
- 🧠 Lightweight and easy to configure
- 🖥️ Executes any command (e.g., `start notepad`, `ipconfig`, `dir`, `start https://www.google.com`)

---

# 🛠️ Setup Instructions

# Server (server.py)

1. Place `server.py` on the target PC.
2. Ensure Python is installed.
3. Create a `.bat` file to auto-run on boot:
   ```bat
   @echo off
   pythonw "C:\path\to\server.py"

Press Win + R, type shell:startup, and hit Enter.

Place a shortcut to server.py or the .bat file in this folder to run it automatically on startup.

Set up port forwarding on your router:

Forward TCP port 9999 to your server PC’s local IP.

Allow port 9999 through Windows Firewall.

Client (client.py)

Place client.py on your control device.

Edit SERVER_IP in client.py to match the server’s public IP or DDNS domain.

Run the script and enter any command to execute on the server.

🌐 Remote Access

To access the server from anywhere:

Use your public IP or DDNS domain in client.py

Ensure port forwarding is active

Confirm connectivity with:

telnet your.public.ip 9999

⚠️ Security Warning

This tool allows remote command execution. To protect your system:

Use strong firewall rules

Restrict access to trusted IPs

Add authentication or command whitelisting if deploying publicly

📄 License

This project is open-source and free to use for educational and personal purposes.

🙋‍♂️ Author

Created by [Arjun MP]
