import asyncio
import traceback
import sys
from Project.PythonChat import chatServer

class ChattingStart():
    @asyncio.coroutine
    def chattingStart(self):
        self.chatServer = yield from chatServer.ChatServer()
        self.HOST = yield from self.chatServer.chatServer()
        print(self.HOST)
        return self.HOST

print("afsadfsd")
print(ChattingStart.chattingStart())