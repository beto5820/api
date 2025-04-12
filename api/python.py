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

    # Simulação de imagem com IA (você vai trocar isso depois por uma real)
    imagem_url = "https://via.placeholder.com/600x400.png?text=Imagem+do+Produto"

    return {
        "texto": texto,
        "imagem_url": imagem_url
    }
