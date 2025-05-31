import tkinter as tk
from tkinter import simpledialog
import math
import random
import heapq
from botoes import criar_botoes

# =====================
# Variáveis Globais
# =====================
vertices = []
arestas = []
adicionar_vertice = False

# =====================
# Funções do Algoritmo MST (Prim)
# =====================
def gerar_mst():
    """Gera e desenha a MST usando o algoritmo de Prim apenas com as arestas existentes."""
    if not vertices:
        print("Nenhum vértice para gerar MST.")
        return
    if not arestas:
        print("Nenhuma aresta existente para gerar MST.")
        return
    
    todas_arestas = arestas.copy()  # Usar apenas as arestas já adicionadas manualmente
    mst = prim_mst(todas_arestas)
    
    canvas.delete("mst")  # Remove MST anterior

    # Remove conexões que estão na MST para evitar sobreposição
    for u, v, peso in mst:
        tag1 = f"conexao_{u}_{v}"
        tag2 = f"conexao_{v}_{u}"
        canvas.delete(tag1)
        canvas.delete(tag2)

    # Desenha a nova MST
    for u, v, peso in mst:
        desenhar_aresta_mst(u, v, peso)

def prim_mst(todas_arestas):
    """Implementa o algoritmo de Prim para encontrar a MST"""
    if not todas_arestas:
        return []
    
    adj = {}
    for u, v, w in todas_arestas:
        if u not in adj: adj[u] = []
        if v not in adj: adj[v] = []
        adj[u].append((v, w))
        adj[v].append((u, w))  # Grafo não direcionado
    
    start = todas_arestas[0][0]
    visited = set([start])
    min_heap = []
    
    for v, w in adj[start]:
        heapq.heappush(min_heap, (w, start, v))
    
    mst_edges = []
    
    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        if v not in visited:
            visited.add(v)
            mst_edges.append((u, v, weight))
            
            for vizinho, peso in adj[v]:
                if vizinho not in visited:
                    heapq.heappush(min_heap, (peso, v, vizinho))
    
    return mst_edges

def desenhar_aresta_mst(u, v, peso):
    """Desenha uma aresta da MST no canvas"""
    v1 = next((vert for vert in vertices if vert["nome"] == u), None)
    v2 = next((vert for vert in vertices if vert["nome"] == v), None)
    
    if not v1 or not v2:
        return
    
    raio = 12
    dx = v2["x"] - v1["x"]
    dy = v2["y"] - v1["y"]
    distancia = math.sqrt(dx**2 + dy**2)
    
    x1 = v1["x"] + (dx * raio / distancia if distancia != 0 else 0)
    y1 = v1["y"] + (dy * raio / distancia if distancia != 0 else 0)
    x2 = v2["x"] - (dx * raio / distancia if distancia != 0 else 0)
    y2 = v2["y"] - (dy * raio / distancia if distancia != 0 else 0)
    
    canvas.create_line(x1, y1, x2, y2, fill="#E71D36", width=2, dash=(4, 2), tags="mst")
    canvas.create_text(
        (x1 + x2)/2, (y1 + y2)/2,
        text=str(round(peso)),
        fill="#000000",
        font=("Helvetica", 10, "bold"),
        tags="mst"
    )

def criar_conexoes():
    if not vertices:
        print("Nenhum vértice para conectar.")
        return

    raio_conexao = 200  # raio de distância (pixels)
    raio = 12          # raio do círculo do vértice

    for i, vertice_origem in enumerate(vertices):
        for j, vertice_destino in enumerate(vertices):
            if i >= j:
                continue  # evita duplicidade e auto-conexão

            dx = vertice_destino["x"] - vertice_origem["x"]
            dy = vertice_destino["y"] - vertice_origem["y"]
            distancia = math.sqrt(dx ** 2 + dy ** 2)
            distancia_int = round(distancia)

            if distancia_int <= raio_conexao and distancia != 0:
                # Calcula os pontos ajustados para a linha começar/terminar na borda do círculo
                x1 = vertice_origem["x"] + dx * raio / distancia
                y1 = vertice_origem["y"] + dy * raio / distancia
                x2 = vertice_destino["x"] - dx * raio / distancia
                y2 = vertice_destino["y"] - dy * raio / distancia

                # ...dentro de criar_conexoes...
                tag_conexao = f"conexao_{vertice_origem['nome']}_{vertice_destino['nome']}"
                canvas.create_line(
                    x1, y1, x2, y2,
                    fill="#14213D",
                    width=2,
                    tags=("conexao", tag_conexao)
                )
                canvas.create_text(
                    (x1 + x2) / 2,
                    (y1 + y2) / 2,
                    text=str(distancia_int),
                    fill="#FCA311",
                    font=("Helvetica", 10, "bold"),
                    tags=("conexao", tag_conexao)
                )
                arestas.append((vertice_origem["nome"], vertice_destino["nome"], distancia_int))
                print(f"Conexão criada: {vertice_origem['nome']} <-> {vertice_destino['nome']} (Distância: {distancia_int})")
# =====================
# Funções de Interface
# =====================
def toggle_adicionar_vertice():
    global adicionar_vertice, botao_adicionar
    adicionar_vertice = not adicionar_vertice
    
    if adicionar_vertice:
        botao_adicionar.config(text="Modo Adição")
        print("Modo de adição de vértice ATIVADO.")
    else:
        botao_adicionar.config(text="Adicionar Poste")
        print("Modo de adição de vértice DESATIVADO.")

