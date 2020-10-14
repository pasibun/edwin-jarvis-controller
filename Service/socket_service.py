import socket


class Socket(object):
    HOST = '10.0.0.30'
    PORT = 1337

    def send_socket(self, input):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.sendall(input.encode())
