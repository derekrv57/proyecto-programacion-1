#!/usr/bin/python3
import os
import platform
usuario=""
def main():
    while True:
        mnu = getvalormenu()
        if  mnu == 1:
            reservas()
        elif mnu == 2:
            facturacion()
        elif mnu == 3:
            informe()
        elif mnu == 4:
            if input("Está seguro que quiere salir s/n: ")=="s":
                break
        else:
            input("Opción no valida.\nPresione enter para continuar...")

def getvalormenu():
    limparpantalla()
    if not logeado():
        login()
    print("1. Reservas")
    print("2. Facturacion")
    print("3. Informes")
    print("4. Salir")
    return int(input("->"))
    
def login():
    u = input("Usuario: ")
    c = input("Contraseña: ")
    limparpantalla()
    if u=="1" and c =="1234":
        print("Login exitoso")
        global usuario
        usuario = u
    else:
        print("Usuario y/o contraseña incorrectos...\n")
        login()

def logeado():
    return usuario != ""

def reservas():
    limparpantalla()

def facturacion():
    limparpantalla()

def informe():
    limparpantalla()

def limparpantalla():
    if platform.system()=="Windows":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == '__main__':
    main()