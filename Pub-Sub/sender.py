# sender.py
import socket


def send_message(message: str, host: str = '127.0.0.1', port: int = 12345) -> None:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
        client.sendall(message.encode())
        print(f"Sent: {message}")
    except ConnectionRefusedError:
        print("Could not connect to listener (connection refused)")
    except Exception as exc:
        print(f"Error sending message: {exc}")
    finally:
        try:
            client.close()
        except Exception:
            pass


def main() -> None:
    print("Type messages to send. Type '/quit' to exit.")
    try:
        while True:
            message = input("Enter message: ").strip()
            if not message:
                continue
            if message.lower() in {"/q", "/quit", "exit"}:
                print("Exiting sender...")
                break
            send_message(message)
    except KeyboardInterrupt:
        print("\nExiting sender...")


if __name__ == "__main__":
    main()