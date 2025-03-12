import socket
import time

HOST = "127.0.0.1"    # The remote host
PORT = 53444          # The same port as used by the server
# PORT = 53333 # part d

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: #Dgram for UDP
    # s.sendto(b'Hello UDP', (HOST, PORT)) #sendto for UDP # part a

    start = time.perf_counter() # in seconds 
    # data = s.recv(1024) # part a
    for i in range(1000):
        s.sendto(b'Hello UDP', (HOST, PORT)) 
        data = s.recv(1024) # part a
    end = time.perf_counter()
print('Client Received: ', repr(data))
print(f'UDP RTT: {((end - start) * 1000):.20f} ms') # * 1000 to convert s to ms