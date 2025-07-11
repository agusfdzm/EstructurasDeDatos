# Enunciado:
# Dado un array de numeros 10, 20, 30:
#   1. Agrega un numero 40 al final
#   2. Elimina el ultimo elemento y guardalo en una variable
#   3. Comprueba si el array contiene el valor 20
#   4. Obten la longitud final del array

arrayej1 = [10, 20 ,30]

#   1. Agrega un numero 40 al final
arrayej1.append(40)
print(arrayej1)

#   2. Elimina el ultimo elemento y guardalo en una variable
elemento_eliminado = arrayej1.pop()
print(elemento_eliminado)
print(arrayej1)

#   3. Comprueba si el array contiene el valor 20

if 20 in arrayej1:
    print("Numero encontrado")
else:
    print("Numero no encontrado")

#   4. Obten la longitud final del array

print(len(arrayej1))