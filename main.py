import cv2
import tkinter as tk
from tkinter import messagebox
from ConectaBanco import ConectaBanco
from FaceCapture import FaceCapture
from FaceTrainer import FaceTrainer
from FaceVerifier import FaceVerifier
from FormataRa import FormataRa

class FaceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition App")

        # Define o tamanho da janela (largura x altura)
        window_width = 400
        window_height = 300

        # Centraliza a janela na tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int(screen_height/2 - window_height/2)
        position_right = int(screen_width/2 - window_width/2)

        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        self.diretorio_imagens = 'imagens'
        self.diretorio_comparacao = 'imagens_comparacao'

        self.face_capture = FaceCapture()
        self.face_trainer = FaceTrainer(self.diretorio_imagens)
        self.face_verifier = FaceVerifier(self.diretorio_comparacao, self.diretorio_imagens)

        self.banco = ConectaBanco()
        self.banco.criaBanco()

        self.create_widgets()

    def create_widgets(self):
        self.ra_label = tk.Label(self.root, text="Digite seu RA:")
        self.ra_label.pack(pady=10)

        self.ra_entry = tk.Entry(self.root, font=("Arial", 14))
        self.ra_entry.pack(pady=10)

        self.train_button = tk.Button(self.root, text="Treinar", font=("Arial", 14), command=self.train)
        self.train_button.pack(pady=10)

        self.verify_button = tk.Button(self.root, text="Verificar", font=("Arial", 14), command=self.verify)
        self.verify_button.pack(pady=10)

        self.exit_button = tk.Button(self.root, text="Sair", font=("Arial", 14), command=self.root.quit)
        self.exit_button.pack(pady=10)

    def train(self):
        ra = self.ra_entry.get()
        raformatado = FormataRa.formataRa(ra)

        imagem = self.face_capture.capturar_e_reconhecer_rosto()
        if imagem is not None:
            self.face_trainer.treinar_modelo(imagem, ra)
            messagebox.showinfo("Sucesso", "Modelo treinado com sucesso!")
        else:
            messagebox.showerror("Erro", "Falha na captura da imagem. Tente novamente.")

    def verify(self):
        ra = self.ra_entry.get()
        raformatado = FormataRa.formataRa(ra)

        imagem = self.face_capture.capturar_e_reconhecer_rosto()
        if imagem is not None:
            imagem_referencia = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
            imagem_banco = self.banco.consultaFotoAlunoPorRA(ra)
            if imagem_banco:
                imagem_mais_semelhante, acuracia = self.face_verifier.verificar_imagem(imagem_referencia, imagem_banco)
                messagebox.showinfo("Resultado", f"A imagem mais semelhante é: {imagem_mais_semelhante} com acurácia de {acuracia:.2f}")
                self.banco.atualiza_presenca(ra, 1)
            else:
                messagebox.showerror("Erro", "Imagem de referência não encontrada no banco de dados.")
        else:
            messagebox.showerror("Erro", "Falha na captura da imagem. Tente novamente.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceApp(root)
    root.mainloop()