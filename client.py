class Client:

    recived_data = bytes

    def __init__(self):
        print("created")

    def show_data(self):
        print(self.recived_data)

    def recieving_data(self, bytes):
        print(bytes)
