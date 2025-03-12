from socket import socket,AF_INET,SOCK_STREAM
s = socket(AF_INET,SOCK_STREAM)
s.bind(("127.0.0.1", 5000))
s.listen(1)
c, a = s.accept()
print(f"connected from {a}")

while True:
    data =c.recv(1024).decode("utf-8")
    if not data:
        break
    else:
        print(data)
        send_data = input("server >>> : ")
        send_data = send_data.encode("utf-8")
        c.send(send_data)  