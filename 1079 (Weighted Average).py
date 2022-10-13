N = int(input())

for i in range(N):
    x, y, z = list(map(float, input().split()))
    average = (x * 2 + y * 3 + z * 5) / (2 + 3 + 5)
    print("%0.1f" % average)
