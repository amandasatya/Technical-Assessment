from sqlalchemy import Column, Integer, Float
from app.database import Base

class RatingDB(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)
