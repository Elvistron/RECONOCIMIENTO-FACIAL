import cv2
import numpy as np
import os


direccionImagenes = "Imagenes"
listaImagenes = os.listdir(direccionImagenes)
print("Lista de Imagenes",listaImagenes)

if not os.path.exists('Rostros encontrados'):
	print ('Carpeta encontrada: Rostros encontrados')
	os.makedirs('Rostros encontrados')

clasificadorRostros = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

contador = 0

for imagenNombre in listaImagenes:
	#print('Nombre de Imagenes',imagenNombre)
	imagen = cv2.imread(direccionImagenes+'/'+imagenNombre)
	imagenAux = imagen.copy()
	# convertimos las imagenes en escala de grises 
	gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
	rostros = clasificadorRostros.detectMultiScale(gray, 1.09, 5)

	#creamos un rectangulo al rededor del rostro

	for (x,y,w,h) in rostros:
		cv2.rectangle(imagen,(x,y),(x+w,y+h),(128,0,255),2)
		cv2.imshow('Imagenes', imagen)
		cv2.waitKey(0)


cv2.destroyAllWindows()