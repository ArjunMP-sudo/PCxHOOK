import socket

SERVER_IP = '192.168.1.100'  # Replace with your server's LAN IP
COMMAND_PORT = 9999

def send_command(command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, COMMAND_PORT))
            s.sendall(command.encode())
            print("[LAN] Command sent successfully.")
    except Exception as e:
        print(f"[LAN] Connection failed: {e}")

if __name__ == "__main__":
    user_input = input("Enter command to run on LAN server: ")
    send_command(user_input)
