X = int(input())
Y = int(input())

Sum = 0

Start = min(X, Y) + 1
End = max(X, Y)

if Start % 2 == 0:
    Start += 1

for i in range(Start, End, 2):
    Sum += i

print(Sum)
