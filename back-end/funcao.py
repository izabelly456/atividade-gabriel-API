from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id SERIAL PRIMARY KEY,
                    nome TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    preco REAL NOT NULL,
                    quantidade INTEGER NOT NULL
                )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()

criar_tabela()

def inserir_produto(nome, categoria, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
                (nome, categoria, preco, quantidade)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

def listar_produto():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("SELECT * FROM produtos ORDER BY id")
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar produtos: {erro}")
        finally:
            cursor.close()
            conexao.close()

def buscar_produto(id_produto):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("SELECT * FROM produtos WHERE id = %s", (id_produto,))
            return cursor.fetchone()
        except Exception as erro:
            print(f"Erro ao buscar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_preco(id_produto, novo_preco):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("UPDATE produtos SET preco = %s WHERE id = %s", (novo_preco, id_produto))
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar preço: {erro}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_quantidade(id_produto, nova_quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("UPDATE produtos SET quantidade = %s WHERE id = %s", (nova_quantidade, id_produto))
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar quantidade: {erro}")
        finally:
            cursor.close()
            conexao.close()

def deletar_produto(id_produto):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
            conexao.commit()
            return cursor.rowcount > 0
        except Exception as erro:
            print(f"Erro ao deletar produto: {erro}")
            return False
        finally:
            cursor.close()
            conexao.close()
