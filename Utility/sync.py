import socket


class Sync:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.s.connect((self.host, self.port))
        except ConnectionRefusedError:
            return False
        else:
            return True

    def request_message(self, message):
        try:
            self.s.sendall(message.encode('utf-8'))
        except BrokenPipeError:
            return False
        else:
            return True

    def response_message(self) -> list:
        data_response = []
        try:
            while True:
                data = self.s.recv(1024)
                data_response.append(data.decode("utf-8"))
                if not data:
                    break
        except OSError:
            return list()
        else:
            return data_response

