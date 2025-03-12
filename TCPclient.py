import socket
import time

HOST = "127.0.0.1"    # The remote host
PORT = 53333              # The same port as used by the server
data = 0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) # blocking so start time right after send msg
    # s.sendall(b'hello TCP') # for part a
    start = time.perf_counter() # in seconds
    # data = s.recv(1024) # for part a
    for i in range(1000):
        s.sendall(b'hello TCP')
        data = s.recv(1024)
    end = time.perf_counter()
print('Client Received: ', repr(data))
print(f'TCP RTT: {((end - start) * 1000):.20f} ms') # * 1000 to convert s to ms