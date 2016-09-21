#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket#se importa la libreria socket 

s=socket.socket() # se crea un objeto tipo socket y se le asigna el nombre "s"
s.connect(("127.0.0.1",2001)) #se llama la funcion "connect" de el objeto socket y se conecta a la ip y el puerto asignado

while True:# se crea un siclo infinito
	mensaje = raw_input(">") # mensaje sera igual a lo recibido por el teclado
	s.send(mensaje)# enviara el mensaje al socket
	if (mensaje == "quit"): # compara si el mensaje es igual a quit se sale del siclo
		break
print "adios" #imprime adios y sale

s.close() #cierra la conexion con el socket