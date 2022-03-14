from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , relationship, backref, joinedload
from sqlalchemy import Column, INTEGER, String, ForeignKey
import pprint
DATABASE_NAME = 'NewDataBase.db'
Base=declarative_base()

class Person(Base):
    __tablename__="Person"
    id = Column(INTEGER , primary_key=True)
    Name = Column(String)
    LastName=Column(String)
    Password=Column(String)
    Level = Column(String)
    Location = Column(String)
    Duty = Column(String)
    ActiveTime = Column(String)
    ActiveStatus = Column(String)
    Mail= Column(String)
   # chatdata = relationship("Chat", backref="Person")
    def __init__(self ,**kwargs):
     self.Name=kwargs["Name"]
     self.LastName=kwargs["LastName"]
     self.Password=kwargs["Password"]
     self.Level=kwargs["Level"]
     self.Location=kwargs["Location"]
     self.Duty=kwargs["Duty"]
     self.ActiveTime=kwargs["ActiveTime"]
     self.ActiveStatus=kwargs["ActiveStatus"]
     self.Mail=kwargs["Mail"]

class Chat(Base):
    __tablename__ = "Chat"
    id = Column(INTEGER, primary_key=True)
    OperateData = Column(String)
    EncryptionMethod = Column(String)
    PublicKey = Column(String)
    PrivateKey = Column(String)
    UserName = Column(String)
    Port = Column(String)
    Host = Column(String)
    Identify = Column(String)
    person_id = Column(INTEGER, ForeignKey('Person.id'))
    person = relationship("Person", backref=backref("Chat"))
    def __init__(self, **kwargs):
        self.OperateData=kwargs["OperateData"]
        self.EncryptionMethod=kwargs["EncryptionMethod"]
        self.PublicKey=kwargs["PublicKey"]
        self.PrivateKey=kwargs["PrivateKey"]
        self.UserName=kwargs["UserName"]
        self.Port=kwargs["Port"]
        self.Host=kwargs["Host"]
        self.Identify=kwargs["Identify"]
engine = create_engine(f'sqlite:///{DATABASE_NAME}', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session=Session()
#b1=Person(Name="Rustam",LastName="Cavid",Password="Bardak675", Level="3", Location="tenza", Duty="Solder", ActiveTime="23.03.2016",ActiveStatus="Active",Mail="No")
#b1.Chat=[Chat(OperateData="NoData",EncryptionMethod="RSA",PublicKey="HDHSJZ^$#Z",PrivateKey="Kdqwhqw",UserName="Kara", Port="6666", Host="112.123.12.12",Identify="21288181" ),Chat(OperateData="NoData",EncryptionMethod="RSA",PublicKey="HDHSJZ^$#Z",PrivateKey="Kdqwhqw",UserName="Kara", Port="6666", Host="112.123.12.12",Identify="21288181" ) ]
#per=session.query(Person)

#session.add(b1)
session.commit()
session.close()

