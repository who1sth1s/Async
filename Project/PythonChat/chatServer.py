import asyncio
import traceback
import socket
import select

class ChatServer():
    def __init__(self):
        self.HOST = ''
        self.SOCKET_LIST = []
        self.RECV_BUFFER = 4096
        self.PORT = 33137
        pass

    @asyncio.coroutine
    def chatServerMain(self):
        try:
            serverSocket = yield from self.chatServerSetting()
            self.SOCKET_LIST.append(serverSocket)
            print('Chat server started on port ' + str(self.PORT))
            while 1:
                ready_to_ready, \
                ready_to_write, \
                in_error = select.select(self.SOCKET_LIST, [], [], 0)
        except:
            print(traceback.format_exc().strip().split('\n'))

    @asyncio.coroutine
    def chatServerSetting(self):
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serverSocket.bind((self.HOST, self.PORT))
        serverSocket.listen(10)
        return serverSocket