from socket import socket,AF_INET,SOCK_STREAM
s = socket(AF_INET,SOCK_STREAM)
s.connect(("127.0.0.1", 5000))

while True:
    send_data = input("client >>> : ") 
    send_data = send_data.encode("utf-8")
    s.send(send_data)
    print(s.recv(1024).decode("utf-8"))
s.close()

