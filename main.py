import cv2

from FaceCapture import FaceCapture
from FaceTrainer import FaceTrainer
from FaceVerifier import FaceVerifier
from FormataRa import FormataRa


def main():
    diretorio_imagens = 'imagens'
    diretorio_comparacao = 'imagens_comparacao'

    face_capture = FaceCapture()
    face_trainer = FaceTrainer(diretorio_imagens)
    face_verifier = FaceVerifier(diretorio_imagens, diretorio_comparacao)

    ra = input("Digite seu ra: ")
    raformatado = FormataRa.formataRa(ra)

    while True:
        escolha = input("Escolha uma opção:\n1 - Treinar\n2 - Verificar\n3 - Sair\n")

        if escolha == "1":
            imagem = face_capture.capturar_e_reconhecer_rosto()
            if imagem is not None:
                face_trainer.treinar_modelo(imagem, raformatado)
                print("Modelo treinado com sucesso!")
            else:
                print("Falha na captura da imagem. Tente novamente.")
        elif escolha == "2":
            imagem = face_capture.capturar_e_reconhecer_rosto()
            if imagem is not None:
                imagem_referencia = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
                imagem_mais_semelhante, acuracia = face_verifier.verificar_imagem(imagem_referencia)
                print(f"A imagem mais semelhante é: {imagem_mais_semelhante} com acurácia de {acuracia:.2f}")
            else:
                print("Falha na captura da imagem. Tente novamente.")
        elif escolha == "3":
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()