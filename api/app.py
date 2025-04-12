import streamlit as st
import requests

st.title("Gerador de Texto Promocional")

link = st.text_input("Insira o link do produto:")

if st.button("Gerar Texto"):
    if not link.startswith(("http://", "https://")):
        st.error("Por favor, insira um link válido começando com http:// ou https://.")
    else:
        api_url = "https://sua-api.com/vender"  # Substitua pelo URL real da sua API
        response = requests.get(api_url, params={"link": link})
        
        if response.status_code == 200:
            data = response.json()
            st.success("Texto promocional gerado com sucesso!")
            st.write(f"**Nome do Produto:** {data['nome']}")
            st.write(f"**Texto Pronto:**\n{data['texto']}")
            st.image(data["imagem_url"], caption="Imagem Gerada")
        else:
            st.error(f"Erro ao chamar a API: {response.status_code}")