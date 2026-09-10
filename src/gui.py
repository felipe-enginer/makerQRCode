import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from src.generator import gerar_qrcode

class QRCodeApp:

    def __init__(self, root: tk.Tk):
        self.root = root  # salvamento de janela principal
        self.root.title("Gerador de QR Code")
        self.root.geometry("400x500")
        self.root.resizable(False, False) 

        self.img_tk = None

        self._construir_interface()

    def _construir_interface(self):
        # 1. Título principal
        lbl_titulo = ttk.Label(
            self.root, text="Gerador de QR Code", font=("Helvetica", 16, "bold")
        )
        lbl_titulo.pack(pady=15)

        # 2. Rótulo de instrução
        lbl_instrucao = ttk.Label(
            self.root, text="Digite a URL ou texto abaixo:", font=("Helvetica", 10)
        )
        lbl_instrucao.pack(pady=5)

        # 3. Campo de entrada de texto
        self.ent_conteudo = ttk.Entry(self.root, width=40)
        self.ent_conteudo.pack(pady=5)
        self.ent_conteudo.focus() 

        # 4. Botão para gerar
        btn_gerar = ttk.Button(
            self.root, text="Gerar QR Code", command=self._processar_geracao
        )
        btn_gerar.pack(pady=15)

        # 5. Espaço reservado para a imagem
        self.lbl_imagem = ttk.Label(self.root, text="O QR Code aparecerá aqui")
        self.lbl_imagem.pack(pady=10)

        # 6. Rótulo para mensagens de status
        self.lbl_status = ttk.Label(self.root, text="", font=("Helvetica", 9))
        self.lbl_status.pack(pady=5)

    def _processar_geracao(self):
        conteudo = self.ent_conteudo.get().strip()  # pega o conteúdo do campo de entrada e remove espaços em branco
        try:
            caminho_imagem = gerar_qrcode(conteudo)  # def que gera o código qr
            imagem_pill = Image.open(caminho_imagem)  # abrir a imagem que é gerada
            imagem_redimensionada = imagem_pill.resize((180, 180))  # tamanho compatível
            self.img_tk = ImageTk.PhotoImage(imagem_redimensionada)  # converte para formato compatível com Tkinter
            self.lbl_imagem.config(image=self.img_tk, text=" ")
            self.lbl_status.config(
                text="QR Code gerado!", foreground="purple"
            )
        except ValueError as e:
            self.lbl_status.config(text=str(e), foreground="black")
        except Exception as e:
            self.lbl_status.config(
                text=f"Erro ao gerar QR Code: {str(e)}", foreground="black"
            )