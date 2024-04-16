import socket

# Function to receive file from client


def receive_file(client_socket, file_name):
    with open(file_name, 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)


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

        # Receive the file name
        file_name = connection.recv(1024).decode()
        print("Receiving file:", file_name)

        # Receive file from client
        receive_file(connection, file_name)

        print("File", file_name, "received successfully!")

    finally:
        # Clean up the connection
        connection.close()
