from sqlalchemy import Column, Integer, String, Float
from database import Base

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    street = Column(String, index=True)
    city = Column(String, index=True)
    state = Column(String, index=True)
    country = Column(String, index=True)
    latitude = Column(Float, index=True)
    longitude = Column(Float, index=True)