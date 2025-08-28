# TIPOS DE DATOS EN PYTHON
# Python tiene varios tipos de datos incorporados fundamentales:
# int, float, complex, str, bool, NoneType, list, tuple, dict, range, set, etc.

# ==============================================
# 1. NÚMEROS ENTEROS (int)
# ==============================================
print("=== NÚMEROS ENTEROS (int) ===")
print(type(10))           # <class 'int'>
print(type(0))            # <class 'int'>
print(type(-5))           # <class 'int'>
print(type(12212121212413))  # <class 'int'>

# Python maneja enteros de tamaño arbitrario sin límites
print(7313121234532324234234432)
print(7313121234532324234234432 + 1)  # Python optimiza mejor que otros lenguajes el manejo de enteros

# ==============================================
# 2. NÚMEROS DECIMALES (float)
# ==============================================
print("\n=== NÚMEROS DECIMALES (float) ===")
print(type(10.5))         # <class 'float'>
print(type(0.0))          # <class 'float'>
print(type(1e5))          # <class 'float'> - Notación científica (100000.0)

# ==============================================
# 3. NÚMEROS COMPLEJOS (complex)
# ==============================================
print("\n=== NÚMEROS COMPLEJOS (complex) ===")
print(type(1 + 2j))       # <class 'complex'>
print(type(0j))           # <class 'complex'> - Nota: Python usa 'j' en lugar de 'i' como en matemáticas

# ==============================================
# 4. CADENAS DE TEXTO (str)
# ==============================================
print("\n=== CADENAS DE TEXTO (str) ===")
print(type("hola"))       # <class 'str'>
print(type(''))           # <class 'str'> - Cadena vacía
print(type("123"))        # <class 'str'> - Números como texto
print(type("""
multi
linea
string
"""))                     # <class 'str'> - Cadena multilínea

# ==============================================
# 5. VALORES BOOLEANOS (bool)
# ==============================================
print("\n=== VALORES BOOLEANOS (bool) ===")
print(type(True))         # <class 'bool'>
print(type(False))        # <class 'bool'>
print(type(1 < 2))        # <class 'bool'> - Resultado de una comparación

# ==============================================
# 6. VALOR NULO (NoneType)
# ==============================================
print("\n=== VALOR NULO (NoneType) ===")
print(type(None))         # <class 'NoneType'> - Representa ausencia de valor