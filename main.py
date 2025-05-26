import tkinter as tk
from tkinter import simpledialog
import math
import random
from botoes import criar_botoes

def imprimir_mensagem(mensagem):
    print(mensagem)

#Função ON/OFF do potão de adicionar vértice
def toggle_adicionar_vertice():
    global adicionar_vertice, botao_adicionar
    adicionar_vertice = not adicionar_vertice
    if adicionar_vertice:
        botao_adicionar.config(text="Modo Adição!!!")
        print("Modo de adição de vértice ATIVADO.")
    else:
        botao_adicionar.config(text="Adicionar Poste")
        print("Modo de adição de vértice DESATIVADO.")
        
# Função para adicionar um vértice no ponto clicado
def adicionar_vertice(event):
    global adicionar_vertice
    
    if not adicionar_vertice:
        return
    x, y = event.x, event.y
    raio = 5  # raio do círculo (vértice)

    canvas.create_oval(x - raio, y - raio, x + raio, y + raio, fill="blue", outline="black")

    nome_vertice = f"V{len(vertices) + 1}"

    canvas.create_text(x, y - 10, text=nome_vertice, fill="black", font=("Helvetica", 10, "bold"))

    vertices.append({"nome": nome_vertice, "x": x, "y": y})

    print(f"{nome_vertice} criado em ({x}, {y})")
    

# Função para criar conexões automáticas com base no raio
def criar_conexoes():
    if not vertices:
        print("Nenhum vértice para conectar.")
        return

    # Pergunta ao usuário qual vértice ele quer conectar
    nome_selecionado = simpledialog.askstring("Selecionar Vértice", "Digite o nome do vértice:")

    if not nome_selecionado:
        print("Nenhum vértice selecionado.")
        return

    # Procura o vértice selecionado
    vertice_origem = next((v for v in vertices if v["nome"] == nome_selecionado), None)

    if not vertice_origem:
        print(f"Vértice {nome_selecionado} não encontrado.")
        return

    raio_conexao = 70  # raio de distância (pixels)

    for vertice_destino in vertices:
        if vertice_destino["nome"] == vertice_origem["nome"]:
            continue  # não conectar consigo mesmo

        distancia = math.sqrt(
            (vertice_origem["x"] - vertice_destino["x"]) ** 2 +
            (vertice_origem["y"] - vertice_destino["y"]) ** 2
        )

        # Arredonda a distância para o número inteiro mais próximo
        distancia_int = round(distancia)

        if distancia_int <= raio_conexao:
            # Escolhe uma cor aleatória para a conexão
            cor = random.choice(["red", "green", "blue", "purple", "orange", "cyan", "magenta", "gold", "pink"])
            # Criar a conexão visual (linha colorida)
            canvas.create_line(
                vertice_origem["x"], vertice_origem["y"],
                vertice_destino["x"], vertice_destino["y"],
                fill=cor, width=2
            )
            # Exibe o peso (distância) ao lado da linha
            canvas.create_text(
                (vertice_origem["x"] + vertice_destino["x"]) / 2,
                (vertice_origem["y"] + vertice_destino["y"]) / 2,
                text=str(distancia_int),
                fill="black",
                font=("Helvetica", 10, "bold")
            )
            # (Opcional) salvar essa conexão numa lista de arestas
            arestas.append((vertice_origem["nome"], vertice_destino["nome"], distancia_int))
            print(f"Conexão criada: {vertice_origem['nome']} -> {vertice_destino['nome']} (Distância: {distancia_int})")

def remover_vertice():
    if not vertices:
        print("Nenhum vértice para remover.")
        return

    nome_remover = simpledialog.askstring("Remover Vértice", "Digite o nome do vértice a remover:")
    
    if not nome_remover:
        print("Nenhum vértice informado.")
        return
    
    vertice_remover = next((v for v in vertices if v["nome"] == nome_remover), None)
    if not vertice_remover:
        print(f"Vértice {nome_remover} não encontrado.")
        return
    
    vertices.remove(vertice_remover)
    global arestas
    arestas = [a for a in arestas if a[0] != nome_remover and a[1] != nome_remover]
    canvas.delete("all")
    for v in vertices:
        canvas.create_oval(v["x"] - 5, v["y"] - 5, v["x"] + 5, v["y"] + 5, fill="blue", outline="black")
        canvas.create_text(v["x"], v["y"] - 10, text=["nome"], fill="black", font=("Helvetica", 10, "bold"))
    for a in arestas:
        v1 = next(v for v in vertices if v["nome"] == a[0])
        v2 = next(v for v in vertices if v["nome"] == a[1])
        canvas.create_line(v1["x"], v1["y"], v2["x"], v2["y"], fill="gray", width=2)
        canvas.create_text(
            (v1["x"] + v2["x"]) / 2,
            (v1["y"] + v2["y"]) / 2,
            text=str(a[2]),
            fill="black",
            font=("Helvetica", 10, "bold")
        )
    print(f"Vértice {nome_remover} e suas conexões removidas.")
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gerenciador de Rede Elétrica")
    root.geometry("800x600")
    root.configure(bg="#f0f0f0")

    # Divisão da Tela
    canvas_grafos = tk.Frame(root, width=600, height=600, bg="white")
    canvas_botoes = tk.Frame(root, width=200, height=600, bg="#f0f0f0")

    canvas_grafos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    canvas_botoes.pack(side=tk.RIGHT, fill=tk.Y)

    canvas = tk.Canvas(canvas_grafos, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    # Listas para armazenar vértices e arestas
    vertices = []
    arestas = []

    # Vincular o clique no canvas para criar vértices
    canvas.bind("<Button-1>", adicionar_vertice)

    # Botões
    try:
        botao_conexoes = criar_botoes(canvas_botoes, "Conexões", largura=150, altura=50, raio=20)
        botao_conexoes.config(command=criar_conexoes)
        botao_conexoes.pack(pady=20, padx=10)
    except Exception as e:
        print(f"Erro ao criar botão 'Conexões': {e}")

    try:
        botao_adicionar = criar_botoes(canvas_botoes, "Adicionar Poste", largura=150, altura=50, raio=20)
        botao_adicionar.config(command=toggle_adicionar_vertice)
        botao_adicionar.pack(pady=20, padx=10)
    except Exception as e:
        print(f"Erro ao criar botão 'Adicionar Poste': {e}")

    try:
        botao_recalcular = criar_botoes(canvas_botoes, "Recalcular Caminho", largura=150, altura=50, raio=20)
        botao_recalcular.config(command=lambda: imprimir_mensagem("Recalcular Caminho"))
        botao_recalcular.pack(pady=20, padx=10)
    except Exception as e:
        print(f"Erro ao criar botão 'Recalcular Caminho': {e}")
        
    try:
        botao_remover = criar_botoes(canvas_botoes, "Remover Poste", largura=150, altura=50, raio=20)
        botao_remover.config(command=remover_vertice)
        botao_remover.pack(pady=20, padx=10)
    except Exception as e:
        print(f"Error ao criar botão 'Remover Poste: {e}")
    adicionar_vertice = False
    
    root.mainloop()