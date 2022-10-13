EvenCount = 0
OddCount = 0
PositiveCount = 0
NegativeCount = 0

for i in range(5):
    Number = int(input())
    if Number % 2 == 0:
        EvenCount = EvenCount + 1
    else:
        OddCount = 1 + OddCount
    if Number > 0:
        PositiveCount = 1 + PositiveCount
    elif Number < 0:
        NegativeCount = 1 + NegativeCount

print(f"{EvenCount} valor(es) par(es)")
print(f"{OddCount} valor(es) impar(es)")
print(f"{PositiveCount} valor(es) positivo(es)")
print(f"{NegativeCount} valor(es) negativo(es)")
