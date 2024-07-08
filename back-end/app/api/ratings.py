from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/ratings/", response_model=schemas.Rating)
def create_rating(rating: schemas.Rating, db: Session = Depends(get_db)):
    return crud.create_rating(db=db, rating=rating)

@router.get("/ratings/{rating_id}", response_model=schemas.Rating)
def read_rating(rating_id: int, db: Session = Depends(get_db)):
    db_rating = crud.get_rating(db=db, rating_id=rating_id)
    if db_rating is None:
        raise HTTPException(status_code=404, detail="Rating not found")
    return db_rating

@router.put("/ratings/{rating_id}", response_model=schemas.Rating)
def update_rating(rating_id: int, rating: schemas.Rating, db: Session = Depends(get_db)):
    db_rating = crud.update_rating(db=db, rating_id=rating_id, rating=rating)
    if db_rating is None:
        raise HTTPException(status_code=404, detail="Rating not found")
    return db_rating

@router.delete("/ratings/{rating_id}", response_model=schemas.Rating)
def delete_rating(rating_id: int, db: Session = Depends(get_db)):
    db_rating = crud.delete_rating(db=db, rating_id=rating_id)
    if db_rating is None:
        raise HTTPException(status_code=404, detail="Rating not found")
    return db_rating
