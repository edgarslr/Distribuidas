file = open("prueba.vocales", "r")
file_write=open("texto.txt","a")
vocales = ('a', 'e', 'i', 'o', 'u')
contenido = file.read()
for letra in vocales:
	contenido = contenido.replace(letra,'')
print contenido
file_write.write(contenido)
file.close()