import cv2


imagen = cv2.imread('imagenes/gabriela1.jpg', 0)
cv2.imshow('Prueba de la Imagen', imagen)
cv2.imwrite('monocromatico.jpg',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()