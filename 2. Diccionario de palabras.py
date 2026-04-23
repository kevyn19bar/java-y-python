dict ={}

oracion= input("Escribe algo: ")

oracion= oracion.lower()

palabras= oracion.split()

for palabra in palabras:
    if palabra in dict:
        dict[palabra] += 1
    else:
        dict[palabra] = 1

print("\nConteo de palabras:")
for palabra, cantidad in dict.items():
    print(palabra, ":", cantidad) 