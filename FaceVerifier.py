import os
import cv2
import numpy as np

class ImageProcessor:
    @staticmethod
    def calcular_similaridade(img1, img2):
        diferenca = cv2.absdiff(img1, img2)
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
    def __init__(self, diretorio_imagens, diretorio_comparacao):
        self.diretorio_imagens = diretorio_imagens
        self.diretorio_comparacao = diretorio_comparacao
        if not os.path.exists(diretorio_comparacao):
            os.makedirs(diretorio_comparacao)

    def verificar_imagem(self, imagem_referencia):
        imagens = ImageProcessor.carregar_imagens(self.diretorio_imagens)

        similaridade_minima = float('inf')
        imagem_mais_semelhante = None

        h, w, _ = imagem_referencia.shape

        for caminho, imagem in imagens:
            imagem_redimensionada = cv2.resize(imagem, (w, h))
            similaridade = ImageProcessor.calcular_similaridade(imagem_referencia, imagem_redimensionada)
            if similaridade < similaridade_minima:
                similaridade_minima = similaridade
                imagem_mais_semelhante = caminho

        acuracia = 1 - similaridade_minima
        caminho_imagem_comparacao = os.path.join(self.diretorio_comparacao, f'imagem_comparacao.png')
        cv2.imwrite(caminho_imagem_comparacao, imagem_referencia)
        return imagem_mais_semelhante, acuracia