a, b, c = list(map(float, input().split()))

if a + b > c and b + c > a and a + c > b:
    parameter = a + b + c
    print("Perimetro = %0.1f" % parameter)
else:
    area = 0.5 * c * (a + b)
    print("Area = %0.1f" % area)
