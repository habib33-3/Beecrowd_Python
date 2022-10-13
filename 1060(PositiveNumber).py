N1 = float(input())
N2 = float(input())
N3 = float(input())
N4 = float(input())
N5 = float(input())
N6 = float(input())

Numbers = [N1, N2, N3, N4, N5, N6]

PositiveCount = 0

for N in Numbers:
    if N > 0:
        PositiveCount += 1

print(f"{PositiveCount} valores positivos")
