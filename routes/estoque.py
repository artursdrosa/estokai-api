from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from models.estoque import Estoque
from schemas.estoque import EstoqueRead, EstoqueUpdate

router = APIRouter(
    prefix="/estoque",
    tags=["Estoque"]
)

@router.get("/", response_model=list[EstoqueRead])
async def get_estoque(db: Session = Depends(get_db)):
    return db.query(Estoque).all()

@router.get("/{id_produto}", response_model=EstoqueRead)
async def get_produto_by_id(id_produto: int, db: Session = Depends(get_db)):
    estoque = db.query(Estoque).filter(Estoque.id_produto == id_produto).first()
    if not estoque:
        raise HTTPException(status_code=404, detail="Produto not found")
    return estoque

@router.post("/", response_model=EstoqueRead, status_code=201)
async def cadastrar_produto_no_estoque(estoque_create: EstoqueRead, db: Session = Depends(get_db)):
    estoque = Estoque(**estoque_create.model_dump())
    db.add(estoque)
    db.commit()
    db.refresh(estoque)
    return estoque


@router.put("/{id_produto}", response_model=EstoqueRead)
async def update_estoque(id_produto: int, estoque_update: EstoqueUpdate, db: Session = Depends(get_db)):
    estoque = db.query(Estoque).filter(Estoque.id_produto == id_produto).first()
    if not estoque:
        raise HTTPException(status_code=404, detail="Produto not found")
    
    if estoque_update.quantidade is not None:
        estoque.quantidade = estoque_update.quantidade
    
    db.commit()
    db.refresh(estoque)
    return estoque

@router.delete("/{id_produto}", status_code=204)
async def deletar_produto_do_estoque(id_produto: int, db: Session = Depends(get_db)):
    estoque = db.query(Estoque).filter(Estoque.id_produto == id_produto).first()
    if not estoque:
        raise HTTPException(status_code=404, detail="Produto not found")
    
    db.delete(estoque)
    db.commit()
    return None