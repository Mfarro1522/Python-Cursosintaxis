# VARIABLES EN PYTHON
# Las variables son contenedores para almacenar valores de datos

# ==============================================
# 1. ASIGNACIÓN BÁSICA DE VARIABLES
# ==============================================
# Para asignar un valor a una variable se utiliza el signo igual (=)
# Se puede utilizar cualquier nombre válido para la variable

mi_nombre = "mauri"
print(mi_nombre)  # Salida: mauri

edad = 21
print(edad)      # Salida: 21

# Las variables pueden cambiar de valor
edad = 22
print(edad)      # Salida: 22

# ==============================================
# 2. TIPADO DINÁMICO Y FUERTE
# ==============================================
# Python es un lenguaje de TIPADO DINÁMICO y TIPADO FUERTE

# TIPADO DINÁMICO: El tipo se determina en tiempo de ejecución
# No tienes que declarar el tipo explícitamente
nombre = "mauricio"
print(type(nombre))  # <class 'str'>

nombre = 32
print(type(nombre))  # <class 'int'> - La variable cambió de tipo automáticamente

nombre = "mauricio"  # Volvemos a string

# TIPADO FUERTE: Python NO realiza conversiones de tipo automáticamente
# print("10" + 2)  # ERROR: No puedes sumar string con entero sin conversión explícita

# ==============================================
# 3. F-STRINGS (FORMATEO DE CADENAS)
# ==============================================
# Para mostrar variables dentro de strings usa f-strings (desde Python 3.6)
print(f"Hola {nombre}, tengo {edad + 5} años.")

# ==============================================
# 4. ASIGNACIÓN MÚLTIPLE
# ==============================================
# No es la forma más recomendada, pero es útil conocerla
name, age, city = "mauricio", 22, "madrid"

# ==============================================
# 5. CONVENCIONES PARA NOMBRES DE VARIABLES
# ==============================================

# RECOMENDADAS en Python:
mi_nombre = "mauri"           # snake_case (MÁS USADO)
nombre = "fabian"             # nombre simple

# MENOS USADAS en Python:
nombreCompleto = "mauri"      # camelCase (más común en JavaScript)
MiNombreCompleto = "mauri"    # PascalCase (más común para clases)
minombrecompleto = "mauri"    # todo junto (NO recomendado)

# CONSTANTES (simuladas):
MI_CONSTANTE = 3.1416         # UPPER_CASE para indicar que no debe reasignarse
                              # Python no tiene constantes reales, es solo convención

# ==============================================
# 6. NOMBRES NO VÁLIDOS
# ==============================================
# Estos nombres causarán errores:
# 123_variable = "yo"          # No puede empezar con número
# mi-variable = "yo"           # No puede contener guiones
# mi variable = "yo"           # No puede contener espacios
# true = false                 # No usar palabras reservadas

# Lista de palabras reservadas principales:
# and, as, assert, async, await, break, class, continue, def, del, elif, else,
# except, False, finally, for, from, global, if, import, in, is, lambda, None,
# nonlocal, not, or, pass, raise, return, True, try, while, with, yield

# ==============================================
# 7. TYPE HINTS (ANOTACIONES DE TIPO)
# ==============================================
# Puedes agregar anotaciones de tipo para documentar y mejorar el código
usuario_esta_logueado: bool = True
print(usuario_esta_logueado)  # Salida: True

# IMPORTANTE: Las anotaciones son solo documentación, no previenen reasignación
usuario_esta_logueado = 42   # Esto funciona, aunque no sea el tipo esperado
print(usuario_esta_logueado)  # Salida: 42

# Las anotaciones ayudan a IDEs y herramientas de análisis estático
nombre: str = "mauri"         # Documenta que esperamos un string