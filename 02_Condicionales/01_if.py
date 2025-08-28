# ==================================================
# MANEJO DE FLUJO - CONDICIONALES IF
# ==================================================

# ==================================================
# EJEMPLO 1: Condicional Simple (if)
# ==================================================#


print("=" * 50)
print("EJEMPLO 1: Condicional Simple")
print("=" * 50)

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")  # Importante: Python usa indentación, no llaves
print("Felicidades")


# ==================================================
# EJEMPLO 2: Condicional con Else (if-else)
# ==================================================
print("\n" + "=" * 50)
print("EJEMPLO 2: Condicional con Else")
print("=" * 50)

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
print("Felicidades")


# ==================================================
# EJEMPLO 3: Condicionales Múltiples (if-elif-else)
# ==================================================
print("\n" + "=" * 50)
print("EJEMPLO 3: Sistema de Calificaciones")
print("=" * 50)

nota = int(input("Ingrese su nota (0-10): "))

if nota >= 9:
    print("Excelente ⭐⭐⭐")
elif nota >= 7:
    print("Bien ⭐⭐")
elif nota >= 5:
    print("Regular ⭐")
else:
    print("Reprobado ❌")


# ==================================================
# OPERADORES LÓGICOS
# ==================================================
print("\n" + "=" * 50)
print("OPERADORES LÓGICOS")
print("=" * 50)

# Operador AND
print("\n--- Operador AND ---")
edad = 25
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puedes conducir 🚗")
else:
    print("No puedes conducir 🚔")

# Operador OR
print("\n--- Operador OR ---")
es_estudiante = True
es_empleado = False

if es_estudiante or es_empleado:
    print("Tienes descuento en el transporte 🚌")
else:
    print("No tienes descuento")

# Operador NOT
print("\n--- Operador NOT ---")
llueve = False

if not llueve:
    print("Puedes salir sin paraguas ☀️")
else:
    print("Necesitas paraguas ☔")

# Combinación de operadores
print("\n--- Combinación de Operadores ---")
edad = 20
tiene_dinero = True
es_fin_de_semana = True

if (edad >= 18 and tiene_dinero) and (es_fin_de_semana or not llueve):
    print("Puedes ir a la fiesta 🎉")
else:
    print("Mejor quédate en casa 🏠")


# ==================================================

numero = 5
if numero : #true
    print("El numero es diferente de cero")

numero = 0
if numero : #false
    print("aqui no entraria nunca")

nombre = ""
if nombre : #false
    print("aqui no entraria nunca , el nombre no es valido")

numero = 5
es_el_5 = numero == 5
if es_el_5 : #false
    print("no entra")

print("Ternaria :")
#es if - else en una sola linea
# [codigo si cumple la condicion] if [condicion] else [codigo si no cumple la condicion]

edad = 20
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)

