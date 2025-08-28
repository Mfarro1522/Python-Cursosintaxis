# CONVERSIÓN DE TIPOS (CASTING)
# Transformar un tipo de valor a otro tipo
# Esto es útil cuando necesitas operar con datos de diferentes tipos

print("=== CONVERSIÓN DE TIPOS ===")

# ==============================================
# 1. CONVERSIÓN A ENTERO (int)
# ==============================================
print("\n--- Conversión a int ---")
print(type(int("100")))      # Convierte string "100" a entero 100
print(2 + int("100"))        # Suma: 2 + 100 = 102
print(int(3.1416))           # Convierte float a int (ATENCIÓN: trunca, no redondea)

# ==============================================
# 2. CONVERSIÓN A STRING (str)
# ==============================================
print("\n--- Conversión a str ---")
print("100" + str(2))        # Concatena strings: "100" + "2" = "1002"

# ==============================================
# 3. CONVERSIÓN A FLOAT (float)
# ==============================================
print("\n--- Conversión a float ---")
print(type(float("3.1416")))  # Convierte string "3.1416" a float 3.1416

# ==============================================
# 4. CONVERSIÓN A BOOLEANO (bool)
# ==============================================
print("\n--- Conversión a bool ---")
print(bool(3))               # Cualquier número diferente de 0 es True
print(bool(0))               # Solo el 0 es False
print(bool(-5))              # Números negativos también son True

print(bool(""))              # Solo cadena vacía es False
print(bool("hola"))          # Cualquier cadena con contenido es True
print(bool("false"))         # Incluso la palabra "false" es True (porque no está vacía)

print(bool([]))              # Solo lista vacía es False

# ==============================================
# 5. ERRORES COMUNES - SENTIDO COMÚN
# ==============================================
print("\n--- Errores comunes ---")
# print(int("hola Mundo"))   # ERROR: No se puede convertir texto no numérico a entero

# ==============================================
# 6. FUNCIÓN ROUND() - REDONDEO
# ==============================================
print("\n--- Función round() ---")
print(round(2.5))            # Resultado: 2 (2 es par)
print(round(3.5))            # Resultado: 4 (4 es par)
print(round(2.6))            # Resultado: 3 (redondeo normal)
print(round(2.4))            # Resultado: 2 (redondeo normal)

"""
IMPORTANTE: Python aplica la regla de "redondeo al par más cercano" 
(también llamada "round half to even" o "redondeo bancario").

Esto significa que cuando el decimal es exactamente .5:
- Si el dígito anterior es par, se mantiene igual
- Si el dígito anterior es impar, sube al siguiente número par

Ejemplos:
- 2.5 → 2 (porque 2 es par)
- 3.5 → 4 (porque 3 es impar, sube al par siguiente)

Esta regla ayuda a reducir el sesgo estadístico en cálculos largos.
"""

