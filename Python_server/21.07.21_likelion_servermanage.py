import socket 
from _thread import *
from pynput import keyboard
import time
import threading
import sys
bServerLoopEnd = False
bClienrWaitEnd = False

def MainLoop():
    if (bServerLoopEnd == False):
        threading.Timer(0.1 , MainLoop).start()
    else:
        print("Server close")
        server_socket.close()
        sys.exit()
# def on_press(key):
    
def on_release(key):
    global bClienrWaitEnd

    if key == keyboard.Key.esc:
        print("==================esc===============")
        bClienrWaitEnd = True;
        return False

def ClientChkThreaded(i):
    global bClienrWaitEnd
    global bServerLoopEnd
    while True:
        print("clientCheckThreaded wait!!!!")

        server_socket.settimeout(1)
        if(bClienrWaitEnd == False):
            try:
                client_socket , addr = server_socket.accept()
            except socket.timeout:
                continue
            server_socket.settimeout(None)
            print("client_socket connected" , addr)
            threaded(client_socket , addr)
        else:
            print("keyboardInterrupt")
            bServerLoopEnd = True
            break

def threaded(client_socket , addr):
    print("Connect by : " , addr[0] , ":" , addr[1])

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print("Disconnected by " + addr[0] , ":" , addr[1])
                break
            print("Recived from" + addr[0] , ":" , addr[1] , data.decode())
            client_socket.send(data)
        except ConnectionResetError as e:
            print("Disconnected by" + addr[0] , ":" , addr[1])
            break
       
    client_socket.close()

HOST = "127.0.0.1"
PORT = 9999
server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
server_socket.bind((HOST , PORT))
server_socket.listen()

print("server start")

while True:
    print("wait")
    client_socket , addr = server_socket.accept()
    start_new_thread(threaded , (client_socket , addr))
    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.Key.esc:
                print(event.key)
                print("프로그램 종료")
                break
    break
print("프로그램을 종료합니다.")
server_socket.close()

