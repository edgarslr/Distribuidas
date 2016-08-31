import socket
import time
s = socket.socket()
s.bind(("localhost",2001))
s.listen(1)
sc, addr = s.accept()
while True:
	recibido = sc.recv(1024)
	print recibido.find("quit")
	recibido = recibido [:-2]
	if (recibido =="quit"):
		print "salir por favor"
		break
	elif (recibido =="uname"):
		print "Mini 13.01"
	elif (recibido =="time"):
		print time.strftime("%I:%M:%S")
	elif (recibido =="help"):
		print "uname: sistema"
		print "quit: salir"
		print "services: servicios"
		print "login: entrar"
		print "logout: salir"
	elif (recibido =="services"):
		print "apache"
		print "MysSQL"
	elif (recibido =="uname -m"):
		print "x86_64"
	elif (recibido =="uname -a"):
		print "faaoksdfknasdfasdlfkasdf"
		print "faaoksdfknasdfasdlfkasdf"
		print "faaoksdfknasdfasdlfkasdf"
	elif (recibido =="ls"):
		print "README.txt"
	elif (recibido =="login"):
		print "Welcome"
	elif (recibido =="logout"):
		print "goodbye"
	sc.send(recibido)
print "adios"
sc.close()
s.close()