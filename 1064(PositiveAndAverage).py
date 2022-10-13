PositiveCount = 0
Sum = 0

for i in range(0, 6):
    Number = float(input())
    if Number > 0:
        PositiveCount += 1
        Sum += Number

print(f"{PositiveCount} valores positivos")

Average = Sum / PositiveCount
print("%0.1f" % Average)
