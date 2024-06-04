import os
import cv2

from ConectaBanco import ConectaBanco


class FaceTrainer:
    def __init__(self):
        pass

    def treinar_modelo(self, imagem, ra):
        banco = ConectaBanco()

        # Converter a imagem para bytes
        imagem_bytes = cv2.imencode('.png', imagem)[1].tobytes()

        verificaRa = banco.consultaAlunoPorRA(ra)
        if verificaRa is not None:
            print(f"Aluno do RA {ra} já cadastrado.")
        else:
            banco.insereAluno(ra, imagem_bytes)
            print("Imagem de treino salva no banco de dados com sucesso!")
