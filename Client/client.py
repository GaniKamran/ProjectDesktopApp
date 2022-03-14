import sys
import socket
import pickle
import threading
from PyQt5 import QtWidgets
from PyQt5.QtGui import QTextCursor
from Client.ChatGui import Ui_Form
from PyQt5 import QtCore
import random


from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
class client(QMainWindow, Ui_Form, QDialog):
    def __init__(self, parent=None):
        super(client,self).__init__(parent)

        self.setupUi(self)

        SERVER_ADDRESS = '127.0.0.1'
        SERVER_PORT = 12000
        self.Name="Rasul"
        try:
            # Instantiate socket and start connection with server
            self.socket_instance = socket.socket()
            self.socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))
            # Create a thread in order to handle messages sent by server
            threading.Thread(target=self.handle_messages, args=[self.socket_instance]).start()

            print('Connected to chat!')

            # Read user's input until it quit from chat and close connection




        except Exception as e:
            print(f'Error connecting to server socket {e}')
            self.socket_instance.close()

        self.pushButton_8.clicked.connect(self.clientz)




    def ClickPAramentrs(self):
        self.show()

    def handle_messages(self,connection: socket.socket):
        '''
            Receive messages sent by the server and display them to user
        '''

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
            self.textEdit_2.clear()
            Name=self.Name
            textms = Name + " : " + msg
            self.textEdit.append(textms)
            # Parse message to utf-8
            self.socket_instance.send(msg.encode())





if(__name__=="__main__"):

    app=QApplication(sys.argv)
    myWin=client()
    myWin.show()
    sys.exit(app.exec_())