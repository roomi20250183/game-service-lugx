from pydantic import BaseModel
from typing import Optional

class GameBase(BaseModel):
    title: str
    category: Optional[str] = None
    price: Optional[float] = None
    release_date: Optional[str] = None

class GameCreate(GameBase):
    pass

class GameResponse(GameBase):
    id: int

    class Config:
        orm_mode = True

