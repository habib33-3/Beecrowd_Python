NumberOfTest = int(input())
RabbitCount = 0
RatCount = 0
FrogCount = 0

for i in range(NumberOfTest):
    n, NameOfAnimal = list(map(str, input().split()))
    NumberOfAnimal = int(n)

    if NameOfAnimal == "C":
        RabbitCount += NumberOfAnimal
    elif NameOfAnimal == "R":
        RatCount += NumberOfAnimal
    elif NameOfAnimal == "S":
        FrogCount += NumberOfAnimal

TotalAnimals = (FrogCount + RatCount + RabbitCount)

Rabbit = (RabbitCount * 100) / TotalAnimals
Rat = (RatCount * 100) / TotalAnimals
Frog = (FrogCount * 100) / TotalAnimals

print(f"Total: {TotalAnimals} cobaias")

print(f"Total de coelhos: {RabbitCount}")
print(f"Total de ratos: {RatCount}")
print(f"Total de sapos: {FrogCount}")

print("Percentual de coelhos: %0.2f %%" % Rabbit)
print("Percentual de ratos: %0.2f %%" % Rat)
print("Percentual de sapos: %0.2f %%" % Frog)
