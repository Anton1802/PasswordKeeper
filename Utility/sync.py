import socket


class Sync:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.s.connect((self.host, self.port))

    def request_message(self, message):
        self.s.sendall(message.encode('utf-8'))

    def response_message(self) -> list:
        data_response = []

        while True:
            data = self.s.recv(3)
            data_response.append(data.decode("utf-8"))
            if not data:
                break

        return data_response




