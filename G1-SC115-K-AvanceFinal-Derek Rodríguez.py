#!/usr/bin/python
import os
import platform
usuario = ""
reservaciones = []
disponibles = [6] * 4
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
    login = False
    while not login:
        u = input("Usuario: ")
        c = input("Contraseña: ")
        limparpantalla()
        login = u == "1" and c == "1234"
        if login:
            print("Login exitoso")
            global usuario
            usuario = u
        else:
            print("Usuario y/o contraseña incorrectos...\n")


def logeado():
    return usuario != ""


def guardarTxt(dir, cont, modo):
    file = open(dir, modo)
    file.write(cont)
    file.close()


def generarTxt(dir, cont):
    guardarTxt(dir, cont, "w")


def actualizarTxt(dir, cont):
    guardarTxt(dir, cont, "a")


def reservas():
    limparpantalla()
    print("1. 8:00 am")
    print("2. 10:00 am")
    print("3. 12:00 md")
    print("4. 2:00 pm")
    print("5. Salir")
    horario = int(input("Seleccione un horario: "))
    while horario > 0 and horario < 6:
        if horario != 5:
            horario -= 1
            resp = -1
            campos = [0] * 6
            while resp != 5:
                print("1. Adultos nacionales")
                print("2. Adultos extranjeros")
                print("3. Adultos mayores ")
                print("4. Niños nacionales")
                print("5. Salir")
                global disponibles
                resp = int(input("-> "))
                if resp > 0 and resp < 5 and disponibles[horario] > 0:
                    cant = int(input("Ingrese la cantidad: "))
                    limparpantalla()
                    if disponibles[horario] >= cant:
                        campos[0] = horario
                        campos[resp] = cant
                        disponibles[horario] -= cant
                    else:
                        print("No hay suficientes espacios")
            print("Reservación #", numReservacion)
            if input("Guardar? s/n: ") == "s":
                reservar(campos)


def reservar(horario):
    global reservaciones
    reservaciones.append(horario)
    global numReservacion
    numReservacion += 1


def facturacion():
    limparpantalla()
    numRes = int(input("Número de reserva: "))
    horarios = ["8:00 am", "10:00 am", "12:00 md", "2:00 pm"]
    an = reservaciones[numRes][1] * 5000
    ae = reservaciones[numRes][2] * 7000
    am = reservaciones[numRes][3] * 2500
    nn = reservaciones[numRes][4] * 3500
    total = an + ae + am + nn
    factura = "Horario:" + str(horarios[reservaciones[numRes][0]]) + "\n" + "Adultos nacionales:" + str(an) + "\n" + "Adultos extranjeros:" + str(
        ae) + "\n" + "Adultos mayores:" + str(am) + "\n" + "Niños nacionales:" + str(nn) + "\n" + "Total:" + str(total)
    print(factura)
    if input("Facturar? s/n: ") == "s":
        limparpantalla()
        cedula = input("Cedula: ")
        reservaciones[numRes][5] = 1
        factura = "Aventuras “El paraíso”\n\nCedula: " + \
            cedula + "\nReserva #: " + str(numRes) + "\n" + factura
        print(factura)
        if input("Guardar como archivo de texto? s/n: ") == "s":
            nombre = input("Guardar como: [" + cedula + ".txt]: ") + ".txt"
            if nombre == ".txt":
                nombre = cedula + ".txt"
            generarTxt(nombre, factura)


def informe():
    horarios = ["8:00 am", "10:00 am", "12:00 md", "2:00 pm"]
    tipos = ["Adultos nacionales:", "Adultos extranjeros:",
             "Adultos mayores:", "Niños nacionales:"]

    def sumar(horario):
        print(horarios[horario])
        sum = 0
        nacionales = 0
        extranjeros = 0
        for j in range(numReservacion):
            if reservaciones[j][0] == horario:
                for i in range(1, 5):
                    print(tipos[i-1], reservaciones[j][i])
                    sum += reservaciones[j][i]
            nacionales += reservaciones[j][1]*5000 + reservaciones[j][3]*2500
            extranjeros = reservaciones[j][2]*7000 + reservaciones[j][4]*3500
        print("Personas que viajaron:", str(sum))
        print("Generado por nacionales:", str(nacionales))
        print("Generado por extranjeros:", str(extranjeros))
        return sum
    limparpantalla()
    datos = []
    for i in range(numReservacion):
        datos.append(sumar(i))
    mayor = 0
    menor = 0
    for i in range(1, numReservacion):
        if datos[i] > datos[mayor]:
            mayor = i
        if datos[i] < datos[menor]:
            menor = i
    print("----------------------")
    print("Mayor:", horarios[mayor], datos[mayor])
    print("Menor:", horarios[menor], datos[menor])
    input("Enter para continuar... ")


def limparpantalla():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


main()
