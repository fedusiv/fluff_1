import sqlite3

class Db_Handler(object):
    __instance = None

    conn = sqlite3.connect("fluffdb.db", check_same_thread = False)
    cursor = conn.cursor()


    @staticmethod
    def inst():
        if Db_Handler.__instance == None:
            Db_Handler.__instance = Db_Handler()
        return Db_Handler.__instance

    #single call
    def __init__(self):
        print("Data Base opened")

    def say_hello(self):
        print("hello")

    def check_login_pass(self,login,password):
        request = "SELECT password FROM users WHERE login=?"
        self.cursor.execute(request, [login])
        pass_string = self.cursor.fetchall()
        if len(pass_string) != 1:
            return 2
        for string in pass_string:
            print(string)
            if string == password:
                return 0
            else:
                return 1