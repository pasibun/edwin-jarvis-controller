import socket


class Socket(object):
    HOST = '10.0.0.30'
    PORT = 1337

    def send_socket(self, input):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.HOST, self.PORT))
        client.send(input.encode())
        from_server = client.recv(4096)
        client.close()
        print(from_server)
