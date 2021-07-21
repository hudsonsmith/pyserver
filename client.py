import socket


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


PORT: int = 5050
HEADER: int = 64
FORMAT: str = "utf-8"
DISCONNECT_MESSAGE: str = "exit"

# Please add the appropriate IP address below.
SERVER: str = "127.0.0.1"

ADDR: tuple = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    if not msg:
        return

    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


while True:
    try:
        msg: str = input(f"{Colors.green}[YOU]:{Colors.reset} ")
        send(msg)
        if msg == "exit":
            exit()
    except KeyboardInterrupt:
        send("exit")
        exit()
