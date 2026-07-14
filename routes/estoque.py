from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from models.estoque import Estoque

router = APIRouter(
    prefix="/estoque",
    tags=["Estoque"]
)

@router.get("/")
async def get_estoque(db: Session = Depends(get_db)):
    return db.query(Estoque).all()