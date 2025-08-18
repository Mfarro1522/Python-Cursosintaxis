###
#03 - casting types
#transformar un tipo de valor a otro
###

print("Conversion de tipos")
#print(type(int("100")))  
#print(2 + int("100"))
#print("100"+str(2)) 

#print(type(float("3.1416")))
#print(int(3.1416)) #tener en cuanta no redondea solo desaparece el decimal

#print(bool(3)) 
#print(bool(0)) #solo cero false
#print(bool(-5)) 

#print(bool("")) #solo cadena vacia false
#print(bool("hola")) 
#print(bool("true")) 

##print(bool([])) #solo lista vacia false

#errores consejo sentido comun 

#print(int("hola Mundo"))

#extra metodo round
print(round(2.5))  # Resultado: 2 (2 es par)
print(round(3.5))  # Resultado: 4 (4 es par)

"""""
Python aplica la regla de "redondeo al par más cercano" (también llamada "round half to even" o "redondeo bancario").
Esto significa que si el dígito anterior al .5 es par, se queda igual; si es impar, sube al siguiente número par.

"""""

