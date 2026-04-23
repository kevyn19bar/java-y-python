def fibonacci():
    numero1 = 1
    numero2 = 1
    print(numero1)
    print(numero2)
    while True:
        temporal = numero2
        numero2 = numero1 + numero2
        numero1 = temporal
        print (numero2)
        if numero2 == 34:
            break

fibonacci()