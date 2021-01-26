import socket


# by default it take ipv4 address
# 1. type of network ip4
# 2. type of network tcp,dcp
s = socket.socket()

print('Socket created ')

# ip address and port number
# range for the port number is 0 to 65535
s.bind(('localhost',9999)) 

s.listen(3)
print('Waiting for connections !!')

while True:
    c,address = s.accept()
    name = c.recv(1024).decode()
    print('Connected with ',address,name)

    c.send(bytes('Welcome to Server','utf-8'))

    c.close()
