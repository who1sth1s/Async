import asyncio
import traceback
from Project.PythonChat.chatServer import ChatServer

class ChattingStart():
    @asyncio.coroutine
    def chattingStart(self):
        yield from ChatServer.chatServer()