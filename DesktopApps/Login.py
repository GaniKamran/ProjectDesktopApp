import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , relationship, backref, joinedload
from sqlalchemy import Column, INTEGER, String, ForeignKey
from PyQt5 import QtWidgets
from DesktopApps.login1 import Ui_Signup
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from models.TreeModel import Person,Chat
from Client.ChooseParametrs import Choose
DATABASE_NAME = 'NewDataBase.db'
Base=declarative_base()
engine = create_engine(f'sqlite:///{DATABASE_NAME}', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
per = session.query(Person)

class Login(QMainWindow, Ui_Signup, QDialog):
    def __init__(self, parent=None):
        super(Login,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.OperUi)
        self.pushButton_2.clicked.connect(self.Allert)
        self.ParametrsCh=Choose()
    def OperUi(self):

        for person in per:
            if((self.lineEdit_2.text() == person.Password) and (self.lineEdit.text()==person.Name) ):
              self.ParametrsCh.ShowMeth()
              self.hide()
            else:
             self.label_4.setText("Access is not correct")
    def Allert(self):
        self.label_3.setText("Denied")
if(__name__=="__main__"):
    app=QApplication(sys.argv)
    myWin=Login()
    myWin.show()
    sys.exit(app.exec_())
