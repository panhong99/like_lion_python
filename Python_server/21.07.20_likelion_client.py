# import socket
# # 서버의 주소 , hostname or ip address를 사용할 수 있음 
# HOST = "127.0.0.1"
# # 서버에서 지정해 놓은 포트 번호
# PORT = 9999
# # 소켓 객체를 생성
# # 주소 체계(address family)로 IPv4 , 소켓 타입으로 TCP 사용합니다.
# client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
# # 지정한 HOST와 POST를 사용하여 서버에 접속
# client_socket.connect((HOST, PORT))
# # 메세지를 전송
# client_socket.sendall("판홍".encode())
# # 메서지를 수신
# data = client_socket.recv(1024)
# print("Received" , repr(data.decode()))
# # 소켓 닫기
# client_socket.close()

import socket

HOST = "127.0.0.1"
PORT = 9999

client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client_socket.connect((HOST , PORT))

while True:
    message = input("Enter Message : ")
    if message == "quit":
        break
    client_socket.send(message.encode())
    data = client_socket.recv(1024)

    print("Received from the server : " , repr(data.decode()))

client_socket.close()