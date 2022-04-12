from concurrent.futures import thread
import socket
import threading

# First message header length
HEADER = 64
PORT = 5000
# Get local server host IP address
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
# Message format
FORMAT = 'utf-8'
# Disconnect message to disconnect from the server
DISCONNECT_MSG = "!CLOSE"
# Initiate socket connection. AF_INET for IPv4 address.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# To handle individual client connection
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            # If disconnect message received
            if msg == DISCONNECT_MSG:
                connected = False

            print(f"[{addr}] {msg}")
    conn.close()

# Starting the server
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        # Thread for individual client connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

    
print("[STARTING] server is starting...")
start()