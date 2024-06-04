import os
import cv2
import numpy as np

class ImageProcessor:
    @staticmethod
    def calcular_similaridade(img1, img2):
        img2_redimensionada = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
        diferenca = cv2.absdiff(img1, img2_redimensionada)
        return np.mean(diferenca)

    @staticmethod
    def carregar_imagens(diretorio):
        imagens = []
        for arquivo in os.listdir(diretorio):
            if arquivo.endswith(".png"):
                caminho_imagem = os.path.join(diretorio, arquivo)
                imagem = cv2.imread(caminho_imagem)
                imagens.append((caminho_imagem, imagem))
        return imagens

class FaceVerifier:
    def __init__(self, diretorio_comparacao):
        self.diretorio_comparacao = diretorio_comparacao
        if not os.path.exists(diretorio_comparacao):
            os.makedirs(diretorio_comparacao)

    def verificar_imagem(self, imagem_referencia, imagem_bd):
        similaridade_minima = float('inf')
        imagem_mais_semelhante = None

        h, w, _ = imagem_referencia.shape

        imagem_bytes = np.frombuffer(imagem_bd, dtype=np.uint8)
        imagem_decodificada = cv2.imdecode(imagem_bytes, cv2.IMREAD_COLOR)
        print(f"fImagem banco: {imagem_decodificada}")
        similaridade_bd = ImageProcessor.calcular_similaridade(imagem_referencia, imagem_decodificada)
        if similaridade_bd < similaridade_minima:
            imagem_mais_semelhante = "Imagem do banco de dados"
            similaridade_minima = similaridade_bd

        acuracia = 1 - similaridade_minima
        caminho_imagem_comparacao = os.path.join(self.diretorio_comparacao, f'imagem_comparacao.png')
        cv2.imwrite(caminho_imagem_comparacao, imagem_referencia)
        return imagem_mais_semelhante, acuracia
