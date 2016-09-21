#!/usr/bin/env python
import socket #se importa la libreria socket 

s = socket.socket() # se crea un objeto tipo socket 
s.bind(("127.0.0.1",2015))# se crea un socket en la ip y puerto especificado
s.listen(5) # se llama la funcion escuchar del objeto socket
sc, addr = s.accept()# El método accept() nos devuelve una conexión abierta entre el servidor y el cliente
while True: #ciclo infinito
	recibido = sc.recv(1024)#se reciben los datos 
	print recibido.find("quit") #imprime  la busqueda en recibido cuando conicida con quit
	recibido = recibido [:-2] # a recibido se le restan dos bits para empezar a buscar en los datos recibidos  la palabra quit
	if (recibido == "quit"): #compara si en la cadena recibido esta la palabra quit
		print "salir por favor" # si esta la palabra quit imprime salir por favor 
		break # y sale

	print "llego:[",recibido,"]" # si no solo imprime que mensaje llego en vez de quit
	sc.send(recibido) # se regresa lo recibido

print "adios" # imprime adios
sc.close()#cierra  la conexion abierta entre el cliente y el servidor.
s.close() #cierra el socket creado al principio



