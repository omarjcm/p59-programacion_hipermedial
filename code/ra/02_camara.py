import cv2

archivo_video = './videos/video.avi'

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# Se establece que el video se almacena el contenido en la variable archivo_video con una tasa de refresco 
# de 20 cuadros/segundo y una resolucion 640x480
video = cv2.VideoWriter(archivo_video, fourcc, 20, (640, 480))

camara = cv2.VideoCapture(0)

if not camara.isOpened():
    print('No es posible abrir la camara.')
    exit()

while True:
    ret, frame = camara.read()

    if not ret:
        print('No es posible obtener la imagen.')
        break

    # Se guardan los frames captados por la camara en el archivo de video
    video.write(frame)
    cv2.imshow('webcam', frame)

    if cv2.waitKey(1) == ord('q'):
        break

camara.release()
video.release()
cv2.destroyAllWindows()