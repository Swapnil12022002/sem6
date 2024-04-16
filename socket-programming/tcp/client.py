import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
# Change localhost to your server IP if needed
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Send data
    message = "Hello"
    print("Sending:", message)
    client_socket.sendall(message.encode())

    # Receive data
    data = client_socket.recv(1024)
    print("Received:", data.decode())

finally:
    # Clean up the connection
    client_socket.close()
