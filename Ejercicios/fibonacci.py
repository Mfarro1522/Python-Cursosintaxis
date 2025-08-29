def fibonacci (x):
    if x<=2:
        print("Tiene q ser mayor a 3 ps como quieres una seria de 2 elementos")
    else:
        num ,num1 = 0, 1
        print("0")
        print("1")
        for i in range(x - 2):
            temp = num1
            num1 = num + num1;
            print(num1)
            num = temp

fibonacci(50)