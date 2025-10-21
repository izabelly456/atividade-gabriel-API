from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    categoria VARCHAR(50),
                    preco DECIMAL(10,2),
                    quantidade INT
                )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()


def inserir_produto(nome, categoria, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                INSERT INTO produtos (nome, categoria, preco, quantidade)
                VALUES (%s, %s, %s, %s)
            """, (nome, categoria, preco, quantidade))
            conexao.commit()
        except Exception as erro:
            raise Exception(f"Erro ao adicionar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()


def listar_produtos():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("SELECT * FROM produtos")
            return cursor.fetchall()
        except Exception as erro:
            raise Exception(f"Erro ao listar produtos: {erro}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_produto(id, preco=None, quantidade=None):
    conexao, cursor = conectar()
    if conexao:
        try:
            linhas_afetadas = 0
            if preco is not None:
                cursor.execute("UPDATE produtos SET preco = %s WHERE id = %s", (preco, id))
                linhas_afetadas += cursor.rowcount
            if quantidade is not None:
                cursor.execute("UPDATE produtos SET quantidade = %s WHERE id = %s", (quantidade, id))
                linhas_afetadas += cursor.rowcount
            conexao.commit()
            return linhas_afetadas > 0
        except Exception as erro:
            raise Exception(f"Erro ao atualizar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()


def excluir_produto(id):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
            conexao.commit()
            return cursor.rowcount > 0
        except Exception as erro:
            raise Exception(f"Erro ao excluir produto: {erro}")
        finally:
            cursor.close()
            conexao.close()


