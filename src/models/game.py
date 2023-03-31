from models.base import Base
from sqlalchemy import Integer, Column, String, Float


class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    platform = Column(String(32), nullable=False)
    price = Column(Float, nullable=False)
    amount = Column(Integer, nullable=False)

    def __init__(self, name, platform, price, amount):
        self.name = name
        self.platform = platform
        self.price = price
        self.amount = amount

    def __repr__(self):  # Print the object with information
        return "<Game(name='%s', platform='%s', price='%s', amount='%s')>" % (self.name, self.platform, self.price, self.amount)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "platform": self.platform,
            "price": self.price,
            "amount": self.amount
        }
