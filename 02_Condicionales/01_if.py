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


# ==============================================
# VALORES TRUTHY Y FALSY EN PYTHON
# ==============================================
print("\n" + "=" * 50)
print("VALORES TRUTHY Y FALSY")
print("=" * 50)

# En Python, algunos valores se evalúan como True o False automáticamente
numero = 5
if numero:  # True - cualquier número diferente de 0 es True
    print("El número es diferente de cero")

numero = 0
if numero:  # False - solo el 0 es False
    print("Aquí no entraría nunca")
else:
    print("El número es cero (Falsy)")

nombre = ""
if nombre:  # False - string vacío es False
    print("Aquí no entraría nunca, el nombre no es válido")
else:
    print("El nombre está vacío (Falsy)")

# Ejemplo con variable booleana
numero = 5
es_el_5 = numero == 5  # True
if es_el_5:
    print("¡Sí es el número 5!")

# ==============================================
# OPERADOR TERNARIO (IF-ELSE EN UNA LÍNEA)
# ==============================================
print("\n" + "=" * 50)
print("OPERADOR TERNARIO")
print("=" * 50)

# Sintaxis: [valor_si_true] if [condición] else [valor_si_false]
edad = 20
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)

# Más ejemplos de operador ternario
temperatura = 25
clima = "Caluroso" if temperatura > 30 else "Templado" if temperatura > 15 else "Frío"
print(f"El clima está: {clima}")

# ==============================================
# RESUMEN DE VALORES FALSY EN PYTHON
# ==============================================
"""
VALORES FALSY (se evalúan como False):
- False
- 0, 0.0, 0j (números cero)
- "", '', "" "" (strings vacíos)
- [], (), {} (listas, tuplas, diccionarios vacíos)
- None
- set() (conjunto vacío)

TODOS LOS DEMÁS VALORES SON TRUTHY (se evalúan como True)
"""

