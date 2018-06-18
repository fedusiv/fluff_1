# 23 05 home
import socket
import sys
from _thread import start_new_thread
from client import Client
import sqlite3

HOST = '' # all availabe interfaces
PORT = 9999 # arbitrary non privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[-] Socket Created")
s.bind((HOST, PORT))
print("[-] Socket Bound to port " + str(PORT))
s.listen(10)
print("Listening...")

# connection with db
sql_conn = sqlite3.connect("fluffdb.db")
# cursor on db
sql_cursor = sql_conn.cursor()

sql_cursor.execute("""CREATE TABLE users
                  (email text, login text, password text,
                   money text)""")
sql_cursor.execute("""INSERT INTO users
    VALUES ('sentipon.n@gmail.com','ilya','555', '10')""")

sql_conn.commit()


def client_thread(conn, addr):
        cl = Client()
        while True:
            # check are client got message for send
            send_message = cl.sending_data()
            if send_message != 0:
                conn.send(send_message.encode("utf-8"))
                print("send: "+send_message)
            try:
                data = conn.recv(1024)
                cl.recieving_data(data)
            except socket.error as e:
                print(e)
                print("close socket")
                break



while True:
    # blocking call, waits to accept a connection
    conn, addr = s.accept()
    print("[-] Connected to " + addr[0] + ":" + str(addr[1]))
    start_new_thread(client_thread, (conn, addr))

s.close()