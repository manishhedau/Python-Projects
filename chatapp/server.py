import socket

s = socket.socket()
print("Socket created ..")

s.bind(('localhost',9999))

s.listen()
print("Waiting for connections !!")


c,address = s.accept()
name = c.recv(1024).decode()
print('Connected with ',address,name)

while True:
    msg = input('Server : ')
    msg = bytes(f'Server : {msg}','utf-8')
    c.send(msg)

    data = c.recv(1024).decode()
    print(data)