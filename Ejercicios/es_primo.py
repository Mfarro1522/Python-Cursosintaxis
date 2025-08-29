import math


def es_primo (n):
    if n<=0 :
        print("ya pe loquito")
    elif n==1:
        return False
    else :
        esPrimo = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if (n % i == 0):
                esPrimo = False
                break
        return esPrimo

def imprimir_primos (n):
    num =0
    while num <n :
        if(es_primo(num)==True):
            print(num)
        num+=1

imprimir_primos(100)