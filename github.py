from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox
import socket

def handleCalc():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('10.20.133.78', 80))
    cmd = 'GET http://10.20.133.78/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
        break
        #print(data.decode(), end='')
        textEdit.appendPlainText(data.decode())
        #QMessageBox.about(window,a)
    mysock.close()
app = QApplication([])
window = QMainWindow()
window.resize(200, 100)
window.move(200, 400）
window.setWindowTitle('socket')
textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("需求内容")
textEdit.move(10,25)
textEdit.resize(200,400)
button = QPushButton('显示', window)
button.move(350,100)
window.show()
button.clicked.connect(handleCalc)
app.exec_()
