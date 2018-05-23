# 23 05 work

import socket
import sys
from _thread import start_new_thread

HOST = '' # all availabe interfaces
PORT = 9999 # arbitrary non privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print("[-] Socket Created")

# bind socket
s.bind((HOST, PORT))
print("[-] Socket Bound to port " + str(PORT))

s.listen(10)
print("Listening...")

# The code below is what you're looking for ############

def client_thread(conn):
    conn.send(b"Welcome to the Server. Type messages and press enter to send.\n")

    while True:
        try:
            data = conn.recv(1024)
            print(data)
            conn.sendall(b"recieved")
        except socket.error as e:
            print(e)
            print("close socket")
            break

    conn.close()

while True:
    # blocking call, waits to accept a connection
    conn, addr = s.accept()
    print("[-] Connected to " + addr[0] + ":" + str(addr[1]))

    start_new_thread(client_thread, (conn,))

s.close()