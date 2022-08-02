import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("0.0.0.0", 26257))
server.listen(1)
import socket
client_socket, addr = server.accept()
import socket
while True:
    if c := client_socket.recv(1):
        sys.stdout.write("%c" % c)
        sys.stdout.flush()
