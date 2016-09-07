import asyncio
import socket

HOST = ''
SOCKET_LIST = []
RECV_BUFFER = 4096
PORT = 33137

def chatServer():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)