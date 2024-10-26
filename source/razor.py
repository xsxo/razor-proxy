from time import sleep
from urllib.parse import urlparse
from base64 import b64encode
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from sys import argv
from platform import platform
from os import system

class InvalidProxy(Exception):
    def __str__(self):
        return "The proxy url is Invalid"

class ArgvException(Exception):
    def __str__(self):
        return "Must include proxy url in argv\nexample: 'razor http://host:port'\nexample with authorization: 'razor http://username:password@host:port'\nfor more examples visit https://github.com/xsxo/razor-proxy"

class ConnectionException(Exception):
    def __str__(self):
        return "field create connection with ip:port"

class CounterClass:
    def __init__(self) -> None:
        self.OpnedConnections = 0
        self.TotalConnections = 0
        self.TrafficBytes = 0

class RazorProxy:
    def __init__(self) -> None:
        ar = argv
        if len(ar) != 2:
            raise ArgvException()

        self.ProxyURL = urlparse(ar[1])
        self.counter = CounterClass()

        if not self.ProxyURL.port or not self.ProxyURL.hostname:
            raise InvalidProxy()

        if self.ProxyURL.username and self.ProxyURL.password:
            self.authorization = b64encode(f"{self.ProxyURL.username}:{self.ProxyURL.password}".encode('utf-8'))

        try:
            self.server = socket(AF_INET, SOCK_STREAM)
            self.server.bind((self.ProxyURL.hostname, self.ProxyURL.port))
            self.server.listen(10000000)
        except:
            ConnectionException()

        print(f'PROXY URL: {ar[1]}')
        Thread(target=self.CounterFunction).start()
        self.accecpted()


    def send_request(self, client_socket:socket):
        to_connect : bytes = client_socket.recv(4096)
        
        if self.ProxyURL.username and not to_connect.__contains__(self.authorization):
            self.counter.OpnedConnections -= 1
            client_socket.close()
            return None

        for splited in to_connect.splitlines():
            splited = splited.lower()
            if b'host: ' in splited:
                host = splited.split(b'host: ')[1].split(b':')
                if len(host) == 1:
                    host = host[0]
                    port = 80
                else:
                    host, port = host
                break
        else:
            self.counter.OpnedConnections -= 1
            client_socket.close()
            return None

        try:
            server_socket = socket(AF_INET, SOCK_STREAM)
            server_socket.connect((str(host, 'utf-8'), int(port)))

            if b'CONNECT' in to_connect:
                client_socket.send(b"HTTP/1.1 200 Connection Established\r\n\r\n")
            else:
                server_socket.send(to_connect)
        except:
            self.counter.OpnedConnections -= 1
            client_socket.close()
            return None

        Thread(target=self.forward, args=(client_socket, server_socket)).start()
        Thread(target=self.forward, args=(server_socket, client_socket, True)).start()

    def forward(self, source, destination, HAND:bool=False):
        while True:
            try:
                data = source.recv(4096)
                if len(data) == 0:
                    break

                destination.send(data)
                self.counter.TrafficBytes += len(data)
            except:
                break

        try:
            source.close()
            destination.close()
        except:
            pass

        if HAND:
            self.counter.OpnedConnections -= 1
    
    def accecpted(self):
        while 1:
            client_socket, addr = self.server.accept()
            self.counter.OpnedConnections += 1
            self.counter.TotalConnections += 1
            Thread(target=self.send_request, args=(client_socket,)).start()

    def CounterFunction(self):
        if platform().__contains__('Windows'):
            system('cls')
        else:
            system('clear')

        while 1000000:
            print(f'\rAlive Connections: {self.counter.OpnedConnections} | Total Connections: {self.counter.TotalConnections} | Total Data Used: {self.counter.TrafficBytes / 1000000} MB', end=' ')
            sleep(1)