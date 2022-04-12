import socket

# First message header length
HEADER = 64
PORT = 5050
# Get local server host IP address
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
# Message format
FORMAT = 'utf-8'
# Disconnect message to disconnect from the server
DISCONNECT_MSG = "!CLOSE"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("Hello World!")
send("Hello Everyone!")
send("This is Sagar")

send(DISCONNECT_MSG)