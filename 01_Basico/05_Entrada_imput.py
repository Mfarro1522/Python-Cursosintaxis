###
#05 Entrada de datos
# funcion input()
###

print("Hola como te llamas? ")
nombre = input()

print(f"hola {nombre} , encantado de conocerte !")

### otra forma

nombre = input("Hola, como te llamas? \n")
print(f"hola {nombre} , encantado de conocerte !")

age = input("Cuantos años, tienes?\n")
#todo lo que se introduce por input es un string
print(f"tienes {age} años")
print(type(age))
# convertir el tipo de dato
age = int(age)
print(f"tienes {age} años")
print(type(age))

print("Para obtener multiples valores a la vez, se pueden separar por comas")
country , city = input("En que pais y ciudad vives? \n").split() #por defecto el separador es un espacio
print(f"Vives en {city} , {country}")





