import cv2
import os
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
