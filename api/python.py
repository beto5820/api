from fastapi import FastAPI, Request 
from fastapi.responses import JSONResponse
import random

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "A API do Beto está online!"}

@app.get("/produto")
def produto():
    return {
        "nome": "Produto Top",
        "preço": "R$ 99,90",
        "descrição": "Esse produto é ótimo pra quem quer praticidade e qualidade!"
    }

@app.get("/vender")
def vender(link: str):
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
        "📦 Entrega rápida e segura!"
    ]

    texto = f"""{random.choice(frases_iniciais)}\n
Confira esse produto incrível:\n
👉 {link}\n
{random.choice(gatilhos)}"""

    imagem_url = "https://via.placeholder.com/600x400.png?text=Imagem+do+Produto"

    return {
        "texto": texto,
        "imagem_url": imagem_url
    }
