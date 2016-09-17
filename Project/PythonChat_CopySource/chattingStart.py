import asyncio
import traceback
import sys
import chatServer

class ChattingStart():
    def __init__(self):
        self.HOST = ''
        self.SOCKET_LIST = []
        self.RECV_BUFFER = 4096
        self.PORT = 33137
        pass

    @asyncio.coroutine
    def chattingStart(self):
        #self.chatServer = yield from chatServer.ChatServer()
        self.HOST = yield from chatServer.ChatServer().chatServerMain()

chattingClass = ChattingStart()
asyncio.get_event_loop().run_until_complete(chattingClass.chattingStart())
