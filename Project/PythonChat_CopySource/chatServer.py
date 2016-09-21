import asyncio
import traceback
import socket
import select

class ChatServer():
    def __init__(self):
        self.HOST = ''
        self.SOCKET_LIST = []
        self.RECV_BUFFER = 4096
        self.PORT = 9009
        pass

    @asyncio.coroutine
    def chatServerMain(self):
        try:
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            serverSocket.bind((self.HOST, self.PORT))
            serverSocket.listen(10)
            self.SOCKET_LIST.append(serverSocket)
            print('Chat server started on port ' + str(self.PORT))
            while 1:
                ready_to_read,ready_to_write,in_error = select.select(self.SOCKET_LIST, [], [], 0)

                for sock in ready_to_read:
                    if sock == serverSocket:
                        sockfd, addr = serverSocket.accept()
                        self.SOCKET_LIST.append(sockfd)
                        loginInfo = 'Client ({host}, {port})'.format(host=addr[0], port=addr[1])
                        print(loginInfo)
                        yield from self.broadcast(serverSocket, sockfd,
                                                  '[{addr}:{addr}] entered our chatting room\n'.format(addr=addr))
                    else:
                        try:
                            data = sock.recv(self.RECV_BUFFER)
                            if data:
                                yield from self.broadcast(serverSocket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)
                            else:
                                if sock in self.SOCKET_LIST:
                                    self.SOCKET_LIST.remove(sock)
                                yield from self.broadcast(serverSocket, sock,
                                                          'Client ({addr}, {addr}) is offline\n'.format(addr=addr))
                        except:
                            yield from self.broadcast(serverSocket, sock,
                                                      'Client ({addr}, {addr}) is offline\n'.format(addr=addr))
                            continue
            serverSocket.close()

        except:
            print(traceback.format_exc().strip().split('\n'))

    @asyncio.coroutine
    def broadcast(self, serverSocket, sock, message):
        for socket in self.SOCKET_LIST:
            if socket != serverSocket and socket != sock:
                try:
                    socket.send(message)
                except:
                    socket.close()
                    if socket in self.SOCKET_LIST:
                        self.SOCKET_LIST.remove(socket)