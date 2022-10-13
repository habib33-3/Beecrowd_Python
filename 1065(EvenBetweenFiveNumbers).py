EvenCount = 0

for i in range(0, 5):
    Number = float(input())
    if Number % 2 == 0:
        EvenCount += 1

print(f"{EvenCount} valores pares")
