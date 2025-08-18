# para asignar un valor a una variable 
# se utiliza el signo igual (=)
# se puede utilizar cualquier nombre para la variable
# python es un lenguaje tipado dinámico y de tipado fuerte

mi_nombre = "mauri"

print(mi_nombre)

edad = 21
print(edad)

edad = 22
print(edad)

#tipado dinamico : el tipo se determina en tiempo de ejecucion
# no tienes que declararlo explicitamente

nombre = "mauricio"
print(type(nombre))

nombre = 32
print(type(nombre))

nombre = "mauricio"

#tipado fuerte: python no realiza conversiones de tipo automaticamente
#print("10" + 2)

#si quieres formatear o mostrar tu variables dentro de se usa f-strings formated string literals
#desde la version 3.6 de python
print(f"hola {nombre} , tengo {edad+5} años.")

#No recomendada forma de asignar variables pero igual saber 
name , age , city = "mauricio" , 22 , "madrid"

#convesiones para los nombres de las variables
mi_nombre = "mauri"  # snake_case
nombre = "fabian" #normal

#poco usados en python
nombreCompleto = "mauri"  # camelCase
MiNombreCompleto = "mauri" #PascalCase
minombrecompleto = "mauri" #todojunto

MI_CONSTANTE = 3.1416 #en python no hay constantes de verdad solo se simulan
                    # pero como convencion se usa upper case para que sepas que no debes de reasignar

#nombres no validos
#123_variable = "yo"
#mi-variable = "yo"
#mi variable = "yo"
#no palabras reservadas
#true = false 

#lista de palabras reservadas
#and, as, assert, async, await, break, 
# class, continue, def, del, elif, else, 
# except, False, finally, for, from, global, 
# if, import, in, is, lambda, None, nonlocal, 
# not, or, pass, raise, return, True, try, 
# while, with, yield

#si tu quieres puedes tipar la variables
usuario_esta_logueado: bool = True
print(usuario_esta_logueado)

#pero igual se reasigna xd , asignarlo es como comentarlo osea como documentar tu tipo
#pero igual puedes hacer con ayudas tanto del ide como con bibliotecas externas
usuario_esta_logueado = 42
print(usuario_esta_logueado)
#teniendo en cuenta que igual se ejecuta

nombre : str = "mauri" #te avisa de mas errores aunque esta debajo del todo parecido a java