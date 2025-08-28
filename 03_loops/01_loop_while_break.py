# Ejemplo de bucle while en Python

# El bucle while repite un bloque de código mientras una condición sea verdadera.

contador = 0

while contador < 5:
    print(contador)
    contador +=1


print()
# break rompe el bucle cuando se cumple una condición específica.
contador = 0
while True:
    print(contador)
    contador += 1
    if contador == 5:
        break

#continue salta a la siguiente iteración del bucle.
print()
contador = 0

while contador < 10:
    contador += 1   
    if contador % 2 == 0:
        continue # salta a la linea 25 evitando lo de abajo
    print(contador)
