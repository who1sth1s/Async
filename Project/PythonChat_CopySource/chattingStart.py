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
        selectType = input('(--- Input your type ---)\n1. Create Server\n2. Join Server\n:')
        if selectType == 'Create':
            self.HOST = yield from chatServer.ChatServer().chatServerMain()
        elif selectType == 'Join':
            print('Hello world!!')
        else:
            print('''\nIf you want to create server, input "Create"\nIf you want to join server, input "Join"''')

chattingClass = ChattingStart()
asyncio.get_event_loop().run_until_complete(chattingClass.chattingStart())
