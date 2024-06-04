import os
import cv2

class FaceTrainer:
    def __init__(self, diretorio_imagens):
        self.diretorio_imagens = diretorio_imagens
        if not os.path.exists(diretorio_imagens):
            os.makedirs(diretorio_imagens)

    def treinar_modelo(self, imagem, raformatado):
        contador_imagem = len(os.listdir(self.diretorio_imagens))
        print("Salvando imagem de treino...")
        caminho_imagem_rosto = os.path.join(self.diretorio_imagens, f'ra{raformatado}_{contador_imagem}.png')
        cv2.imwrite(caminho_imagem_rosto, imagem)
        print(f"Imagem {caminho_imagem_rosto} de treino salva com sucesso!")