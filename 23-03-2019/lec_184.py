import socket

host="localhost"
port=4000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

print("Server listing to a port : ",port)

s.listen(1)
c,addr=s.accept()
print("Connection from : ",str(addr))
s.send(b"Hello how are you?")
s.send("bye".encode())
c.close()