# 23 05 home
import socket
import sys
from _thread import start_new_thread
from client import Client

HOST = '' # all availabe interfaces
PORT = 9999 # arbitrary non privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[-] Socket Created")
s.bind((HOST, PORT))
print("[-] Socket Bound to port " + str(PORT))
s.listen(10)
print("Listening...")

def client_thread(conn, addr):
        cl = Client()
        while True:
            try:
                data = conn.recv(1024)
                cl.recived_data = data
                cl.recieving_data(data)
                cl.show_data()
                conn.send(b"i'm server")
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