import cv2

fps = 30
velocidad_reproduccion = int(1000/fps)

video = cv2.VideoCapture('./videos/video.avi')

if not video.isOpened():
    print( 'No es posible abrir el archivo.' )
    exit()

while True:
    ret, frame = video.read()

    if not ret:
        print('Reproduccion finalizada.')
        break
    
    cv2.imshow('webcam', frame)
    if cv2.waitKey(velocidad_reproduccion) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()