Time = int(input())

Day = Month = Year = 0

while Time != 0:
    if Time >= 365:
        Year = Time / 365
        Time = Time % 365
    elif Time >= 30:
        Month = Time / 30
        Time = Time % 30
    else:
        Day = Time
        Time = 0

print("%d ano(s)" % Year)
print("%d mes(es)" % Month)
print("%d dia(s)" % Day)
