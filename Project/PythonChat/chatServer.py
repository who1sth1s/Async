import asyncio
import traceback
import socket
import sys

HOST = ''
SOCKET_LIST = []
RECV_BUFFER = 4096
PORT = 33137

@asyncio.coroutine
def chatServer():
    try:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serverSocket.bind((HOST, PORT))
        serverSocket.listen(10)
        SOCKET_LIST.append(serverSocket)
        return HOST
    except:
        print(traceback._format_final_exc_line())

@asyncio.coroutine
def main(argv):
    try:
        HOST = yield from chatServer()
        print(HOST)
    except:
        print(traceback._format_final_exc_line())

if __name__ == '__main__':
    sys.exit(main(sys.argv))