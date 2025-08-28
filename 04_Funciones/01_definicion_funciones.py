# ========================================
# DEFINICIÓN Y LLAMADA DE FUNCIONES EN PYTHON
# ========================================

# ¿Qué es una función?
# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Las funciones nos permiten organizar el código y evitar repetir el mismo código.

# SINTAXIS BÁSICA DE UNA FUNCIÓN:
# def nombre_funcion():
#     código que ejecuta la función
#     return valor_opcional  # Si queremos devolver algo

# ========================================
# EJEMPLO 1: FUNCIÓN SIMPLE SIN PARÁMETROS
# ========================================

def saludar():
    """
    Esta función imprime un saludo en pantalla.
    No recibe parámetros y no devuelve nada.
    """
    print("Hola, bienvenido a Python!")

# Para EJECUTAR o LLAMAR una función, escribimos su nombre seguido de paréntesis
print("=== Ejemplo 1: Función simple ===")
saludar()  # Llama a la función saludar()

# ========================================
# EJEMPLO 2: FUNCIÓN QUE DEVUELVE UN VALOR
# ========================================

def obtener_saludo():
    """
    Esta función devuelve un string con un saludo.
    Usamos 'return' para devolver un valor.
    """
    return "¡Hola desde una función!"

# Podemos guardar el valor devuelto en una variable
print("\n=== Ejemplo 2: Función con return ===")
mensaje = obtener_saludo()  # Guardamos el resultado
print(mensaje)

# O llamar la función directamente dentro de print()
print(obtener_saludo())

# ========================================
# EJEMPLO 3: MÚLTIPLES FUNCIONES
# ========================================

def despedirse():
    """Función que imprime una despedida"""
    print("¡Hasta luego!")

def mostrar_info():
    """Función que muestra información sobre funciones"""
    print("Las funciones hacen el código más organizado y reutilizable.")

print("\n=== Ejemplo 3: Múltiples funciones ===")
mostrar_info()
despedirse()

# ========================================
# PUNTOS CLAVE SOBRE FUNCIONES:
# ========================================
# 1. Se definen con la palabra clave 'def'
# 2. El nombre debe ser descriptivo de lo que hace la función
# 3. Los paréntesis () son obligatorios, aunque la función no tenga parámetros
# 4. El código de la función debe estar indentado (4 espacios o 1 tab)
# 5. 'return' es opcional, si no se usa, la función devuelve None
# 6. Se pueden llamar tantas veces como necesitemos

print("\n=== Llamando la misma función varias veces ===")
saludar()
saludar()
saludar()
