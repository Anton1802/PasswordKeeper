import socket
import json


class Server:

    def __init__(self):
        self.host = ""
        self.port = 0
        self.s = None
        self.conn = None
        self.addr = None
        self.data = None
        self.client_dict = None
        self.db_path = "data/db.json"
        self.server_dict = {}

    def start_server(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))
        print("Server started")
        while True:
            self.s.listen(1)
            self.conn, self.addr = self.s.accept()
            print(f"Connect: {self.addr[0]}:{self.addr[1]}")
            if self.addr:
                if self.request_handler():
                    self.response_handler()

    def request_handler(self) -> bool:
        try:
            self.server_dict = self.read_db()
        except json.decoder.JSONDecodeError:
            pass

        while True:
            self.data = self.conn.recv(1024)

            if not self.data:
                break

            try:
                self.client_dict = json.loads(self.data.decode('utf-8'))
            except json.decoder.JSONDecodeError:
                self.conn.close()
                print("Connect close")
                break

            try:
                if (self.server_dict[self.client_dict['username']] and
                        self.client_dict['data_user']):
                    self.server_dict[self.client_dict['username']] = self.client_dict
                    self.save_db(json.dumps(self.server_dict))
                    print("User data update")
                    return True
                else:
                    return True
            except KeyError:
                self.server_dict[self.client_dict['username']] = self.client_dict
                self.save_db(json.dumps(self.server_dict))
                print("User add to base")
                return True

    def response_handler(self) -> None:
        try:
            self.conn.sendall(json.dumps(self.server_dict[self.client_dict['username']]).encode('utf-8'))
            print("Data sent to client")
        except BrokenPipeError:
            print("Client disconnect")

        self.client_dict.clear()
        self.conn.close()
        print("Connect close")

    def read_db(self) -> dict:
        with open(self.db_path, 'r') as file:
            data = file.read()
            json_data = json.loads(data)
        return json_data

    def save_db(self, data: str) -> None:
        json_obj = json.loads(data)
        with open(self.db_path, 'w') as file:
            json.dump(json_obj, file, indent=4)


if __name__ == "__main__":
    server = Server()
    server.start_server("localhost", 3035)
