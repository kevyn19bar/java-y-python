lista = []

def menu():
    print("Agregar Variables a una lista")
    print("1. Agregar variable")
    print("2. Salir")

def add_variable():
    variable = input("Ingrese una variable: ")
    if variable not in lista:
        lista.append(variable)
    else:
        print("La variable ya existe en la lista")

while True:
    menu()
    op = input("Ingrese una opción: ")

    match op:
        case "1":
            add_variable()
        case "2":
            print("Saliendo...")
            break
        case _:
            print("Esta opción no está disponible")