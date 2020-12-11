import socket
port=80
ip_address=input("enter the ip_address")
sock = socket.socket()
try:
    sock.connect((ip_address,port))
    print("port is open")
except:
    print("port is closed")

