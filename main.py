import cv2
import mediapipe as mp
import os
import numpy as np

def calcular_similaridade(img1, img2):
    diferenca = cv2.absdiff(img1, img2)
    return np.mean(diferenca)

def carregar_imagens(diretorio):
    imagens = []
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(".png"):
            caminho_imagem = os.path.join(diretorio, arquivo)
            imagem = cv2.imread(caminho_imagem)
            imagens.append((caminho_imagem, imagem))
    return imagens

diretorio_imagens = 'imagens'
if not os.path.exists(diretorio_imagens):
    os.makedirs(diretorio_imagens)

def capturar_e_reconhecer_rosto():
    webcam = cv2.VideoCapture(0)

    reconhecimento_rosto = mp.solutions.face_detection
    reconhecedor_rosto = reconhecimento_rosto.FaceDetection()

    while webcam.isOpened():
        validacao, frame = webcam.read()
        if not validacao:
            break

        imagem_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        lista_rostos = reconhecedor_rosto.process(imagem_rgb)

        if lista_rostos.detections:
            for rosto in lista_rostos.detections:
                mp.solutions.drawing_utils.draw_detection(frame, rosto)

            cv2.imshow("Rostos na sua webcam", frame)

            tecla = cv2.waitKey(5)
            if tecla == 27:  # Tecla 'ESC'
                rosto = lista_rostos.detections[0].location_data.relative_bounding_box
                h, w, _ = frame.shape

                x_min = int(rosto.xmin * w)
                y_min = int(rosto.ymin * h)
                largura = int(rosto.width * w)
                altura = int(rosto.height * h)

                rosto_recortado = frame[y_min:y_min + altura, x_min:x_min + largura]

                cv2.imshow("Rosto Capturado", rosto_recortado)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                return rosto_recortado
    webcam.release()

def treinar_modelo(imagem):
    contador_imagem = len(os.listdir(diretorio_imagens))

    print("Salvando imagem de treino...")
    caminho_imagem_rosto = os.path.join(diretorio_imagens, f'rosto_{contador_imagem}.png')
    cv2.imwrite(caminho_imagem_rosto, imagem)
    print("Imagem de treino salva com sucesso!")
def verificar_imagem(imagem_referencia):
    diretorio_comparacao = 'imagens_comparacao'
    if not os.path.exists(diretorio_comparacao):
        os.makedirs(diretorio_comparacao)
    imagens = carregar_imagens(diretorio_imagens)

    similaridade_minima = float('inf')
    imagem_mais_semelhante = None

    h, w, _ = imagem_referencia.shape

    for caminho, imagem in imagens:

        imagem_redimensionada = cv2.resize(imagem, (w, h))
        similaridade = calcular_similaridade(imagem_referencia, imagem_redimensionada)
        if similaridade < similaridade_minima:
            similaridade_minima = similaridade
            imagem_mais_semelhante = caminho

    acuracia = 1 - similaridade_minima
    caminho_imagem_comparacao = os.path.join(diretorio_comparacao, f'imagem_comparacao.png')
    cv2.imwrite(caminho_imagem_comparacao, imagem_referencia)
    return imagem_mais_semelhante, acuracia


def main():
    while True:
        escolha = input("Escolha uma opção:\n1 - Treinar\n2 - Verificar\n3 - Sair\n")

        if escolha == "1":
            imagem = capturar_e_reconhecer_rosto()
            treinar_modelo(imagem)
            print("Modelo treinado com sucesso!")
        elif escolha == "2":
            imagem = capturar_e_reconhecer_rosto()
            imagem_referencia = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
            imagem_mais_semelhante = verificar_imagem(imagem_referencia)
            print(f"A imagem mais semelhante é: {imagem_mais_semelhante}")
        elif escolha == "3":
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
