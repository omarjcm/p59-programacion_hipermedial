import cv2

# el argumento es 0 debido que se utiliza la camara existente.
camara = cv2.VideoCapture(0)

if not camara.isOpened():
    print( 'No es posible abrir la camara.' )
    exit()

while True:
    ret, frame = camara.read()

    # si el frame se ha capturado correctamente, el valor de ret sera True
    if not ret:
        print('No es posible obtener la imagen.')
        break
    
    # Si el frame es obtenido correctamente, la imagen en frame se mostrara en una pantalla
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()