import socket
HOST = '127.0.0.1'    # The remote host
PORT = 5429              # The same port as used by the server

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
    s.close()
    print('Received', repr(data))

except socket.error:
    print("Error in socket creation.")
