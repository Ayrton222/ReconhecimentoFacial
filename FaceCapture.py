import cv2
import mediapipe as mp

class FaceCapture:
    def __init__(self):
        self.webcam = cv2.VideoCapture(0)
        self.reconhecimento_rosto = mp.solutions.face_detection.FaceDetection()

    def capturar_e_reconhecer_rosto(self):
        while self.webcam.isOpened():
            validacao, frame = self.webcam.read()
            if not validacao:
                break

            imagem_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            lista_rostos = self.reconhecimento_rosto.process(imagem_rgb)

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
        self.webcam.release()
        return None