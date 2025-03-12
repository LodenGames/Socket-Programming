import socket

HOST = ''
PORT = 53444
# PORT = 53333 # part d

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: #Dgram for udp
    s.bind((HOST, PORT))
    
    while True:
        data, add = s.recvfrom(1024) # recvfrom for UDP
        if not data: break
        s.sendto(b'back at you UDP', add) # sendto for UDP
        print(f"Server Received: {data.decode()}") 