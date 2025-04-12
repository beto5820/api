from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import random
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "A API do Beto está online!"}

def extrair_nome_do_produto(link):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        resposta = requests.get(link, headers=headers)
        soup = BeautifulSoup(resposta.text, "html.parser")
        titulo = soup.find("title")
        if titulo:
            return titulo.text.split("|")[0].strip()
        return "Produto Incrível"
    except:
        return "Produto Incrível"

@app.get("/vender")
def vender(link: str):
    nome_produto = extrair_nome_do_produto(link)

    frases_iniciais = [
        "🚀 Promoção exclusiva!",
        "🔥 Não perca essa chance!",
        "🎯 Produto com qualidade e preço justo!",
        "💥 Oferta imperdível só hoje!",
    ]

    gatilhos = [
        "✅ Frete grátis para todo Brasil!",
        "🛡️ Compra segura com garantia de 7 dias.",
        "💳 Parcele em até 12x no cartão!",
        "📦 Entrega rápida e segura!",
    ]

    texto = f"""{random.choice(frases_iniciais)}\n\n{nome_produto}\n\n👉 {link}\n\n{random.choice(gatilhos)}"""

    imagem_url = "https://via.placeholder.com/600x400.png?text=" + nome_produto.replace(" ", "+")

    return {
        "nome": nome_produto,
        "texto": texto,
        "imagem_url": imagem_url
    }
