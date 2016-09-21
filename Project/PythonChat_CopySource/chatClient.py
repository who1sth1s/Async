import asyncio
import sys
import socket
import select

class ChatClient():
    def __init__(self):
        pass

    @asyncio.coroutine
    def chatClient(self, inputHost, inputPort):
        createSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        createSocket.settimeout(2)
        try:
            createSocket.connect((inputHost, int(inputPort)))
        except:
            print('Unable to connect')
            sys.exit()

        print('Connected to remote host. You can start sending messages')
        sys.stdout.write('[Me] '); sys.stdout.flush()

        while 1:
            # stdin: Input stream
            SOCKET_LIST = [sys.stdin, createSocket]
            ready_to_read, ready_to_write, in_error = select.select(SOCKET_LIST, [], [])
            for sock in ready_to_read:
                if sock == createSocket:
                    data = sock.recv(4096)
                    if not data:
                        print('\nDisconnected from chat server')
                        sys.exit()
                    else:
                        sys.stdout.write(data)
                        sys.stdout.write('[Me] '); sys.stdout.flush()

                else:
                    msg = sys.stdin.readline().encode()
                    createSocket.send(msg)
                    sys.stdout.write('[Me] '); sys.stdout.flush()