#!/usr/bin/python3
import os
import platform
usuario = ""
horario1 = [], []
horario2 = [], []
horario3 = [], []
horario4 = [], []
numReservacion = 0


def main():
    while True:
        mnu = getvalormenu()
        if mnu == 1:
            reservas()
        elif mnu == 2:
            facturacion()
        elif mnu == 3:
            informe()
        elif mnu == 4:
            if input("Está seguro que quiere salir s/n: ") == "s":
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
    return int(input("-> "))


def login():
    u = input("Usuario: ")
    c = input("Contraseña: ")
    limparpantalla()
    if u == "1" and c == "1234":
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
    print("1.  8:00 am")
    print("2. 10:00 am")
    print("3. 12:00 md")
    print("4.  2:00 pm")
    print("5.    Salir")
    horario = int(input("Seleccione un horario: "))
    if horario != 5:
        resp = -1
        while resp != 4:
            print("1. Adultos nacionales")
            print("2. Adultos extranjeros")
            print("3. Adultos mayores / niños nacionales")
            print("4. Salir")
            resp = int(input("-> "))
            if resp != 4:
                cant = int(input("Ingrese la cantudad: "))
                if horario == 1:
                    reservar(cant, resp, horario1)
                elif horario == 2:
                    reservar(cant, resp, horario2)
                if horario == 3:
                    reservar(cant, resp, horario3)
                elif horario == 4:
                    reservar(cant, resp, horario4)
        global numReservacion
        numReservacion += 1

def reservar(cant, tipo, horario):
    limparpantalla()
    tipo = int(tipo)
    if tipo > 0 and tipo < 5:
        disponibles = len(horario)
        if cant <= disponibles:
            for i in range(0, cant):
                horario.append(tipo, numReservacion)
    else:
        print("Opción no valida")

def facturacion():
    limparpantalla()


def informe():
    limparpantalla()


def limparpantalla():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == '__main__':
    main()
