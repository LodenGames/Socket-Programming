import socket

HOST = ''
PORT = 53333

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(b'back at you TCP')
            print(f"Server Received: {data.decode()}") 