def adicionar_vertice(event):
    global adicionar_vertice
    
    if not adicionar_vertice:
        return
    
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    raio = 12
    
    canvas.create_oval(x - raio, y - raio, x + raio, y + raio, fill="#FCA311", outline="black")
    nome_vertice = f"V{len(vertices) + 1}"
    canvas.create_text(x, y, text=nome_vertice, fill="#14213D", font=("Helvetica", 9, "bold"))
    vertices.append({"nome": nome_vertice, "x": x, "y": y})
    print(f"{nome_vertice} criado em ({x}, {y})")

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
        raio = 12
        canvas.create_oval(v["x"] - raio, v["y"] - raio, v["x"] + raio, v["y"] + raio, fill="#FCA311", outline="black")
        canvas.create_text(v["x"], v["y"], text=v["nome"], fill="#14213D", font=("Helvetica", 9, "bold"))
    
    for a in arestas:
        v1 = next(v for v in vertices if v["nome"] == a[0])
        v2 = next(v for v in vertices if v["nome"] == a[1])
        canvas.create_line(v1["x"], v1["y"], v2["x"], v2["y"], fill="#E5E5E5", width=2)
        canvas.create_text(
            (v1["x"] + v2["x"])/2, (v1["y"] + v2["y"])/2,
            text=str(a[2]),
            fill="#14213D",
            font=("Helvetica", 10, "bold")
        )
    print(f"Vértice {nome_remover} e suas conexões removidas.")
    
     # Recalcula e redesenha a MST automaticamente
    gerar_mst()

# =====================
# Eventos do Canvas
# =====================
def comecar_arrastar(event):
    canvas.scan_mark(event.x, event.y)

def arrastar(event):
    canvas.scan_dragto(event.x, event.y, gain=1)

# =====================
# Configuração da Interface
# =====================
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gerenciador de Rede Elétrica")
    root.geometry("800x600")
    root.configure(bg="#f0f0f0")

    # Frames principais
    canvas_grafos = tk.Frame(root, width=600, height=600, bg="white")
    canvas_botoes = tk.Frame(root, width=200, height=600, bg="#f0f0f0")
    
    # Scrollbars
    scroll_y = tk.Scrollbar(canvas_grafos, orient="vertical")
    scroll_x = tk.Scrollbar(canvas_grafos, orient="horizontal")
    
    # Canvas principal
    canvas = tk.Canvas(
        canvas_grafos, 
        bg="white",
        yscrollcommand=scroll_y.set,
        xscrollcommand=scroll_x.set,
        width=600,
        height=600,
        scrollregion=(0, 0, 2000, 2000)
    )
    
    scroll_y.config(command=canvas.yview)
    scroll_x.config(command=canvas.xview)
    
    # Layout dos componentes
    canvas_grafos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    canvas_botoes.pack(side=tk.RIGHT, fill=tk.Y)
    
    canvas.grid(row=0, column=0, sticky="nsew")
    scroll_y.grid(row=0, column=1, sticky="ns")
    scroll_x.grid(row=1, column=0, sticky="ew")
    canvas_grafos.grid_rowconfigure(0, weight=1)
    canvas_grafos.grid_columnconfigure(0, weight=1)

    # Eventos do canvas
    canvas.bind("<ButtonPress-3>", adicionar_vertice)
    canvas.bind("<ButtonPress-1>", comecar_arrastar)
    canvas.bind("<B1-Motion>", arrastar)
    canvas.bind("<ButtonPress-2>", comecar_arrastar)
    canvas.bind("<B2-Motion>", arrastar)

    # Botões da interface
    try:
        botao_conexoes = criar_botoes(canvas_botoes, "Conexões", "#FCA311","#14213D", largura=150, altura=50, raio=20)
        botao_conexoes.config(command=criar_conexoes)
        botao_conexoes.pack(pady=20, padx=10)
    except Exception as e:
        print(f"Erro ao criar botão 'Conexões': {e}")
        
    try:
        botao_adicionar = criar_botoes(canvas_botoes, "Adicionar Poste","#FCA311","#14213D", largura=150, altura=50, raio=20)
        botao_adicionar.config(command=toggle_adicionar_vertice)
        botao_adicionar.pack(pady=20, padx=10)
    except Exception as e:
        print(f"Erro ao criar botão 'Adicionar Poste': {e}")
        
    try:
        botao_remover = criar_botoes(canvas_botoes, "Remover Poste","#FCA311","#14213D", largura=150, altura=50, raio=20)
        botao_remover.config(command=remover_vertice)
        botao_remover.pack(pady=20, padx=10)
    except Exception as e:
        print(f"Error ao criar botão 'Remover Poste: {e}")
    
    try:
        botao_caminho = criar_botoes(canvas_botoes, "Gerar MST", "#FCA311", "#14213D", largura=150, altura=50, raio=20)
        botao_caminho.config(command=gerar_mst)
        botao_caminho.pack(pady=20, padx=10)
    except Exception as e:
        print(f"Erro ao criar botão 'Gerar MST': {e}")

    root.mainloop()