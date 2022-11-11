import socket
import os
def sendfile(s):
    str1 = s.recv(1024)
    filename = str1.decode('utf-8')
    print('The rerver1 requests my file:%s', filename)
    if os.path.exists(filename):
        print('I have %s, begin to download!' % filename)
        s.send(b'yes')
        s.recv(1024)
        size = 1024
        with open(filename, 'rb') as f:
            while True:
                data = f.read(size)
                s.send(data)
                if len(data) < size:
                    break
        print('%s is downloaded successfully!' % filename)
    else:
        print('Sorry, I have no %s' % filename)
        s.send(b'no')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8585))
while True:
    sendfile(s)
s.close()