import asyncio
import socket
import sys

HOST = ''
SOCKET_LIST = []
RECV_BUFFER = 4096
PORT = 33137

async def chatServer():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(10)
    SOCKET_LIST.append(serverSocket)
    print('[Chat server]')
    print('[Port]{PORT}').format(PORT=PORT)




if __name__ == '__main__':
    await chatServer()
    sys.exit(chatServer())