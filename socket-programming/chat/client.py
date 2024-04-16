import socket
import threading

# Function to receive messages from server


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except Exception as e:
            print("Error receiving message:", e)
            break


# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server address and port
# Change localhost to your server IP if needed
server_address = ('localhost', 12345)

# Connect the socket to the server's address and port
client_socket.connect(server_address)

# Start a thread to receive messages from server
receive_thread = threading.Thread(
    target=receive_messages, args=(client_socket,))
receive_thread.start()

# Send messages to server
while True:
    message = input()
    client_socket.sendall(message.encode())
