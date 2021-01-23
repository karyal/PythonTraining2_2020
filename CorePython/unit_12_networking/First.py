import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)
print(mysocket)# <socket.socket fd=524, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.0.104', 51428), raddr=('192.241.136.170', 80)>
while True:
    data = mysocket.recv(512)
    if len(data)<1:
        break
    print(data.decode(), end='')
mysocket.close()