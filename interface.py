import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
import os

ARQUIVO_PLANILHA = 'clientes.xlsx'

def carregar_dados():
    if os.path.exists(ARQUIVO_PLANILHA):
        return pd.read_excel(ARQUIVO_PLANILHA)
    else:
        df = pd.DataFrame(columns=['Nome', 'CPF/CNPJ', 'Produto', 'Quantidade', 'Valor', 'E-mail', 'Telefone', 'Observação', 'Emitir', 'Enviar Email', 'Enviar WhatsApp'])
        df.to_excel(ARQUIVO_PLANILHA, index=False)
        return df

def salvar_dados(df):
    df.to_excel(ARQUIVO_PLANILHA, index=False)

def adicionar_cliente():
    def salvar():
        novo = {
            'Nome': nome.get(),
            'CPF/CNPJ': cpf.get(),
            'Produto': produto.get(),
            'Quantidade': quantidade.get(),
            'Valor': valor.get(),
            'E-mail': email.get(),
            'Telefone': telefone.get(),
            'Observação': obs.get(),
            'Emitir': False,
            'Enviar Email': False,
            'Enviar WhatsApp': False
        }
        df.loc[len(df)] = novo
        salvar_dados(df)
        atualizar_lista()
        janela.destroy()

    janela = tk.Toplevel(root)
    janela.title("Adicionar Cliente")

    campos = ['Nome', 'CPF/CNPJ', 'Produto', 'Quantidade', 'Valor', 'E-mail', 'Telefone', 'Observação']
    entradas = {}

    for i, campo in enumerate(campos):
        tk.Label(janela, text=campo).grid(row=i, column=0)
        entradas[campo] = tk.Entry(janela)
        entradas[campo].grid(row=i, column=1)

    nome, cpf, produto = entradas['Nome'], entradas['CPF/CNPJ'], entradas['Produto']
    quantidade, valor, email = entradas['Quantidade'], entradas['Valor'], entradas['E-mail']
    telefone, obs = entradas['Telefone'], entradas['Observação']

    tk.Button(janela, text="Salvar", command=salvar).grid(row=len(campos), column=0, columnspan=2)

def excluir_cliente():
    selecionado = lista.curselection()
    if selecionado:
        index = selecionado[0]
        df.drop(index, inplace=True)
        df.reset_index(drop=True, inplace=True)
        salvar_dados(df)
        atualizar_lista()
    else:
        messagebox.showinfo("Info", "Selecione um cliente para excluir.")

def atualizar_lista():
    lista.delete(0, tk.END)
    for i, row in df.iterrows():
        lista.insert(tk.END, f"{row['Nome']} | {row['Produto']} | Emitir: {row['Emitir']}")

def marcar_para_emissao():
    selecionado = lista.curselection()
    if selecionado:
        index = selecionado[0]
        df.at[index, 'Emitir'] = not df.at[index, 'Emitir']
        salvar_dados(df)
        atualizar_lista()

def enviar_para_agente():
    selecionados = df[df['Emitir'] == True]
    if selecionados.empty:
        messagebox.showwarning("Aviso", "Nenhum cliente marcado para emissão.")
    else:
        # Aqui entrará a automação da NFe
        messagebox.showinfo("Agente", f"{len(selecionados)} clientes enviados para o agente de nota fiscal!")

# Interface principal
root = tk.Tk()
root.title("Agente Automação Nota Fiscal")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

lista = tk.Listbox(frame, width=80, height=15)
lista.pack()

botao_frame = tk.Frame(root)
botao_frame.pack(pady=5)

tk.Button(botao_frame, text="Cadastrar Cliente", command=adicionar_cliente).grid(row=0, column=0, padx=5)
tk.Button(botao_frame, text="Excluir", command=excluir_cliente).grid(row=0, column=1, padx=5)
tk.Button(botao_frame, text="Marcar para Emissão", command=marcar_para_emissao).grid(row=0, column=2, padx=5)
tk.Button(botao_frame, text="Enviar para o Agente", command=enviar_para_agente).grid(row=0, column=3, padx=5)

df = carregar_dados()
atualizar_lista()

root.mainloop()
