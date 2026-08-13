from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from models.estoque import Estoque
from models.produto import Produto
from schemas.produto import ProdutoRead, ProdutoUpdate, ProdutoCreate

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)

@router.post("/", response_model=ProdutoRead, status_code=201)
def criar_produto(produto_create: ProdutoCreate, db: Session = Depends(get_db)):
    """Cria o produto e insere seu registro no estoque físico, com quantidade zero."""
    produto = Produto(**produto_create.model_dump())
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto


@router.get("/", response_model=list[ProdutoRead])
def get_produtos(db: Session = Depends(get_db)):
    return db.query(Produto).all()

@router.get("/{id_produto}", response_model=ProdutoRead)
def get_produto_by_id(id_produto: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id_produto).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto not found")
    return produto


@router.put("/{id_produto}", response_model=ProdutoRead)
def update_produto(id_produto: int, produto_update: ProdutoUpdate, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id_produto).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto not found")
    
    update_data = produto_update.model_dump(exclude_unset=True)
    

    for field, value in update_data.items():
        setattr(produto, field, value)
    
    db.commit()
    db.refresh(produto)
    return produto


@router.delete("/{id_produto}", status_code=204)
def deletar_produto(id_produto: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id_produto).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto not found")

    registro_estoque = db.query(Estoque).filter(Estoque.id_produto == id_produto).first()
    if registro_estoque:
        db.delete(registro_estoque)

    db.delete(produto)
    db.commit()
