def menu():
    print("-----Menú-----")
    print("1. Ver tienda")
    print("2. Ver factura")
    print("3. Pagar")
    print("4. Salir")
    return int(input("Elige una opción: "))

def tienda(papa, pollo, arroz, frijol):
    carrito = 0
    k1 = k2 = k3 = k4 = 0
    p1 = p2 = p3 = p4 = 0
    print("====Productos====")
    print("1k-papa--------3k")
    print("1k-pollo-------9k")
    print("1k-arroz-------4k")
    print("1k-frijol------6k")
    print("=================")
    while True:
        respuesta = input("¿Quieres agregar al carrito? (si/no): ").lower()
        if respuesta in ["si", "s"]:
            producto = input("¿Qué te gustaría llevar?: ").lower()
            match producto:
                case "papa":
                    k1 = float(input("¿Cuántos kilos quieres llevar? (solo número, medio es 0.5): \n"))
                    p1 = papa * k1
                    carrito += p1
                case "pollo":
                    k2 = float(input("¿Cuántos kilos quieres llevar? (solo número, medio es 0.5): \n"))
                    p2 = pollo * k2
                    carrito += p2
                case "arroz":
                    k3 = float(input("¿Cuántos kilos quieres llevar? (solo número, medio es 0.5): \n"))
                    p3 = arroz * k3
                    carrito += p3
                case "frijol":
                    k4 = float(input("¿Cuántos kilos quieres llevar? (solo número, medio es 0.5): \n"))
                    p4 = frijol * k4
                    carrito += p4
                case _:    
                    print("Producto no encontrado.")
        else:
            break
            
    return carrito, p1, p2, p3, p4, k1, k2, k3, k4


def factura(costo, K1, K2, K3, K4, P1, P2, P3, P4):
    print("*" * 20)
    print("Cajero Automático")
    print("Producto.........Precio")
    if K1 > 0: print(f"{K1}K--papa........${P1}")
    if K2 > 0: print(f"{K2}K--pollo.......${P2}")
    if K3 > 0: print(f"{K3}K--arroz.......${P3}")
    if K4 > 0: print(f"{K4}K--frijol......${P4}")
    print("*" * 20)
    print("*" * 20)
    print(f"Total-----------${costo}")
    print("*" * 20)

papa = 3000
pollo = 9000
arroz = 4000
frijol = 6000

carrito = p1 = p2 = p3 = p4 = k1 = k2 = k3 = k4 = 0

while True:
    match menu():
        case 1:
            carrito, p1, p2, p3, p4, k1, k2, k3, k4 = tienda(papa, pollo, arroz, frijol)
        case 2:
            factura(carrito, k1, k2, k3, k4, p1, p2, p3, p4)
        case 3:
            print("Pago Exitoso. ¡Gracias por su compra!")
            carrito = p1 = p2 = p3 = p4 = k1 = k2 = k3 = k4 = 0
        case 4:
            print("Saliendo del sistema...")
            break
        case _:
            print("Opción inválida")
            print("Vuelva a intentar")