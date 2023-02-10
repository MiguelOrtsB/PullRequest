# ACTIVIDAD 48
print("Programa para desglosar una contidad de denero en Euros(€)")
n = int(input("Introduce la cantidad deseas desglosar: "))
y = n
if y // 500 > 0:
    c = y // 500
    print(str(c), "billetes de 500€")
    y = y - (500*c)

if y // 200 > 0:
    c = y // 200
    print(str(c), "billetes de 200€")
    y = y - (200*c)

if y // 100 > 0:
    c = y // 100
    print(str(c), "billetes de 100€")
    y = y - (100*c)

if y // 50 > 0:
    c = y // 50
    print(str(c), "billetes de 50€")
    y = y - (50*c)

if y // 20 > 0:
    c = y // 20
    print(str(c), "billetes de 20€")
    y = y - (20*c)

if y // 10 > 0:
    c = y // 10
    print(str(c), "billetes de 10€")
    y = y - (10*c)

if y // 5 > 0:
    c = y // 5
    print(str(c), "billetes de 5€")
    y = y - (5*c)

if y // 2 > 0:
    c = y // 2
    print(str(c), "monedas de 2€")
    y = y - (2*c)

if y // 1 > 0:
    c = y // 1
    print(str(c), "monedas de 1€")

