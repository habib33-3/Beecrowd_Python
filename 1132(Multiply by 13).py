x = int(input())
y = int(input())
sum = 0
mx = max(x, y)
mn = min(x, y)

for i in range(mn, mx+1):
    if i % 13 != 0:
        sum = sum+i

print(sum)
