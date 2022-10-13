Product1 = input().split()
Product2 = input().split()

Code1, Unit1, Price1 = Product1
Code2, Unit2, Price2 = Product2

Cost1 = float(Price1) * int(Unit1)
Cost2 = float(Price2) * int(Unit2)

Total = float(Cost1) + float(Cost2)

print("VALOR A PAGAR: R$ %0.2f" % Total)
