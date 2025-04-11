from fastapi import FastAPI

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
