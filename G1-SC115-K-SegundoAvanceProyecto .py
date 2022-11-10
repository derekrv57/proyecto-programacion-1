#!/usr/bin/python3
usuario = ""
numReservacion = 0
adultonacional = 0
adultoextranjero = 0
otronacional = 0
otroextranjero = 0
horario = 0


def main():
    mnu = 0
    while mnu != 4:
        mnu = getvalormenu()
        if mnu == 1:
            reservas()
        elif mnu == 2:
            facturar()
        elif mnu == 4:
            if input("Está seguro que quiere salir s/n: ") != "s":
                mnu = 0
        else:
            input("Opción no valida.\nPresione enter para continuar...")


def getvalormenu():

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
    print("1.  8:00 am")
    print("2. 10:00 am")
    print("3. 12:00 md")
    print("4.  2:00 pm")
    global horario
    global adultonacional
    global adultoextranjero
    global otronacional
    global otroextranjero
    horario = int(input("Seleccione un horario: "))
    capaciad = 6
    adultonacional = int(input("Cántidad de adultos nacionales: "))
    capaciad -= adultonacional
    if capaciad > 0:
        adultoextranjero = int(input("Cántidad de adultos extranjeros: "))
        capaciad -= adultoextranjero
        if capaciad > 0:
            otronacional = int(
                input("Cántidad de adultos mayores / niños nacionales: "))
            capaciad -= otronacional
            if capaciad > 0:
                otroextranjero = int(
                    input("Cántidad de adultos mayores / niños extranjeros: "))
                capaciad -= otroextranjero
            else:
                print("No hay más espacios disponibles")
        else:
            print("No hay más espacios disponibles")
    else:
        print("No hay más espacios disponibles")


def facturar():
    reserva = int(input("Ingrese en numero de la reserva:"))
    nombre = input("Nombre del cliente: ")
    print("Total de la reservación #", numReservacion, ": ¢", adultonacional *
          5000+adultoextranjero*7000+otronacional*2500+otroextranjero*3500)


main()
