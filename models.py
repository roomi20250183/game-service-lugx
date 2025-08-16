from sqlalchemy import Column, Integer, String, Float
from database import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    category = Column(String(50))
    price = Column(Float)
    release_date = Column(String(20))


