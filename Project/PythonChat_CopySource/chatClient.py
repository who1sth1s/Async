import asyncio
import sys
import socket
import select

class ChatClient():
    @asyncio.coroutine
    def chatClient(self, inputHost, inputPort):
        createSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        createSocket.settimeout(2)

        try:
            createSocket.connect((inputHost, inputPort))
        except:
            print('Unable to connect')
            sys.exit()

        print('Connected to remote host. You can start sending messages')
        sys.stdout.write('[Me] '); sys.stdout.flush()

        while 1:
