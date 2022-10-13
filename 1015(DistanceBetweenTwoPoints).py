import math

p = input().split()
q = input().split()

x1, y1 = p
x2, y2 = q

X1 = float(x1)
X2 = float(x2)
Y1 = float(y1)
Y2 = float(y2)

Distance = math.sqrt(((X2 - X1) ** 2) + ((Y2 - Y1) ** 2))

print("%0.4f" % Distance)
