# Programa para verificar un numero es par o impar

# input
x= int(input("Digite el valor de x: "))

# processing

r= x%2

if r==0:
    rta="Par"
else:
    rta="Impar"

# output

print("el numero " + str(x) + " es " + rta)
