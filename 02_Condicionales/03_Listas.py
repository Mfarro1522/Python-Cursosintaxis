# LISTAS EN PYTHON
# Las listas son secuencias mutables (modificables) de elementos
# Pueden contener cualquier tipo de dato y son muy versátiles

# ==============================================
# 1. DEFINICIÓN DE LISTAS
# ==============================================
print("=== CREACIÓN DE LISTAS ===")

lista1 = [1, 2, 3, 4, 5]                    # Lista de enteros
lista2 = ["manzana", "banana", "cereza"]     # Lista de cadenas
lista3 = [1, "dos", 3.0, True]              # Lista mixta (diferentes tipos)

lista4 = []                                  # Lista vacía (método 1)
lista5 = list()                              # Lista vacía (método 2)

lista6 = [(1, 'calcetín'), (3, 4), (5, 6)]  # Lista de tuplas
matrix = [[1, 2], [4, 5], [7, 8]]           # Lista de listas (matriz)

print("Lista de enteros:", lista1)
print("Lista de cadenas:", lista2)
print("Lista mixta:", lista3)
print("Lista vacía:", lista4)
print("Otra lista vacía:", lista5)
print("Lista de tuplas:", lista6)
print("Matriz (lista de listas):", matrix)

# ==============================================
# 2. ACCESO A ELEMENTOS POR ÍNDICE
# ==============================================
print("\n=== ACCESO A ELEMENTOS ===")
print("lista2[0]:", lista2[0])    # "manzana" - Primer elemento (índice 0)
print("lista2[1]:", lista2[1])    # "banana"  - Segundo elemento
print("lista2[2]:", lista2[2])    # "cereza"  - Tercer elemento

# Índices negativos (desde el final)
print("lista2[-1]:", lista2[-1])  # "cereza"  - Último elemento
print("lista2[-2]:", lista2[-2])  # "banana"  - Penúltimo elemento
print("lista2[-3]:", lista2[-3])  # "manzana" - Antepenúltimo elemento

# Acceso a listas anidadas
print("lista6[0][1]:", lista6[0][1])  # 'calcetín' - Segundo elemento de la primera tupla

# ==============================================
# 3. SLICING (REBANADO) DE LISTAS
# ==============================================
print("\n=== SLICING O REBANADO ===")
lista1 = [1, 2, 3, 4, 5]

# Sintaxis: lista[inicio:fin] (fin no incluido)
print("lista1[1:4]:", lista1[1:4])   # [2, 3, 4] - Elementos del índice 1 al 3
print("lista1[:3]:", lista1[:3])     # [1, 2, 3] - Primeros 3 elementos
print("lista1[3:]:", lista1[3:])     # [4, 5]    - Desde el índice 3 hasta el final
print("lista1[:]:", lista1[:])       # [1, 2, 3, 4, 5] - Copia completa de la lista

# ==============================================
# 4. SLICING AVANZADO CON PASOS
# ==============================================
print("\n=== SLICING AVANZADO ===")
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sintaxis: lista[inicio:fin:paso]
print("lista1[::2]:", lista1[::2])   # [1, 3, 5, 7, 9] - De 2 en 2 (índices pares)
print("lista1[1::2]:", lista1[1::2]) # [2, 4, 6, 8, 10] - De 2 en 2 desde índice 1
print("lista1[::-1]:", lista1[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] - Lista invertida

# ==============================================
# 5. MODIFICACIÓN DE ELEMENTOS
# ==============================================
print("\n=== MODIFICACIÓN DE ELEMENTOS ===")
lista1[0] = 10  # Cambiar el primer elemento
print("Después de modificar lista1[0]:", lista1)

# ==============================================
# 6. AÑADIR ELEMENTOS A UNA LISTA
# ==============================================
print("\n=== AÑADIR ELEMENTOS ===")
lista1 = [1, 2, 3]
print("Lista original:", lista1)

# Método menos eficiente (crea nueva lista)
lista1 = lista1 + [4, 5, 6]
print("Después de + [4, 5, 6]:", lista1)

# Método más eficiente (modifica lista existente)
lista1 += [7, 8, 9]
print("Después de += [7, 8, 9]:", lista1)

# ==============================================
# 7. LONGITUD DE UNA LISTA
# ==============================================
print("\n=== LONGITUD DE LISTA ===")
print("Longitud de lista1:", len(lista1))

# ==============================================
# 8. EJEMPLOS PRÁCTICOS
# ==============================================
print("\n=== EJEMPLOS PRÁCTICOS ===")

# Verificar si un elemento está en la lista
frutas = ["manzana", "banana", "cereza"]
print("'banana' en frutas:", "banana" in frutas)        # True
print("'uva' en frutas:", "uva" in frutas)              # False

# Obtener índice de un elemento
print("Índice de 'banana':", frutas.index("banana"))    # 1

# Contar ocurrencias
numeros = [1, 2, 2, 3, 2, 4]
print("Veces que aparece 2:", numeros.count(2))         # 3

# ==============================================
# 9. range() PARA GENERAR LISTAS DE NÚMEROS
# ==============================================
print("\n=== USO DE range() ===")
# range(inicio, fin, paso) genera una secuencia de números
nums = range(5) #no genera una lista, genera un objeto range
print(type(nums))  # <class 'range'>
print(type([1, 2, 3]))  # <class 'list'>
# para convertir a lista usamos list()
print(list(nums))  # [0, 1, 2, 3, 4]


# typos de range
#range(fin) - empieza en 0, termina en fin-1, paso 1
print(list(range(5)))  # [0, 1, 2, 3, 4]
#range(inicio, fin) - empieza en inicio, termina en fin-1, paso 1
print(list(range(2, 5)))  # [2, 3, 4]
#range(inicio, fin, paso) - empieza en inicio, termina en fin-1, paso definido
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]

#range es muy optimo para usar en bucles for y valores grandes 
#ademas para hacer alguna accion 5 veces mejora mucho la sintaxis

# Ejemplo básico de un bucle for
for _ in range(5):  #convencion usar _ cuando no se usa la variable
    print(f"Iteración {_}")

for i in range(5): #usar i cuando se usa la variable 
    print(f"Iteración {i}")

#en ejemplos pequeños no se nota pero en programas grandes si