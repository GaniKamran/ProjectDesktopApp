import sys
from Client.Encription import Ui_Form
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from Client.client import client
class Choose(QMainWindow, Ui_Form, QDialog):
    def __init__(self, parent=None):
        super(Choose,self).__init__(parent)
        self.cli=client()
        self.setupUi(self)
        self.pushButton_8.clicked.connect(self.AddPAramentrs1)

    def AddPAramentrs1(self):
        self.cli.ClickPAramentrs()
    def ShowMeth(self):
        self.show()


if(__name__=="__main__"):
    app=QApplication(sys.argv)
    myWin=Choose()
    myWin.show()
    sys.exit(app.exec_())