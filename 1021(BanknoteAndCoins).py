Money = int(input())

Hundred = Fifty = Twenty = Ten = Five = Two = One = Note = 0
Note = Money

while Money != 0:
    if Money >= 100:
        Hundred = Money / 100
        Money = Money % 100
    elif Money >= 50:
        Fifty = Money / 50
        Money = Money % 50
    elif Money >= 20:
        Twenty = Money / 20
        Money = Money % 20
    elif Money >= 10:
        Ten = Money / 10
        Money = Money % 10
    elif Money >= 5:
        Five = Money / 5
        Money = Money % 5
    elif Money >= 2:
        Two = Money / 2
        Money = Money % 2
    elif Money>=1:
        One=Money
        Money=Money-1

    elif Money>=0.50:
        FiftyCent=


print(Note)
print("%d nota(s) de R$ 100,00" % Hundred)
print("%d nota(s) de R$ 50,00" % Fifty)
print("%d nota(s) de R$ 20,00" % Twenty)
print("%d nota(s) de R$ 10,00" % Ten)
print("%d nota(s) de R$ 5,00" % Five)
print("%d nota(s) de R$ 2,00" % Two)
print("%d nota(s) de R$ 1,00" % One)
