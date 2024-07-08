from sqlalchemy.orm import Session
from app import models, schemas

def create_rating(db: Session, rating: schemas.Rating):
    db_rating = models.RatingDB(rating=rating.rating)
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating
