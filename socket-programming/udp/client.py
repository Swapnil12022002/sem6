import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
# Change localhost to your server IP if needed
server_address = ('localhost', 12345)

try:
    # Send message
    message = "Welcome"
    print("Sending:", message)
    client_socket.sendto(message.encode(), server_address)

    # Receive response
    response, _ = client_socket.recvfrom(1024)
    print("Received:", response.decode())

finally:
    # Clean up the socket
    client_socket.close()
