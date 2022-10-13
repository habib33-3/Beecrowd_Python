import math

Number = input().split()

A, B, C = Number

a = float(A)
b = float(B)
c = float(C)

Discriminate = (b ** 2) - 4 * a * c

if Discriminate < 0 or a == 0:
    print("Impossivel calcular")

else:
    R1 = (-b + math.sqrt(Discriminate)) / (2 * a)

    print("R1 = %0.5f" % R1)

    R2 = (-b - math.sqrt(Discriminate)) / (2 * a)

    print("R2 = %0.5f" % R2)
