import socket
import pickle

HEADSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))


while True:
    full_msg = b''
    new_msg = True

    while True:
        msg = s.recv(16)

        if new_msg:
            print(f'new msg length: {msg[:HEADSIZE]}')
            msglen = int(msg[:HEADSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg)-HEADSIZE == msglen:
            print('Full msg recvd')
            
            d = pickle.loads(full_msg[HEADSIZE:])
            new_msg = True
            full_msg = b''
print(msg)
print(d)