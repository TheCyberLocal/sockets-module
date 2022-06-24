import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'pythonprogramming.net'
port = 80


def pscan(port):
    try:
        s.connect((server, port))
        return True
    except:
        return False


for x in range(1, 26):
    if pscan(x):
        print(f'Port {x} is open')
    else:
        print(f'Port {x} is closed')
