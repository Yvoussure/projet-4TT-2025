print("voici les numéros lier au calcule :")
print("1 = addition")
print("2 = soustraction")
print("3 = multiplication")
print("4 = division")

choix = int(input("quel opperation voulez-vous effecter ?"))

def addition() :

    nombre1 = int(input("entré vorte premier nombre :"))
    nombre2 = int(input("entré votre second nombre :"))
    somme = nombre1 + nombre2

    print("voici le resultat :", nombre1 ,"+", nombre2, "=", somme)

def soustraction() :

    nombre1 = int(input("entré vorte premier nombre :"))
    nombre2 = int(input("entré votre second nombre :"))
    somme = nombre1 - nombre2

    print("voici le resultat :", nombre1 ,"-", nombre2, "=", somme)

def multiplication() :

    nombre1 = int(input("entré vorte premier nombre :"))
    nombre2 = int(input("entré votre second nombre :"))
    somme = nombre1 * nombre2

    print("voici le resultat :", nombre1 ,"*", nombre2, "=", somme)

def division() :

    nombre1 = int(input("entré vorte premier nombre :"))
    nombre2 = int(input("entré votre second nombre :"))
    somme = nombre1 / nombre2

    print("voici le resultat :", nombre1 ,"/", nombre2, "=", somme)

if choix == 1 :
    addition()
else:
    if choix == 2 :
        soustraction()
    else:
        if choix == 3 :
            multiplication()
        else:
            if choix == 4 :
                division()