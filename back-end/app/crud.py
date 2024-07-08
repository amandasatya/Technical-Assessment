from sqlalchemy.orm import Session
from app import models, schemas

def create_rating(db: Session, rating: schemas.Rating):
    db_rating = models.RatingDB(rating=rating.rating)
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating

def get_rating(db: Session, rating_id: int):
    return db.query(models.RatingDB).filter(models.RatingDB.id == rating_id).first()

def update_rating(db: Session, rating_id: int, rating: schemas.Rating):
    db_rating = db.query(models.RatingDB).filter(models.RatingDB.id == rating_id).first()
    if db_rating:
        db_rating = rating
        db.commit()
        db.refresh(db_rating)
        return db_rating
    return None

def delete_rating(db: Session, rating_id: int):
    db_rating = db.query(models.RatingDB).filter(models.RatingDB.id == rating_id).first()
    if db_rating:
        db.delete(db_rating)
        db.commit()
        return db_rating
    return None
