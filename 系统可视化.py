from socket import *
from tkinter import *
import tkinter

def client():
    IP = '10.128.255.255'
    SERVER_PORT = 50000
    BUFLEN = 1024

    dataSocket = socket(AF_INET, SOCK_STREAM)

    dataSocket.connect((IP, SERVER_PORT))

    while True:
        toSend = input('>>>')
        if toSend == 'exit':
            break
        dataSocket.send(toSend.encode())

        receved = dataSocket.recv(BUFLEN)
        if not receved:
            break
        print(receved.decode())

    dataSocket.close()
window =tkinter.Tk()
window.title('clientOperation')
window.geometry('400x200')

button=tkinter.Button(window,text='在客户机操作',bg='#CC33CC', command=lambda : client())
button.pack()
top=mainloop()
