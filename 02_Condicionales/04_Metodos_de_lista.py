import os

# Metodos de listas
#Cuando se accede por un . es que es un metodo o atributo de un objeto
#las listas tienen muchos metodos que se pueden usar para manipularlas
lista1 = ['a', 'b', 'c']

#metodo append : añade un elemento al final de la lista
lista1.append('d')
print(lista1) 

#insert : añade un elemento en una posicion especifica
lista1.insert(1, '@') 
print(lista1) 

#extend : añade varios elementos al final de la lista
lista1.extend('e')
#lista1.extend('😍','😍') #mal cuando quieres agregar varios
lista1.extend(['😍','😛'])
print(lista1)

#remove : elimina la primera aparicion de un elemento

lista1.remove('@') #no se pasa indice si no el elemento que quieres eliminar
print(lista1)

#pop : elimina un elemento en un indice especifico y lo devuelve
ultimo = lista1.pop() #elimina el ultimo elemento
print(ultimo)
print(lista1)

lista1.pop(0) #elimina el primer elemento
print(lista1)
lista1.pop(-1) #elimina el ultimo elemento , se puede usar indice negativo
lista1.pop(1) #elimina el elemento en la posicion 1

# tambien se puede eliminar un elemento por su indice con del
del lista1[0] #elimina el primer elemento
print(lista1)

#clear : elimina todos los elementos de la lista
lista1.clear()
print(lista1)

#eliminar un rango de elementos con slicing
lista1 = ['🐵', '🐶', '🐱', '🦊', '🐻', '🐰']
print(lista1)

del lista1[1:4] #elimina al perro , gato y zorro
print(lista1)

#mas metodos utiles
#ordenasr una lista con sort
print('Ordenar una lista con sort modificando la original:')
numeros = [5, 2, 9, 1, 5, 6]
print(numeros)
numeros.sort()
print(numeros) # [1, 2, 5, 5, 6, 9]

print('Ordenar una lista creando una nueva con sorted:')
numeros = [5, 2, 9, 1, 5, 6]
print(numeros)
ordenados = sorted(numeros)
print(ordenados) # [1, 2, 5, 5, 6, 9]
print(numeros) # [5, 2, 9, 1, 5, 6] 

#tambien se puede con cadenas de texto
frutas = ['manzana', 'naranja', 'banana', 'kiwi']
print(frutas)
frutas.sort()
print(frutas) # ['banana', 'kiwi', 'manzana', 'naranja']
# si por lo que sea hay mayusculas y minusculas
frutas = ['manzana', 'Naranja', 'banana', 'kiwi']
print(frutas)
frutas.sort()
print(frutas) # ['Naranja', 'banana', 'kiwi', 'manzana'] las mayusculas van primero
#para evitar eso se puede usar key=str.lower para que todas las compare en minusculas

frutas.sort(key=str.lower) #le damos la funcion str.lower para que compare en minusculas

print(frutas) # ['banana', 'kiwi', 'manzana', 'Naranja']

#mas cositas utiles

lista1 = ['🐵', '🐶', '🐶', '🦊', '🐻', '🐰']
print(len(lista1)) #len : devuelve la longitud de la lista
print(lista1.count('🐶')) #count : cuenta cuantas veces aparece un elemento en la lista
print(lista1.index('🦊')) #index : devuelve el indice de la primera aparicion de un elemento en la lista
#si el elemento no existe da error
#print(lista1.index('🐸')) #ValueError: '🐸' is not in list

print('🐶' in lista1) #in : devuelve True si el elemento existe en la lista , False si no
print('🐸' in lista1) # false


