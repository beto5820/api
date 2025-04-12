from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import random
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "🚀 A API do Beto está online e vendendo!"}

def extrair_nome_do_produto(link):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        resposta = requests.get(link, headers=headers, timeout=10)
        soup = BeautifulSoup(resposta.text, "html.parser")
        titulo = soup.find("title")
        if titulo:
            nome = titulo.text.split("|")[0].strip()
            return nome if len(nome) < 100 else nome[:97] + "..."
        return "Produto Incrível"
    except Exception as e:
        return "Produto Incrível"

@app.get("/vender")
def vender(link: str):
    nome_produto = extrair_nome_do_produto(link)

    frases_iniciais = [
        "🔥 Oferta especial que vai acabar rápido!",
        "🚀 Promoção imperdível do dia!",
        "🎯 Chegou o produto que você procurava!",
        "💥 Desconto exclusivo para você!",
    ]

    gatilhos = [
        "✅ Frete grátis para todo Brasil!",
        "🛡️ Compra protegida com garantia de 7 dias.",
        "💳 Parcele em até 12x sem juros!",
        "📦 Entrega rápida e segura!",
    ]

    texto_pronto = f"""{random.choice(frases_iniciais)}\n\n{nome_produto}\n\n👉 {link}\n\n{random.choice(gatilhos)}"""

    imagem_url = f"https://via.placeholder.com/600x400.png?text={nome_produto.replace(' ', '+')}"

    return {
        "nome": nome_produto,
        "texto": texto_pronto,
        "imagem_url": imagem_url
    }
