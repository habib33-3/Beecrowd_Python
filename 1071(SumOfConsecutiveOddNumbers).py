Start = int(input())
End = int(input())

Sum = 0

if Start > End:
    for i in range(Start, End):
        if i % 2 != 0:
            Sum = Sum + i
else:
    for i in range(End, Start):
        if i % 2 != 0:
            Sum = Sum + i

print(Sum)
