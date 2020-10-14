import socket


class Socket(object):
    HOST = '10.0.0.30'
    PORT = 1337

    def send_socket(self, input):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.HOST, self.PORT))
        client.send(b'right')
        from_server = client.recv(1024)
        client.close()
        print(from_server)
