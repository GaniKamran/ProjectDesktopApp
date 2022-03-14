import sys
import socket, threading
from ServerUI import Ui_Form
from PyQt5 import QtWidgets
from PyQt5.QtGui import QTextCursor
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
class serverDesk(QMainWindow, Ui_Form, QDialog):
    def __init__(self, parent=None):
        super(serverDesk,self).__init__(parent)
        self.setupUi(self)
        self.Host=self.lineEdit_2.text()
        self.Port=12000



        con1=[]
        self.connections=con1


        self.pushButton_8.clicked.connect(self.server)

    def handle_user_connection(self,connection: socket.socket, address: str) -> None:
        '''
            Get user connection in order to keep receiving their messages and
            sent to others users/connections.
        '''
        while True:
            try:
                # Get client message
                msg = connection.recv(1024)

                # If no message is received, there is a chance that connection has ended
                # so in this case, we need to close connection and remove it from connections list.
                if msg:
                    # Log message sent by user
                    print(f'{address[0]}:{address[1]} - {msg.decode()}')

                    # Build message format and broadcast to users connected on server
                    msg_to_send = f'From {address[0]}:{address[1]} - {msg.decode()}'
                    self.broadcast(msg_to_send, connection)

                # Close connection if no message was sent
                else:
                    self.remove_connection(connection)
                    break

            except Exception as e:
                print(f'Error to handle user connection: {e}')
                self.remove_connection(connection)
                break

    def broadcast(self, message: str, connect: socket.socket) -> None:
        '''
            Broadcast message to all users connected to the server
        '''
        connection1=self.connections
        # Iterate on connections in order to send message to all client's connected
        for client_conn in connection1:
            # Check if isn't the connection of who's send
            if client_conn != connect:
                try:
                    # Sending message to client connection
                    client_conn.send(message.encode())

                # if it fails, there is a chance of socket has died
                except Exception as e:
                    print('Error broadcasting message: {e}')
                    self.remove_connection(client_conn)

    def remove_connection(self, conn: socket.socket) -> None:
        '''
            Remove specified connection from connections list
        '''
        connection1=self.connections
        if conn in connection1:
            # Close socket connection and remove connection from connections list
            conn.close()
            connection1.remove(conn)

    def server(self) -> None:
        '''
            Main process that receive client's connections and start a new thread
            to handle their messages
        '''
        self.connections


        try:
            # Create server and specifying that it can only handle 4 connections by time!
            socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_instance.bind((self.Host, self.Port))
            socket_instance.listen(4)

            print('Server running!')

            while True:
                # Accept client connection
                socket_connection, address = socket_instance.accept()
                # Add client connection to connections list
                self.connections.append(socket_connection)
                # Start a new thread to handle client connection and receive it's messages
                # in order to send to others connections
                threading.Thread(target=self.handle_user_connection, args=[socket_connection, address]).start()

        except Exception as e:
            print(f'An error has occurred when instancing socket: {e}')
        finally:
            # In case of any problem we clean all connections and close the server connection
            if len(self.connections) > 0:
                for conn in self.connections:
                    self.remove_connection(conn)

            socket_instance.close()


if(__name__=="__main__"):
    app=QApplication(sys.argv)
    myWin=serverDesk()
    myWin.show()
    sys.exit(app.exec_())