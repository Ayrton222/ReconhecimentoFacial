# Reconhecimento facial

### Requisitos
 - Python versão 3 ou superior
 - Biblioteca cv2
 - Biblioteca ``mediapipe`` 
 - Biblioteca ``numpy``

### Importação das  bibliotecas
É recomendando usar um editor proprio da linguagem python ``(Pycharm ou jupiter)`` mas com outras IDES também é possivel rodar a aplicação, para instalar as bibliotecas va para o terminal do projeto e digite:

### Importar cv2:

pip install opencv-python

### Importar mediapipe

pip install mediapipe

### Importar numpy

pip install numpy

### Como utilizar 

A aplicação assim que inciada ela ira aparecer 3 opções no terminal para o usuario escolher (digitar) uma delas:

- Opção 1: Treinar
- Opção 2: Verificar
- Opção 3: sair

### Treinar

A aplicação ira abrir uma janela mostrando a webcam, e ira mostrar um frame reconhecendo o rosto da pessoa. Para tirar a foto é necessario apertar a tecla "ESC" do teclado. Após tirar a foto, a aplicação ira abrir um outro frame exibindo o rosto que foi detectado e como a foto ira ser armazenada,
apos o usuario fechar ambos os frames, a aplicação ira salvar essa imagem no diretório imagens.

### Verificar

A aplicação ira abrir uma janela moostrando a webcam e ira mostrar um frame reconhecendo o rosto da pessoa. Assim que a tecla "ESC" for pressionada, a aplicação ira tirar uma foto do rosto da pessoa e ira exibir um frame mostrando a imamgem do rosto que foi detectado,
apos o usuario fechar ambos os frames, a aplicação ira salvar a imagem no diretorio imagens_comparacao, e ira exibir no terminal com qual das imagens contida no diretorio "imagens" a foto tirada mais se parece, e ira exibir a accurance da comparação realizada.
