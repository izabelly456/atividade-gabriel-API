from fastapi import FastAPI
import funcao

# rodar o fastapi:
# python -m uvicorn api:app --reload

app = FastAPI(title="Gerenciador de Produtos")

@app.get("/")
def home():
    return {"mensagem": "API Loja funcionando!"}

@app.post("/produtos")
def criar_produto(nome: str, categoria: str, preco: float, quantidade: int):
    funcao.inserir_produto(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto adicionado com sucesso!"}

@app.get("/produtos")
def listar_produtos():
    produtos = funcao.listar_produto()
    lista = []
    for linha in produtos:
        lista.append({
            "id": linha[0],
            "nome": linha[1],
            "categoria": linha[2],
            "preco": linha[3],
            "quantidade": linha[4]
        })
    return {"produtos": lista}

@app.put("/produtos/{id_produto}")
def atualizar_produto(id_produto: int, preco_novo: float = None, quantidade_nova: int = None):
    produto = funcao.buscar_produto(id_produto)
    if not produto:
        return {"erro": "Produto não encontrado"}

    if preco_novo is not None:
        funcao.atualizar_preco(id_produto, preco_novo)
    if quantidade_nova is not None:
        funcao.atualizar_quantidade(id_produto, quantidade_nova)

    return {"mensagem": "Produto atualizado com sucesso!"}

@app.delete("/produtos/{id_produto}")
def deletar_produto(id_produto: int):
    sucesso = funcao.deletar_produto(id_produto)
    if sucesso:
        return {"mensagem": "Produto deletado com sucesso!"}
    else:
        return {"erro": "Produto não encontrado"}
