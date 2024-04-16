import socket


def main():
    target_host = "www.google.co.in"
    target_port = 80

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((target_host, target_port))
        print("Connected to %s on port %s" % (target_host, target_port))
    except Exception as e:
        print("Error: %s" % str(e))
    finally:
        client.close()


if __name__ == "__main__":
    main()
