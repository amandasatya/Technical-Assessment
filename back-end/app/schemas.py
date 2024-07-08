from pydantic import BaseModel
class Rating(BaseModel):
    rating: int

    class Config:
        orm_mode = True
