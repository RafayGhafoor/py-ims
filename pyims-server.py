import socket

HOST, PORT = '127.0.0.1', 5429

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    print("Began Listening...")
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    while 1:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)
    conn.close()

except socket.error:
    print("Error occured in creation of socket object.")
