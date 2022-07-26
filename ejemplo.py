import face_recognition

#Cargue los archivos jpg en matrices numpy
obama_image = face_recognition.load_image_file("Barack Obama.jpg")
justin_image = face_recognition.load_image_file("Justin Timberlake.jpg")
ryan_image = face_recognition.load_image_file("Ryan Reynolds.jpg")
unknown_image = face_recognition.load_image_file("unknown_celebrity.jpg")

# Obtenga las codificaciones de caras para cada cara en cada archivo de imagen
# Dado que podría haber más de una cara en cada imagen, devuelve una lista de codificaciones.
# Pero como sé que cada imagen solo tiene una cara, solo me importa la primera codificación en cada imagen, así que tomo el índice 0.
try:
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    justin_face_encoding = face_recognition.face_encodings(justin_image)[0]
    ryan_face_encoding = face_recognition.face_encodings(ryan_image)[0]
    
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError:
    print("No pude localizar ningún rostro en al menos una de las imágenes. Verifique los archivos de imagen. Abortando ...")
    quit()

known_faces = [
    obama_face_encoding,
    justin_face_encoding,
    ryan_face_encoding
]

# Los resultados son una matriz de Verdadero / Falso que indica si la cara desconocida coincide con alguien en la matriz de caras conocidas.
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

print("Is the unknown face a picture of Obama? {}".format(results[0]))
print("Is the unknown face a picture of Justin? {}".format(results[1]))
print("Is the unknown face a picture of Ryan? {}".format(results[2]))
print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))