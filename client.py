import socket


class Colors:
    """A class to contain all the colors needed in order to style text output."""

    red: str = "\033[31m"
    blue: str = "\033[34m"
    green: str = "\033[32m"
    purple: str = "\033[35m"
    brown: str = "\033[33m"
    yellow: str = "\033[1;33m"
    cyan: str = "\033[36m"
    pink: str = "\033[35;1m"
    reset: str = "\033[0m"


# Port number for the server to run on.
PORT: int = 5050

# The header used to pad initial message that gets sent to the server.
HEADER: int = 64

# The format that the messages will be encoded in.
FORMAT: str = "utf-8"

# The disconnect message that will disconnect the client from the server.
DISCONNECT_MESSAGE: str = "exit"

# Please add the appropriate IP address below.
SERVER: str = "127.0.0.1"

# Create the Address using the server and the port.
ADDR: tuple = (SERVER, PORT)

# Initialize the client and connect it to the address of the server.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    """A function to send the message to the server."""

    # If the message is an empty line, then return.
    if not msg:
        return

    # Encode the message.
    message = msg.encode(FORMAT)

    # Get the length of the message and send it to the server.
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)

    # Then send the real message to the server.
    client.send(message)


# The client mainloop.
while True:
    try:
        # Let the user type their messages and send it to the server.
        msg: str = input(f"{Colors.green}[YOU]:{Colors.reset} ")
        send(msg)

        # If the message is "exit", then exit the program.
        if msg == "exit":
            exit()
    except KeyboardInterrupt:
        # If a KeyboardInterrupt occurs then disconnect the client from the server.
        send("exit")
        exit()
