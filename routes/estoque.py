from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from models.estoque import Estoque
from schemas.estoque import EstoqueRead, EstoqueUpdate

router = APIRouter(
    prefix="/estoque",
    tags=["Estoque"]
)

@router.get("/estoque", response_model=list[EstoqueRead])
async def get_estoque(db: Session = Depends(get_db)):
    return db.query(Estoque).all()

@router.get("/estoque/{id_produto}", response_model=EstoqueRead)
async def get_estoque_by_id(id_produto: int, db: Session = Depends(get_db)):
    estoque = db.query(Estoque).filter(Estoque.id_produto == id_produto).first()
    if not estoque:
        raise HTTPException(status_code=404, detail="Estoque not found")
    return estoque


@router.put("/estoque/{id_produto}", response_model=EstoqueRead)
async def update_estoque(id_produto: int, estoque_update: EstoqueUpdate, db: Session = Depends(get_db)):
    estoque = db.query(Estoque).filter(Estoque.id_produto == id_produto).first()
    if not estoque:
        raise HTTPException(status_code=404, detail="Estoque not found")
    
    if estoque_update.quantidade is not None:
        estoque.quantidade = estoque_update.quantidade
    
    db.commit()
    db.refresh(estoque)
    return estoque