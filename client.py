import json

class Client:

    received_data = dict

    def parse_command_login(self):
        if self.received_data["login"] == "ilya" and self.received_data["password"] == "555" :
            print("correct")

        else:
            print("incorrect")

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

