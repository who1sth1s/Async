import asyncio
import sys
import socket
import select
import traceback

class ChatClient():
    def __init__(self):
        pass

    @asyncio.coroutine
    def chatClient(self, inputHost, inputPort):
        createSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        createSocket.settimeout(2)
        print(createSocket)
        try:
            createSocket.connect((inputHost, int(inputPort)))
        except:
            print(traceback.format_exc())
            sys.exit()

        print('Connected to remote host. You can start sending messages')
        sys.stdout.write('[Me] '); sys.stdout.flush()

        while 1:
            # stdin: Input stream
            SOCKET_LIST = [sys.stdin, createSocket]
            ready_to_read, ready_to_write, in_error = select.select(SOCKET_LIST, [], [])
            for sock in ready_to_read:
                print(sock)
                print(createSocket)
                if sock == createSocket:
                    data = sock.recv(4096).decode()
                    if not data:
                        print('\nDisconnected from chat server')
                        createSocket.close()
                        sys.exit()
                    else:
                        sys.stdout.write(data)
                        sys.stdout.write('[Me] '); sys.stdout.flush()

                else:
                    msg = sys.stdin.readline().encode()
                    createSocket.send(msg)
                    sys.stdout.write('[Me] '); sys.stdout.flush()