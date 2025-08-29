# Función con argumentos por posición y clave
def describir_persona(nombre, edad, ciudad="Desconocida"):
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

describir_persona("Ana", 30)
describir_persona("Luis", 25, ciudad="Madrid")
#otro orden
describir_persona(edad=40, nombre="Carlos", ciudad="Barcelona")

# Argumentos de longitud variable (*args): 
def sumar_numeros(*args):
    suma = 0
    for num in args:
        suma += num
    return suma

print(sumar_numeros(1, 2, 3))          # 6
print(sumar_numeros(10, 20, 30, 40))   # 100
print(sumar_numeros())                  # 0

#Argumentos de clave-valor variable (**kwargs):
# kwargs es un diccionario
# 
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=30, ciudad="Madrid")
print("---")
mostrar_info(producto="Laptop", precio=1200, tiene_garantia=True)

