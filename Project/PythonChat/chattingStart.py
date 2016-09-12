import asyncio
import traceback
import sys
import chatServer

class ChattingStart():
    def __init__(self):
        pass

    @asyncio.coroutine
    def chattingStart(self):
        self.chatServer = yield from chatServer.ChatServer()
        self.HOST = yield from self.chatServer.chatServer()
        print(self.HOST)
        return self.HOST

print("afsadfsd")
tmp_obj = ChattingStart()
print(tmp_obj.chattingStart())