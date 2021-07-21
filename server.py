import socket
import threading


class Colors:
    red = "\033[31m"
    blue = "\033[34m"
    green = "\033[32m"
    purple = "\033[35m"
    brown = "\033[33m"
    yellow = "\033[1;33m"
    cyan = "\033[36m"
    pink = "\033[35;1m"
    reset = "\033[0m"


# Open the settings.yaml file and define global vars.
PORT: int = 5050
SERVER: str = socket.gethostbyname(socket.gethostname())
HOSTNAME: str = socket.gethostname()
ADDR: tuple = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "exit"


# Create and bind the server to and adress and port.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# A function to handle client connections.
def handle_client(conn, addr):
    print(
        f"{Colors.green}[NEW CONNECTION]{Colors.reset} {Colors.cyan}{addr}{Colors.reset} connected."
    )

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"{Colors.green}[{addr}]:{Colors.reset} {msg}")

    conn.close()


def start():
    """A function to start the socket server."""

    # Listen for new connections.
    server.listen()

    print(
        f"{Colors.green}[RUNNING]{Colors.reset} Server is running on address: {Colors.cyan}{SERVER}{Colors.reset}, hostname: {Colors.cyan}{HOSTNAME}{Colors.reset}, port: {Colors.cyan}{PORT}{Colors.reset}"
    )

    # Server mainloop.
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(
            f"{Colors.green}[ACTIVE CONNECTIONS]:{Colors.reset} {threading.activeCount() - 1}"
        )


print(f"{Colors.green}[STARTING]{Colors.reset} Server is starting...")
start()
