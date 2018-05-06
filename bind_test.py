import socket
import server.start
import time
mb = socket.socket()
mb.bind((("127.0.0.1",8484)))
mb.listen(1000)
sok,addr=mb.accept()
sok.send("hello")
print sok.recv(1024444)
# mb.connect(("192.168.1.114",8484))
# mes = mb.recv(1024)
# print mes.encode('hex')
# mb.send("hello")
# print(mb.recv(1024).encode('hex'))