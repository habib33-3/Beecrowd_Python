EmployeeName = input()
Salary = float(input())
Sell = float(input())

Bonus = Sell * (15 / 100)

Total = Salary + Bonus

print("TOTAL = R$ %0.2f" % Total)
