import socket
import threading


class Colors:
    red: str = "\033[31m"
    blue: str = "\033[34m"
    green: str = "\033[32m"
    purple: str = "\033[35m"
    brown: str = "\033[33m"
    yellow: str = "\033[1;33m"
    cyan: str = "\033[36m"
    pink: str = "\033[35;1m"
    reset: str = "\033[0m"


# The port that the server will run on.
PORT: int = 5050

# Get the current machine's IP address and then use that for the server.
SERVER: str = socket.gethostbyname(socket.gethostname())

# Get the machine hostname.
HOSTNAME: str = socket.gethostname()

# Create the address using the server and the port.
ADDR: tuple = (SERVER, PORT)

# The header used to recieve the first message sent by the client.
HEADER = 64

# The format that all the messages will be encoded with.
FORMAT = "utf-8"

# The message the client will send to the server to signify their disconnection.
DISCONNECT_MESSAGE = "exit"


# Create and bind the server to and adress and port.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


# A function to handle client connections.
def handle_client(conn, addr):
    """A function to recieve messages from the client and print them to the screen."""

    # Print who connected.
    print(
        f"{Colors.green}[NEW CONNECTION]{Colors.reset} {Colors.cyan}{addr}{Colors.reset} connected."
    )

    # Set the state of the client to connected.
    connected = True

    while connected:
        # Recieve the size of the message.
        msg_length = conn.recv(HEADER).decode(FORMAT)

        # If the message is not a blank connect message then recieve the message.
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            # If the message is disconnect message, then set the client state to disconnected.
            if msg == DISCONNECT_MESSAGE:
                connected = False

            # Print the client message.
            print(f"{Colors.green}[{addr}]:{Colors.reset} {msg}")

    # If the client is no longer connected, close the connection.
    conn.close()


def start():
    """A function to start the socket server."""

    # Listen for new connections.
    server.listen()

    # Notify the user that the server is running.
    print(
        f"{Colors.green}[RUNNING]{Colors.reset} Server is running on address: {Colors.cyan}{SERVER}{Colors.reset}, hostname: {Colors.cyan}{HOSTNAME}{Colors.reset}, port: {Colors.cyan}{PORT}{Colors.reset}"
    )

    # Server mainloop.
    while True:
        # Accept a connection, and address.
        conn, addr = server.accept()

        # Start a new thread to handle the client.
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        # Print how many active connections there are.
        print(
            f"{Colors.green}[ACTIVE CONNECTIONS]:{Colors.reset} {threading.activeCount() - 1}"
        )


# Notify the user that the server is starting.
print(f"{Colors.green}[STARTING]{Colors.reset} Server is starting...")
start()
