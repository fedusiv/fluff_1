import json
import sqlite3


class Client:
    # recieved data from tcp
    received_data = dict
    # list of json packets for sending
    sending_fifo = []



    def parse_command_login(self):
        if self.received_data["login"] == "ilya" and self.received_data["password"] == "555":
            msg = json.dumps(
                {"command": "login",
                 "result": "correct"}
            )
            self.sending_fifo.append(msg)
            print("correct client login")
        else:
            msg = json.dumps(
                {"command": "login",
                 "result": "incorrect"}
            )
            self.sending_fifo.append(msg)
            print("incorrect client login")

    def parse_command_password(self):
        print(self.received_data)


    commands_dict = {
        "login": parse_command_login,
        "register": parse_command_password
    }

    def __init__(self):
        print("created")

    def recieving_data(self, b_data):
        j_data = json.loads(b_data.decode("utf-8"))
        print(j_data)
        self.received_data = j_data
        command = j_data["command"]
        try:
            parse_res = self.commands_dict[command]
            parse_res(self)
        except KeyError as e:
            print("got wrong command")


    def sending_data(self):
        if len(self.sending_fifo) > 0:
            return self.sending_fifo.pop(0)
        else:
            return 0
