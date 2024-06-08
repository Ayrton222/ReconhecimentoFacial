import os
import cv2
import numpy as np

from ImageProcessor import ImageProcessor


class FaceVerifier:
    def __init__(self, diretorio_comparacao, diretorio_imagens):
        self.diretorio_comparacao = diretorio_comparacao
        self.diretorio_imagens = diretorio_imagens
        if not os.path.exists(diretorio_comparacao):
            os.makedirs(diretorio_comparacao)

    def verificar_imagem(self, imagem_referencia, imagem_bd):
        similaridade_minima = float('inf')
        imagem_mais_semelhante = None

        # Verificar a imagem no banco de dados
        imagem_bytes = np.frombuffer(imagem_bd, dtype=np.uint8)
        imagem_decodificada = cv2.imdecode(imagem_bytes, cv2.IMREAD_COLOR)
        similaridade_bd = ImageProcessor.calcular_similaridade(imagem_referencia, imagem_decodificada)
        if similaridade_bd < similaridade_minima:
            imagem_mais_semelhante = "Imagem do banco de dados"
            similaridade_minima = similaridade_bd

        # Verificar imagens no diretório
        imagens = ImageProcessor.carregar_imagens(self.diretorio_imagens)
        for caminho_imagem, imagem in imagens:
            similaridade = ImageProcessor.calcular_similaridade(imagem_referencia, imagem)
            if similaridade < similaridade_minima:
                imagem_mais_semelhante = caminho_imagem
                similaridade_minima = similaridade

        acuracia = 1 - similaridade_minima
        caminho_imagem_comparacao = os.path.join(self.diretorio_comparacao, 'imagem_comparacao.png')
        cv2.imwrite(caminho_imagem_comparacao, imagem_referencia)
        return imagem_mais_semelhante, acuracia