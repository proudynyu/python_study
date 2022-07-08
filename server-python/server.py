import socket
import pickle

HEADSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(4)

while True:
    clientConnect, adress = s.accept()
    print(f'Connection estabilished with {adress}')

    d = {
        1: 'Dictionary',
        2: 'Object send',
        3: 'With pickle'
    }
    msg = pickle.dumps(d)
    msg = bytes(f'{len(msg):<{HEADSIZE}}', 'utf-8') + msg

    print(msg)
    clientConnect.send(msg)