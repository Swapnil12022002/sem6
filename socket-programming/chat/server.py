import socket
import threading

# Function to handle client connections


def handle_client(client_socket, client_address):
    print("Connection from:", client_address)

    # Receive and broadcast messages from the client
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print("Received from", client_address, ":", message)
        broadcast(message, client_socket)

    # Close the client connection
    print("Client", client_address, "disconnected.")
    client_sockets.remove(client_socket)
    client_socket.close()

# Function to broadcast message to all clients


def broadcast(message, sender_socket):
    for client in client_sockets:
        if client != sender_socket:
            try:
                client.sendall(message.encode())
            except Exception as e:
                print("Error broadcasting message:", e)


# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
# Change localhost to your server IP if needed
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

print("Server is listening for connections...")

client_sockets = []

# Accept and handle client connections
while True:
    client_socket, client_address = server_socket.accept()
    client_sockets.append(client_socket)
    client_thread = threading.Thread(
        target=handle_client, args=(client_socket, client_address))
    client_thread.start()
