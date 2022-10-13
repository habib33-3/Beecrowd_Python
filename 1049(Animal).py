Word1 = str(input())
Word2 = str(input())
Word3 = str(input())
if Word1 == "vertebrado":
    if Word2 == "ave":
        if Word3 == "carnivoro":
            print("aguia")
        elif Word3 == "onivoro":
            print("pomba")
    elif Word2 == "mamifero":
        if Word3 == "onivoro":
            print("homem")
        elif Word3 == "herbivoro":
            print("vaca")
elif Word1 == "invertebrado":
    if Word2 == "inseto":
        if Word3 == "hematofago":
            print("pulga")
        elif Word3 == "herbivoro":
            print("lagarta")
    elif Word2 == "anelideo":
        if Word3 == "hematofago":
            print("sanguessuga")
        elif Word3 == "onivoro":
            print("minhoca")
