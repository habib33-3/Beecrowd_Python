access = False

while access == False:
    password = int(input())

    if password == 2002:
        print("Acesso Permitido")
        access = True
    else:
        print("Senha Invalida")
