N = int(input())

InCount = 0
OutCount = 0

for i in range(N):
    X = int(input())
    if 10 <= X <= 20:
        InCount += 1
    else:
        OutCount += 1

print(f"{InCount} in")
print(f"{OutCount} out")
