import cv2

captura = cv2.VideoCapture('Salida de video.avi')
#grabacion=cv2.VideoWriter('Salida de video.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
while (captura.isOpened()):
	ret,imagen = captura.read()
	if ret==True:
		cv2.imshow('video',imagen)
		#grabacion.write(imagen)
		if cv2.waitKey(30) & 0xFF == ord('s'):
			break
			pass
	else: break
captura.release()
#grabacion.release()
cv2.destroyAllWindows()
