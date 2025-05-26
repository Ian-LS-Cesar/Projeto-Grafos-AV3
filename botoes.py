import tkinter as tk
from PIL import ImageTk, Image, ImageDraw


def criar_botoes(master, texto, cor, cor_texto, largura=150, altura=10, raio=2):
    try:
        # Validações
        if largura <= 0 or altura <= 0:
            raise ValueError("Largura e altura devem ser maiores que zero.")
        if raio < 0 or raio > min(largura, altura) // 2:
            raise ValueError("Raio deve ser não negativo e menor que metade da largura ou altura.")

        # Criar imagem com bordas arredondadas
        imagem = Image.new("RGBA", (largura, altura), (0, 0, 0, 0))
        draw = ImageDraw.Draw(imagem)
        draw.rounded_rectangle((0, 0, largura, altura), radius=raio, fill=cor)
        imagem_tk = ImageTk.PhotoImage(imagem)

        # Criar botão
        botao = tk.Button(
            master,
            text=texto,
            font=("Helvetica", 13),
            fg=cor_texto,
            relief="flat",
            highlightcolor="#f0f0f0",  # Cor corrigida
            bd=0,
            image=imagem_tk,
            compound="center"
            
        )

        botao.image = imagem_tk  # Evitar garbage collection
        return botao

    except Exception as e:
        print(f"Erro ao criar botão: {e}")
        return None