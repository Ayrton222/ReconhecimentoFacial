# Reconhecimento Facial

## Requisitos

- Python versão 3 ou superior
- Biblioteca `cv2`
- Biblioteca `mediapipe`
- Biblioteca `numpy`

## Importação das bibliotecas

É recomendando usar um editor próprio da linguagem Python (como PyCharm ou Jupyter), mas com outras IDEs também é possível rodar a aplicação. Para instalar as bibliotecas, vá para o terminal do projeto e digite:

### Importar cv2

```sh
pip install opencv-python
```

### Importar mediapipe

```sh
pip install mediapipe
```

### Importar numpy

```sh
pip install numpy
```

## Como utilizar

A aplicação, assim que iniciada, irá apresentar 3 opções no terminal para o usuário escolher (digitando uma delas):

- Opção 1: Treinar
- Opção 2: Verificar
- Opção 3: Sair

### Treinar

A aplicação irá abrir uma janela mostrando a webcam, e irá exibir um frame reconhecendo o rosto da pessoa. Para tirar a foto é necessário apertar a tecla **ESC** do teclado. Após tirar a foto, a aplicação irá abrir outro frame exibindo o rosto que foi detectado e como a foto será armazenada. Após o usuário fechar ambos os frames, a aplicação irá salvar essa imagem no diretório `imagens`.

### Verificar

A aplicação irá abrir uma janela mostrando a webcam e exibirá um frame reconhecendo o rosto da pessoa. Assim que a tecla **ESC** for pressionada, a aplicação irá tirar uma foto do rosto da pessoa e exibirá um frame mostrando a imagem do rosto que foi detectado. Após o usuário fechar ambos os frames, a aplicação irá salvar a imagem no diretório `imagens_comparacao`, e exibirá no terminal com qual das imagens contidas no diretório `imagens` a foto tirada mais se parece, além de exibir a acurácia da comparação realizada.
