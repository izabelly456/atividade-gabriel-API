import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

load_dotenv()

def conectar():
    try:
        conexao = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )
        cursor = conexao.cursor(cursor_factory=RealDictCursor)
        return conexao, cursor
    except Exception as e:
        print(f"Erro ao conectar no banco: {e}")
        return None, None
