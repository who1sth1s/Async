import asyncio
import traceback
import socket

class ChatServer():
    def __init__(self):
        self.HOST = ''
        self.SOCKET_LIST = []
        self.RECV_BUFFER = 4096
        self.PORT = 33137
        pass

    @asyncio.coroutine
    def chatServer(self):
        try:
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            serverSocket.bind((self.HOST, self.PORT))
            serverSocket.listen(10)
            self.SOCKET_LIST.append(serverSocket)
            print('Chat server started on port ' + str(self.PORT))
        except:
            print(traceback.format_exc().strip().split('\n'))