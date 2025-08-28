# ENTRADA DE DATOS CON INPUT()
# La función input() permite recibir datos del usuario desde la consola

# ==============================================
# 1. INPUT BÁSICO
# ==============================================
print("¿Hola, cómo te llamas?")
nombre = input()  # Espera que el usuario escriba algo y presione Enter

print(f"¡Hola {nombre}, encantado de conocerte!")

# ==============================================
# 2. INPUT CON MENSAJE PERSONALIZADO
# ==============================================
# Es más común incluir el mensaje directamente en input()
nombre = input("Hola, ¿cómo te llamas?\n")
print(f"¡Hola {nombre}, encantado de conocerte!")

# ==============================================
# 3. IMPORTANTE: INPUT SIEMPRE DEVUELVE STRING
# ==============================================
age = input("¿Cuántos años tienes?\n")

# TODO lo que se introduce por input() es un STRING
print(f"Tienes {age} años")
print(type(age))  # <class 'str'> - Siempre es string

# Para usar como número, hay que convertir el tipo de dato
age = int(age)    # Convertimos string a entero
print(f"Tienes {age} años")
print(type(age))  # <class 'int'> - Ahora es entero

# ==============================================
# 4. OBTENER MÚLTIPLES VALORES
# ==============================================
print("--- Obtener múltiples valores a la vez ---")

# Usando split() para separar la entrada por espacios
country, city = input("¿En qué país y ciudad vives? (separados por espacio)\n").split()
print(f"Vives en {city}, {country}")

# ==============================================
# 5. EJEMPLOS ADICIONALES CON SPLIT()
# ==============================================
print("\n--- Ejemplos con diferentes separadores ---")

# Separar por comas
# datos = input("Escribe tu nombre, edad y ciudad (separados por comas):\n").split(',')
# nombre, edad, ciudad = datos
# print(f"Nombre: {nombre.strip()}, Edad: {edad.strip()}, Ciudad: {ciudad.strip()}")

# ==============================================
# 6. CONSEJOS DE BUENAS PRÁCTICAS
# ==============================================
"""
CONSEJOS:
1. Siempre validar y convertir la entrada si es necesario
2. Usar mensajes claros que expliquen qué formato esperas
3. Considerar usar try/except para manejar errores de conversión
4. Recordar que input() pausa la ejecución hasta que el usuario responda

EJEMPLO DE VALIDACIÓN:
try:
    edad = int(input("Ingresa tu edad: "))
    print(f"Tienes {edad} años")
except ValueError:
    print("Error: Debes ingresar un número válido")
"""





