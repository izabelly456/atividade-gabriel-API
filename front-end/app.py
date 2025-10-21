import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de Loja", page_icon="🛒")
st.title("🛍️ Gerenciador de Produtos da Loja")

menu = st.sidebar.radio("Navegação", ["Catálogo", "Adicionar Produto"])

if menu == "Catálogo":
    st.subheader("Produtos disponíveis")
    response = requests.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            st.dataframe(produtos)
        else:
            st.info("Nenhum produto cadastrado")
    else:
        st.error("Erro ao acessar a API")

if menu == "Adicionar Produto":
    st.subheader("Adicionar novo produto")
    nome = st.text_input("Nome do Produto")
    categoria = st.text_input("Categoria")
    preco = st.number_input("Preço", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade", min_value=0, step=1)
    if st.button("Salvar Produto"):
        dados = {
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "quantidade": quantidade
        }
        response = requests.post(f"{API_URL}/produtos", params=dados)
        if response.status_code == 200:
            st.success("Produto adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar produto")
