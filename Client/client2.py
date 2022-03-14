import sys
import socket,threading
from PyQt5 import QtWidgets
from PyQt5.QtGui import QTextCursor

from ChatGui import Ui_Form
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
class client2(QMainWindow, Ui_Form, QDialog):

    def __init__(self, parent=None):
        super(client2,self).__init__(parent)

        self.setupUi(self)
        # Socket IO
        self.StartChatProssecces()

        self.pushButton_8.clicked.connect(self.clientz)



    def StartChatProssecces(self):
        SERVER_ADDRESS = '127.0.0.2'
        SERVER_PORT = 12000
        self.Name = "Gani"
        try:
            # Instantiate socket and start connection with server
            self.socket_instance = socket.socket()
            self.socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))
            # Create a thread in order to handle messages sent by server
            threading.Thread(target=self.handle_messages, args=[self.socket_instance]).start()

            print('Connected to chat!')
        except Exception as e:
            print(f'Error connecting to server socket {e}')
            self.socket_instance.close()
    def ClickPAramentrs(self):
        self.show()

    def handle_messages(self, connection: socket.socket):

        while True:
            try:
                msg = connection.recv(1024)

                # If there is no message, there is a chance that connection has closed
                # so the connection will be closed and an error will be displayed.
                # If not, it will try to decode message in order to show to user.
                if msg:
                   self.textEdit.append(msg.decode())



                else:
                    connection.close()
                    break

            except Exception as e:
                print(f'Error handling message from server: {e}')
                connection.close()
                break

    def clientz(self) -> None:
            msg = self.textEdit_2.toPlainText()
            Name=self.Name
            textms=Name+" : "+msg
            self.textEdit.append(textms)
            self.textEdit_2.clear()
            #self.textEdit.setText(self.aze)
            self.socket_instance.send(msg.encode())

if(__name__=="__main__"):

    app=QApplication(sys.argv)
    myWin=client2()
    myWin.show()
    sys.exit(app.exec_())