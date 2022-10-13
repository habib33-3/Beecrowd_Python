InitialSalary = float(input())
Percentage = 0
p = 0

if 0 <= InitialSalary <= 400:
    Percentage = 0.15
    p = 15
elif 400.01 <= InitialSalary <= 800.00:

    Percentage = 0.12
    p = 12
elif 800.01 <= InitialSalary <= 1200.00:

    Percentage = 0.10
    p = 10
elif 1200.01 <= InitialSalary <= 2000.00:
    Percentage = 0.07
    p = 7
elif InitialSalary > 2000:
    Percentage = 0.04
    p = 4

IncreaseSalary = InitialSalary * Percentage
FinalSalary = InitialSalary + IncreaseSalary

print("Novo salario: %0.2f" % FinalSalary)
print("Reajuste ganho: %0.2f" % IncreaseSalary)
print(f"Em percentual: {p} %")
