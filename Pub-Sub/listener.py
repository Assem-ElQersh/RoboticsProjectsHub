# listener.py
import socket


def start_server(host: str = '127.0.0.1', port: int = 12345) -> None:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)
    print(f"Listening for messages on {host}:{port} ...")

    try:
        while True:
            try:
                client, addr = server.accept()
                try:
                    data = client.recv(4096)
                    if not data:
                        continue
                    message = data.decode(errors='replace')
                    print(f"Received from {addr[0]}:{addr[1]}: {message}")
                finally:
                    client.close()
            except Exception as exc:
                print(f"Error handling connection: {exc}")
    except KeyboardInterrupt:
        print("Shutting down listener...")
    finally:
        server.close()


if __name__ == "__main__":
    start_server()