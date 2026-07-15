from fastapi import FastAPI

from routes import produto, estoque, historico_estoque

app = FastAPI(
    title="Estokai API"
)

#app.include_router(produto.router)
app.include_router(estoque.router)
#app.include_router(historico_estoque.router)