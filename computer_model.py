from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()
 

class ComputerModel(Base):
    __tablename__ = "computer"
        
    com_id = Column(Integer, primary_key=True)
    name = Column(Integer)
    price = Column(String)
    ram = Column(String)
    disk = Column(String)
    quantity = Column(String)

    def __init__(self, com_id, name, price, ram, disk, quantity):
        self.com_id = com_id
        self.name = name
        self.price = price
        self.ram = ram
        self.disk = disk
        self.quantity = quantity


    def __str__(self):
        return "Computer-Id = %d, Name = %s, Price = %s, Ram Size = %s, Disk Size = %s Quantity = %s" % (self.com_id, self.name, self.price, self.ram, self.disk, self.quantity)

