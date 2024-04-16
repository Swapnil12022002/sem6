import socket

# Function to send file to server


def send_file(server_socket, file_name):
    with open(file_name, 'rb') as file:
        for data in file:
            server_socket.sendall(data)


# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server address and port
# Change localhost to your server IP if needed
server_address = ('localhost', 12345)

# Connect the socket to the server's address and port
client_socket.connect(server_address)

try:
    # Send file name
    file_name = "example.txt"  # Change to the file you want to transfer
    client_socket.sendall(file_name.encode())
    print("Sending file:", file_name)

    # Send file to server
    send_file(client_socket, file_name)

    print("File", file_name, "sent successfully!")

finally:
    # Clean up the socket
    client_socket.close()
