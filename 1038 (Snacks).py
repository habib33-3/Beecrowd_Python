X, Y = list(map(int, input().split()))

if X == 1:
    Price = Y * 4.00
elif X == 2:
    Price = Y * 4.50
elif X == 3:
    Price = Y * 5.00
elif X == 4:
    Price = Y * 2.00
elif X == 5:
    Price = Y * 1.50

print("Total: R$ %0.2f" % Price)
