import sys
from Encription import Ui_Form
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from client2 import client2
class Choose2(QMainWindow, Ui_Form, QDialog):
    def __init__(self, parent=None):
        super(Choose2,self).__init__(parent)
        self.cli=client2()
        self.setupUi(self)

    def AddPAramentrs1(self):
        self.cli.ClickPAramentrs()
        self.cli.Name=self.lineEdit_3.text()
        self.cli.Port=self.lineEdit_4.text()
        self.cli.ServerAdd=self.lineEdit_5.text()



if(__name__=="__main__"):
    app=QApplication(sys.argv)
    myWin=Choose2()
    myWin.show()
    sys.exit(app.exec_())