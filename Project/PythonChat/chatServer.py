import asyncio
import socket

HOST = ''
SOCKET_LIST = []
RECV_BUFFER = 4096
PORT = 33137

def chatServer():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)