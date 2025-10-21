from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import funcao

app = FastAPI(title="Estoque De Produtos")

class ProdutoCreate(BaseModel):
    nome: str
    categoria: str
    preco: float
    quantidade: int

class ProdutoUpdate(BaseModel):
    preco: Optional[float] = None
    quantidade: Optional[int] = None

@app.get("/")
def home():
    return {"mensagem": "API Produtos funcionando!"}

@app.post("/produtos")
def criar_produto(produto: ProdutoCreate):
    funcao.inserir_produto(produto.nome, produto.categoria, produto.preco, produto.quantidade)
    return {"mensagem": "Produto adicionado com sucesso!"}

@app.get("/produtos")
def listar_produtos():
    produtos = funcao.listar_produtos()
    return {"produtos": produtos}

@app.put("/produtos/{produto_id}")
def atualizar_produto(produto_id: int, dados: ProdutoUpdate):
    if dados.preco is None and dados.quantidade is None:
        raise HTTPException(status_code=400, detail="Informe preço ou quantidade para atualizar")
    sucesso = funcao.atualizar_produto(produto_id, dados.preco, dados.quantidade)
    if sucesso:
        return {"mensagem": "Produto atualizado com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.delete("/produtos/{produto_id}")
def excluir_produto(produto_id: int):
    sucesso = funcao.excluir_produto(produto_id)
    if sucesso:
        return {"mensagem": "Produto excluído com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.get("/estoque/valor-total")
def valor_total_estoque():
    total = funcao.valor_total_estoque()
    return {"valor_total_estoque": total}
