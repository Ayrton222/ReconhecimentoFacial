import os
import cv2

from ConectaBanco import ConectaBanco


class FaceTrainer:
    def __init__(self, diretorio_imagens):
        self.diretorio_imagens = diretorio_imagens
        if not os.path.exists(diretorio_imagens):
            os.makedirs(diretorio_imagens)

    def gerar_nome_arquivo(self, ra):
        ultimos_4_digitos = ra[-4:]
        quantidade_imagens = len([nome for nome in os.listdir(self.diretorio_imagens) if os.path.isfile(os.path.join(self.diretorio_imagens, nome))])
        return f"ra_{ultimos_4_digitos}_{quantidade_imagens + 1}.png"

    def treinar_modelo(self, imagem, ra):
        banco = ConectaBanco()

        # Gerar nome do arquivo
        nome_arquivo = self.gerar_nome_arquivo(ra)
        caminho_arquivo = os.path.join(self.diretorio_imagens, nome_arquivo)

        # Salvar a imagem no diretório
        cv2.imwrite(caminho_arquivo, imagem)
        print(f"Imagem de treino salva no diretório com sucesso: {caminho_arquivo}")

        # Converter a imagem para bytes
        imagem_bytes = cv2.imencode('.png', imagem)[1].tobytes()

        # Verificar se o aluno já está cadastrado no banco de dados
        verificaRa = banco.consultaAlunoPorRA(ra)
        if verificaRa is not None:
            print(f"Aluno do RA {ra} já cadastrado.")
        else:
            banco.insereAluno(ra, imagem_bytes)
            print("Imagem de treino salva no banco de dados com sucesso!")