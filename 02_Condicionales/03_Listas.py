# Listas : secuencias mutables de elementos

print("Listas en Python:")
# Definicion de una listas

lista1 = [1, 2, 3, 4, 5] # lista de enteros
lista2 = ["manzana", "banana", "cereza"] # lista de cadenas
lista3 = [1, "dos", 3.0, True] # lista mixta

lista4 = [] # lista vacia
lista5 = list() # otra forma de crear una lista vacia

lista6 = [(1, 'calcetin'), (3, 4), (5, 6)] # lista de listas o matrices
matrix = [[1, 2], [4, 5], [7, 8]]

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)
print( lista6)
print( matrix)

#Aceseso a elementos de una lista por indice
print("Acceso a elementos de una lista:")
print(lista2[0]) #manazana
print(lista2[1]) #banana
print(lista2[2]) #cereza
print(lista2[-1]) #cereza
print(lista2[-2]) #banana
print(lista2[-3]) #manzana

#Acesso a lista de listas
print("Acceso a elementos de una lista de listas:")
print(lista6[0][1]) #2

#Slicing o rebanado de listas
lista1 = [1, 2, 3, 4, 5]
#quiero tomar los elementos del indice 1 al 5
print("Slicing o rebanado de listas:")
print(lista1[1:4]) # [2, 3, 4] 
#quiero los 3 primeros numeros
print(lista1[:3]) # [1, 2, 3]
#quiero los 2 ultimos numeros
print(lista1[3:]) # [4, 5]

#quiero una compia de la lista
print(lista1[:]) # [1, 2, 3, 4, 5]



#hay mas magia en hacer slicing
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# froma normal print(lista1[desde:hasta])
# con pasos print(lista1[desde:hasta:pasos])
#ejemplo 

print(lista1[::2]) # [1, 3, 5, 7, 9] de 2 en 2 o devolver indices pares 
print(lista1[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] invierte la lista

#modificar elementos de una lista

lista1[0] = 10
print(lista1) # [10, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#añadir elementos a una lista
lista1 = [1, 2, 3]
print(lista1)
#larga y menos eficiente
lista1 = lista1 + [4,5,6] #automaticamente concatena 
print(lista1)
#corta y eficiente
lista1 += [7,8,9] #automaticamente concatena
print(lista1)

#recuperar longitud de una lista
print("Longitud de la lista1:", len(lista1)) # 9

