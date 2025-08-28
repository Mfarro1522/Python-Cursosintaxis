##boleanos : true , false

print("Valores booleanos basicos:")
print(True)
print(False)

#operadores de comparacion

print("Operadores de comparacion")
print("5 > 3:", 5 > 3) # true , Mayor que
print("5 < 3:", 5 < 3) # false , Menor que
print("5 >= 3:", 5 >= 3) # true , Mayor o igual que
print("5 <= 3:", 5 <= 3) # false , Menor o igual que
print("5 == 3:", 5 == 3) # false , Igual que
print("5 != 3:", 5 != 3) # true , Distinto que

print("Comparacion de cadenas:")
print("Manzana" < "Pera") # true , en pythin las cadenas se comparan lexilograficamente 
print(" 'Hola == 'hola'" , 'Hola' == 'hola') # false , las cadenas son case sensitive

#operadores logicos : and , or , not

print("Operadores logicos:")
print("True and False:", True and False) # false , ambas condiciones deben ser true
print("True or False:", True or False) # true , al menos una condicion debe ser true
print("not True:", not True) # false , invierte el valor booleano
print("not False:", not False) # true , invierte el valor booleano 
# en si sigue las lleyes de la logica matematic
# 
#Como referencia tablas de verdad

print("\nTabla de verdad AND:")
print("A     B      A and B ")
print("True  True  ", True and True)
print("True  False ", True and False)
print("False  True ", False and True)
print("False  False", False and False)

print("\nTabla de verdad OR:")
print("A     B      A or B ")
print("True  True  ", True or True)
print("True  False ", True or False)
print("False  True ", False or True)
print("False  False", False or False)

print("\nTabla de verdad NOT:")
print("A      not A ")
print("True  ", not True)
print("False ", not False)
