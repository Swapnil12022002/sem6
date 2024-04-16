import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
# Change localhost to your server IP if needed
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

print("Server is listening for connections...")

while True:
    # Wait for a connection
    connection, client_address = server_socket.accept()

    try:
        print("Connection from:", client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            if data:
                print("Received:", data.decode())
                if data.decode() == "Hello":
                    connection.sendall("Hello from server".encode())
                else:
                    connection.sendall("Invalid message".encode())
            else:
                break

    finally:
        # Clean up the connection
        connection.close()
