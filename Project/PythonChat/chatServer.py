import asyncio
import traceback
import socket

HOST = ''
SOCKET_LIST = []
RECV_BUFFER = 4096
PORT = 33137

class ChatServer:
    @asyncio.coroutine
    def chatServer(self):
        try:
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            serverSocket.bind((HOST, PORT))
            serverSocket.listen(10)
            SOCKET_LIST.append(serverSocket)
            return HOST
        except:
            print(traceback.format_exc().strip().split('\n'))