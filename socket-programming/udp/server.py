import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
# Change localhost to your server IP if needed
server_address = ('localhost', 12345)
server_socket.bind(server_address)

print("Server is listening for messages...")

while True:
    # Receive message and client address
    message, client_address = server_socket.recvfrom(1024)
    print("Received:", message.decode(), "from", client_address)

    # Send response
    response = "Welcome from server"
    server_socket.sendto(response.encode(), client_address)
