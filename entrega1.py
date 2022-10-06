#!/usr/bin/python3
u = input("Usuario: ")
c = input("Contraseña: ")
if u == "1" and c == "1234":
    print("Login exitoso")
    global usuario
    usuario = u
    # Reservas
    numreservacion = 0
    print("1.  8:00 am")
    print("2. 10:00 am")
    print("3. 12:00 md")
    print("4.  2:00 pm")
    horario = int(input("Seleccione un horario: "))
    capaciad = 6
    adultonacional = int(input("Cántidad de adultos nacionales: "))
    adultoextranjero = 0
    otronacional = 0
    otroextranjero = 0
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
    print("Total de la reservación #",numreservacion,": ¢", adultonacional*5000+adultoextranjero*7000+otronacional*2500+otroextranjero*3500)
else:
    print("Usuario y/o contraseña incorrectos...\n")
