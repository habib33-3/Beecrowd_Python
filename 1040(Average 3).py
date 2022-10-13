N1, N2, N3, N4 = list(map(float, input().split()))

Average = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 5) / (2 + 3 + 4 + 5)

print("Media: %0.1f" % Average)

if Average >= 7.0:
    print("Aluno aprovado.")
elif Average < 5.0:
    print("Aluno reprovado.")
elif 5.0 <= Average <= 6.9:
    print("Aluno reprovado.")
    N = float(input())
    print("Nota do exame: %0.1f" % N)
    Average2 = (Average + N) / 2
    if Average2 >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %0.1f" % Average2)
