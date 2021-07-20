# # import socket
# # # 접속할 주소 여기서는 loopback
# # HOST = "127.0.0.1"
# # # 클라이언트 접속을 대기하는 포트 번호
# # PORT = 9999
# # # 소켓 객체를 생성
# # # 주소 체계(address family)로 IPv4 , 소켓  타입으로 TCP 사용
# # server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
# # # 포트사용중이라 연결할 수 없다는 
# # # winError 10048 에러 해결을 위해 필요합니다.
# # server_socket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)

# # # bind 함수는 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결하는데 사용됨
# # # HOST는 hostname , ip address , 빈 문자열 ""이 될 수 있습니다.
# # # 빈 문자열이면 모든 네트워크 인터페이스로부터의 접속을 허용합니다.
# # # portsms 1-65545 사이의 숫자를 사용할 수 있습니다.
# # server_socket.bind((HOST , PORT))

# # # 서버가 클라이언트의 접속을 허용하도록 합니다.
# # server_socket.listen()
# # print("Server listen")
# # # accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴합니다.
# # client_socket , addr = server_socket.accept()
# # # 접속한 클라이언트의 주소
# # print("Connected by" , addr)

# # while True:
# #     # 클라이언트가 보낸 메세지를 수신하기 위해 대기
# #     data = client_socket.recv(1024)
# #     # 빈 문자열을 수신하면 루프를 중지합니다.
# #     if not data:
# #         break
# #     # 수신받은 문자열을 출력
# #     print("Received from" , addr , data.decode())

# #     client_socket.sendall(data)

# # client_socket.close()
# # server_socket.close()

# print("================================================================")

# import socket
# from _thread import *

# def threaded(client_socket , addr):
#     print("Connect by : " , addr[0] , ":" , addr[1])

#     while True:
#         try:
#             data = client_socket.recv(1024)
#             if not data:
#                 print("Disconnected by " + addr[0] , ":" , addr[1])
#                 break
#             print("Recived from" + addr[0] , ":" , addr[1] , data.decode())
#             client_socket.send(data)
#         except ConnectionResetError as e:
#             print("Disconnected by" + addr[0] , ":" , addr[1])
#             break
#     client_socket.close()

# HOST = "127.0.0.1"
# PORT = 9999
# server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
# server_socket.bind((HOST , PORT))
# server_socket.listen()

# print("server start")


# while True:
#     print("wait")
#     client_socket , addr = server_socket.accept()
#     start_new_thread(threaded , (client_socket , addr))

# server_socket.close()fimport socket

print("===============================================================")
# 서버를 실행하고 하나의 서버에 다중으로 클라이언트들을 받아들인다.
# 서버에서 하나의 클라이언트들을 받아들일때마다 threaded라는 함수를 작동(함수가 실행될때마다 새로운 클라이언트가 온다라는 뜻)
# thread는 본인의 생각으로는 개인비서라고 생각을 함 새로운 클라이언트가 들어올때마다 1 대 1로 스레드가 생성이 되고 1개의 스레드가 
# 여러개의 클라이언트들을 커버하는것이 아니라 오직 하나의 클라이언트들만 커버하기때문에 그렇다고 생각을 함

# 그리고 모든 클라이언트들이 종료가 되도 서버는 종료를 시키지 못했는데 (강제종료를 제외하고)
# pynput 모듈에 keyboard로 키보드가 눌리는 이벤트를 사용해 모든 클라이언트들이 퇴장하고 서버만 돌아가고 있는 상황에서
# esc를 press하면 "종료합니다."라는 문구와 함께 서버가 다운됨 
# 실행결과 모든부분에서 정상적으로 작동 
# 함수를 실행하는 부분(threaded)에서는 이미 break문이 있기때문에 굳이 제어코드를 넣을필요 없다고 생각을 했고
# 아래에 start new thread부분도 반복문인데 break가 보이지 않아 여기다가 키보드 이벤트 제어코드를 작성해주면 될거 같다라는 생각을 함
# 확실히 너무 어렵게 생각하지 않고 일단 내가 원하는 흐름으로 코드를 작성하고 코드를 읽은 다음 흘러가는 부분에서 추가시키고 싶은 부분은 추가시키면
# 큰 고민없이 정상적으로 코드가 작동하는 모습을 확인할 수가 있었음 
# 물론 기본적으로 코드를 이해를 해야겠지만 일단 먼저 내가 원하는 흐름의 코드를 작성을 하고 추가를 할때 어느 부분에서 넣어주면 원활하게 다시 흐름이 흘러가겠다라는
# 단순한 생각을 가지고 접근을 하니 횔씬 코드를 작성하는 부분과 추가하는 부분이 쉬웠음 (물론 내가 지금 작성한느 코드는 하나도 어려운것이 아니지만 .......)

import socket
from _thread import *
from pynput import keyboard

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

