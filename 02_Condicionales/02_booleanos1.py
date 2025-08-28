# VALORES BOOLEANOS Y OPERADORES LÓGICOS
# Los booleanos son un tipo de dato que solo puede tener dos valores: True o False

# ==============================================
# 1. VALORES BOOLEANOS BÁSICOS
# ==============================================
print("=== VALORES BOOLEANOS BÁSICOS ===")
print(True)   # Valor verdadero
print(False)  # Valor falso

# ==============================================
# 2. OPERADORES DE COMPARACIÓN
# ==============================================
print("\n=== OPERADORES DE COMPARACIÓN ===")
print("5 > 3:", 5 > 3)      # True - Mayor que
print("5 < 3:", 5 < 3)      # False - Menor que
print("5 >= 3:", 5 >= 3)    # True - Mayor o igual que
print("5 <= 3:", 5 <= 3)    # False - Menor o igual que
print("5 == 3:", 5 == 3)    # False - Igual que
print("5 != 3:", 5 != 3)    # True - Distinto que

# ==============================================
# 3. COMPARACIÓN DE CADENAS
# ==============================================
print("\n=== COMPARACIÓN DE CADENAS ===")
print("'Manzana' < 'Pera':", "Manzana" < "Pera")  # True - Se comparan lexicográficamente (orden alfabético)
print("'Hola' == 'hola':", 'Hola' == 'hola')      # False - Las cadenas son case-sensitive (distinguen mayúsculas)
print("'abc' < 'abd':", 'abc' < 'abd')             # True - Comparación carácter por carácter

# ==============================================
# 4. OPERADORES LÓGICOS
# ==============================================
print("\n=== OPERADORES LÓGICOS ===")

# AND: Ambas condiciones deben ser True para que el resultado sea True
print("True and False:", True and False)   # False

# OR: Al menos una condición debe ser True para que el resultado sea True
print("True or False:", True or False)     # True

# NOT: Invierte el valor booleano
print("not True:", not True)               # False
print("not False:", not False)             # True

# ==============================================
# 5. TABLAS DE VERDAD
# ==============================================
# Estas tablas muestran todos los posibles resultados de los operadores lógicos

print("\n=== TABLA DE VERDAD AND ===")
print("A       B       A and B")
print("True    True   ", True and True)     # True
print("True    False  ", True and False)    # False
print("False   True   ", False and True)    # False
print("False   False  ", False and False)   # False

print("\n=== TABLA DE VERDAD OR ===")
print("A       B       A or B")
print("True    True   ", True or True)      # True
print("True    False  ", True or False)     # True
print("False   True   ", False or True)     # True
print("False   False  ", False or False)    # False

print("\n=== TABLA DE VERDAD NOT ===")
print("A       not A")
print("True   ", not True)                  # False
print("False  ", not False)                 # True

# ==============================================
# 6. EJEMPLOS PRÁCTICOS
# ==============================================
print("\n=== EJEMPLOS PRÁCTICOS ===")

edad = 20
tiene_licencia = True
es_fin_de_semana = False

# Combinando operadores
puede_conducir = edad >= 18 and tiene_licencia
print(f"¿Puede conducir? {puede_conducir}")

# Usando paréntesis para claridad
puede_salir = (edad >= 18) and (es_fin_de_semana or not tiene_licencia)
print(f"¿Puede salir? {puede_salir}")

# ==============================================
# 7. PRECEDENCIA DE OPERADORES
# ==============================================
"""
ORDEN DE PRECEDENCIA (de mayor a menor):
1. Paréntesis ()
2. not
3. and
4. or

Ejemplo: True or False and False
Se evalúa como: True or (False and False) = True or False = True

Para mayor claridad, siempre usa paréntesis: (True or False) and False = False
"""
