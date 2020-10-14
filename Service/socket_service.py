import socket


class Socket(object):
    HOST = '10.0.0.109'
    PORT = 1337

    def send_socket(self, input):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.sendall(input)
            data = s.recv(1024)
        print('Received', repr(data))
