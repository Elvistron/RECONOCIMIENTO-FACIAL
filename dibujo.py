import cv2
import numpy as np


#bgr= np.zeros((300,300,3),dtype=np.uint8)
#bgr[:,:,:]=(255,0,0)


imagen=255*np.zeros((400,600,3),dtype=np.uint8)
imagen[:,:,:]=(25,25,25)
# Dibujando una linea
cv2.line(imagen,(0,0),(600,400),(255,0,0),4)

#Dibujando un Rectangulo
cv2.rectangle(imagen,(50,80),(200,200),(0,255,0),3)

#Dibujando un Circulo
cv2.circle(imagen,(300,200),100,(255,255,0),-1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen,'practicando con figuras con opencv',(10,30),font,1,(0,255,255),2,cv2.LINE_AA)



#cv2.imshow('BGR',bgr)
cv2.imshow('Figuras Geometricas Con NUMPY',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

