import os
import time
import hashlib
BLUE    = '\033[34m'
GREEN   = '\033[32m'
MAGENTA = '\033[35m'
from tqdm import tqdm
data = []
content = 0
f = open('dato.txt', 'r')
content = f.read()
def signup():
    dni = input("ingrese su dni: ")
    pwd = input("ingrese su contraseña: ")
    conf_pwd= input("confirme su contraseña: ")
    os.system("cls")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5 (enc).hexdigest()
    with open("credentials.txt" , "w") as f:
        f.write(dni + "\n")
        f.write(hash1)
    f.close()
    print("Su registro fue exitoso")
    time.sleep(.5)
    os.system("cls")

def login():
    dni = input("ingrese su dni: ")
    pwd = input("ingrese su contraseña: ")
    auth= pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt" , "r") as f:
        stored_dni , stored_pwd = f.read().split("\n")
    f.close()

    if dni == stored_dni and auth_hash == stored_pwd:
        print("login existoso")
    print(MAGENTA + content)
    print(GREEN + "Espere un momento....")
    time.sleep(5.0)
    os.system("cls")
    while True:
        print(GREEN + f"----------------Escoga el curso para ver su horario-------------\n\
matematicas\n\
comunicacion\n\
ciencias\n\
ingles\n\
personal_social\n\
Educacion_Fisica\n\
Educacion_para_el_Trabajo\n\
Arte\n\
religion\n\
Tutoria\n\
--------------------------------------------------------------------------------\n\
presione h para salir:")
        opcion=input(("ingrese su opcion "))
        if opcion=='matematicas':
            print(MAGENTA + f"---------su horario son de lunes y miercoles de 08:00 AM a 10:30 AM---------")
            pbar = tqdm(range(100))
            Rojo = '\033[31m'

            for i in pbar:
                data.append(i)
                time.sleep(.10)
                pbar.set_description(Rojo + "Descargando Archivo...")

            Verde = '\033[32m'
            print(Verde + "------------Archivo descargado------------")
            break
        if opcion=='comunicacion':
            print(MAGENTA + f"---------su horario son de martes y jueves de 08:00 AM a 10:30 AM---------")
            pbar = tqdm(range(100))
            Rojo = '\033[31m'

            for i in pbar:
                data.append(i)
                time.sleep(.10)
                pbar.set_description(Rojo + "Descargando Archivo...")

            Verde = '\033[32m'
            print(Verde + "------------Archivo descargado------------")
            break
        if opcion=='ciencias':
            print(MAGENTA + f"---------su horario son de lunes y miercoles de 11:00 AM a 12:30 PM---------")
            pbar = tqdm(range(100))
            Rojo = '\033[31m'

            for i in pbar:
                data.append(i)
                time.sleep(.10)
                pbar.set_description(Rojo + "Descargando Archivo...")

            Verde = '\033[32m'
            print(Verde + "------------Archivo descargado------------")
            break
        if opcion=='ingles':
            print(MAGENTA + f"---------su horario son los viernes de 08:00 AM a 10:30 AM---------")
            pbar = tqdm(range(100))
            Rojo = '\033[31m'

            for i in pbar:
                data.append(i)
                time.sleep(.10)
                pbar.set_description(Rojo + "Descargando Archivo...")

            Verde = '\033[32m'
            print(Verde + "------------Archivo descargado------------")
            break
        if opcion == 'Educacion_Fisica':
            print(MAGENTA + f"---------su horario son los viernes de 11:00 AM a 12:00 PM---------")
            pbar = tqdm(range(100))
            Rojo = '\033[31m'

            for i in pbar:
                data.append(i)
                time.sleep(.10)
                pbar.set_description(Rojo + "Descargando Archivo...")

            Verde = '\033[32m'
            print(Verde + "------------Archivo descargado------------")
            break
        if opcion == 'Educacion_para_el_Trabajo':
            print(MAGENTA + f"---------su horario son los martes  de 11:00 AM a 12:00 PM---------")
            pbar = tqdm(range(100))
            Rojo = '\033[31m'

            for i in pbar:
                data.append(i)
                time.sleep(.10)
                pbar.set_description(Rojo + "Descargando Archivo...")

            Verde = '\033[32m'
            print(Verde + "------------Archivo descargado------------")
            break
        if opcion == 'Arte':
            print(MAGENTA + f"---------su horario son los jueves de 11:00 AM a 12:00 PM---------")
            pbar = tqdm(range(100))
            Rojo = '\033[31m'

            for i in pbar:
                data.append(i)
                time.sleep(.10)
                pbar.set_description(Rojo + "Descargando Archivo...")

            Verde = '\033[32m'
            print(Verde + "------------Archivo descargado------------")
            break
        os.system('cls')
        if opcion == 'religion':
            print(MAGENTA + f"---------su horario son de lunes  de 07:00 AM a 7:30 AM---------")
            break
        if opcion == 'Tutoria':
            print(MAGENTA + f"---------su horario son de martes de 12:30 PM a 2:00 PM---------")
            pbar = tqdm(range(100))
            Rojo = '\033[31m'

            for i in pbar:
                data.append(i)
                time.sleep(.10)
                pbar.set_description(Rojo + "Descargando Archivo...")

            Verde = '\033[32m'
            print(Verde + "------------Archivo descargado------------")
            break
        if opcion=='h':
    
            break



def menu():
    os.system('cls')
    while 1:
        print(BLUE + "********** Aprendo en casa **********")
        print("1.Registrar")
        print("2.Login")
        print("3.Salir")
        ch = int(input("Escoga una opcion: "))
        os.system('cls')
        if ch == 1:
            signup()
        elif ch == 2:
            login()
        elif ch == 3:
            break
        else:
            print("Opcion Incorrecta!")   
menu() 


