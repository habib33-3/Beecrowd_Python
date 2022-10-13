x, y = list(map(int, input().split()))

if y % x == 0 or x % y == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
