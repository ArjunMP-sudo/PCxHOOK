import socket

SERVER_IP = 'your.public.ip.or.ddns.net'  # Replace with public IP or DDNS domain
COMMAND_PORT = 9999

def send_command(command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, COMMAND_PORT))
            s.sendall(command.encode())
            print("[WAN] Command sent successfully.")
    except Exception as e:
        print(f"[WAN] Connection failed: {e}")

if __name__ == "__main__":
    user_input = input("Enter command to run on WAN server: ")
    send_command(user_input)
