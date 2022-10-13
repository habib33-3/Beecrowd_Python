v = input().split()

a, b, c = v

A = float(a)
B = float(b)
C = float(c)

pi = 3.14159

Triangle = 0.5 * A * C

Circle = pi * C * C

Trapezium = 0.5 * (A + B) * C

Square = B * B

Rectangle = A * B

print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (
Triangle, Circle, Trapezium, Square, Rectangle))
