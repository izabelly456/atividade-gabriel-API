📦 API - Controle de Produtos e Estoque
🎯 Objetivo

Este projeto tem como objetivo o desenvolvimento de um sistema completo para gestão de produtos em uma loja, utilizando:

FastAPI para o back-end (API RESTful)

MySQL como banco de dados relacional

Streamlit para o front-end (consumo da API)

Boas práticas de organização de projeto e versionamento com Git

🛠️ Funcionalidades

A aplicação permite:

✅ Adicionar um novo produto

📃 Listar todos os produtos

✏️ Atualizar preço e/ou quantidade de um produto

❌ Excluir um produto

💰 Exibir valor total do estoque (via front-end em Streamlit)

🧱 Estrutura do Projeto
controle-estoque/
│
├── backend/
│   ├── __pychache__
│   │   ├── api.py
│   │   ├── conexao.py
│   │   ├── 
│   │   └── funcao.py
│   
│
├── frontend/
│   ├── app.py
│   
 ├──.env
├── .gitignore
└── README.md
 ├──requirements.txt

🗃️ Banco de Dados

Script para criação da tabela no MySQL:

CREATE TABLE produtos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  categoria VARCHAR(50),
  preco DECIMAL(10,2),
  quantidade INT
);

🚀 Como Rodar o Projeto
Pré-requisitos

Python 3.9+

MySQL Server

Git

1️⃣ Clonar o repositório
git clone  https://github.com/izabelly456/atividade-gabriel-API
cd 

2️⃣ Configurar o Back-end
Acessar a pasta:
cd backend

Criar e configurar o .env:
DB_HOST=localhost
DB_PORT=3306
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=nome_do_banco

Instalar dependências:
pip install -r requirements.txt

Rodar a API:
uvicorn app.main:app --reload


Acesse a documentação da API em:
📚 http://localhost:8000/docs

3️⃣ Rodar o Front-end
Acessar a pasta:
cd ../frontend

Instalar dependências:
pip install -r requirements.txt

Executar o app:
streamlit run app.py

✅ Boas Práticas Adotadas

Organização em pastas backend/ e frontend/

Uso de variáveis de ambiente com .env

Tratamento de erros e validações com Pydantic (FastAPI)

Uso de Git com commits descritivos

Documentação automática da API com Swagger UI

