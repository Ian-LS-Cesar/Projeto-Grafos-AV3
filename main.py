import tkinter as tk
from botoes import criar_botoes


def imprimir_mensagem(mensagem):
    print(mensagem)

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

    # Adicionando os botões com valores válidos
    try:
        botao_conexoes = criar_botoes(canvas_botoes, "Conexões", largura=150, altura=50, raio=20)
        botao_conexoes.config(command=lambda: imprimir_mensagem("Conexões"))
        botao_conexoes.pack(pady=20, padx=10)
    except Exception as e:
        print(f"Erro ao criar botão 'Conexões': {e}")

    try:
        botao_adicionar = criar_botoes(canvas_botoes, "Adicionar Poste", largura=150, altura=50, raio=20)
        botao_adicionar.config(command=lambda: imprimir_mensagem("Adicionar Poste"))
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
        botao_remover.config(command=lambda: imprimir_mensagem("Remover Poste"))
        botao_remover.pack(pady=20, padx=10)
    except Exception as e:
        print(f"Error ao criar botão 'Remover Poste: {e}")

    root.mainloop()