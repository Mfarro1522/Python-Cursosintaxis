
# FUNCIÓN PRINT EN PYTHON
# La función print() es una de las más básicas e importantes en Python
# Se usa para mostrar información en la consola

# 1. Imprimir texto simple
print("¡Hola, Mundo!")  # Salida: ¡Hola, Mundo!

# 2. Usando comillas simples y dobles
print('Esto también "funciona" ¿ves?')  # Las comillas simples permiten usar comillas dobles dentro

# 3. Imprimir múltiples elementos separados por comas
print("python", "es", "genial")  # Por defecto los separa con espacios

# 4. Usar el parámetro 'sep' para cambiar el separador
print("python", "es", "la", "leche", sep="-")  # Salida: python-es-la-leche

# 5. Usar el parámetro 'end' para cambiar el final de línea
# Por defecto, print() termina con un salto de línea (\n)
print("esto se imprime", end=" ")  # No hace salto de línea, termina con espacio
print("en una línea")  # Se imprime en la misma línea que el anterior

