Number = float(input())

if Number >= 0 and Number <= 25:
    print("Intervalo [0,25]")
elif Number > 25 and Number <= 50:
    print("Intervalo (25,50]")
elif Number > 50 and Number <= 75:
    print("Intervalo (50,75]")
elif Number > 75 and Number <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
