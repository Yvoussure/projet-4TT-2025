
def fn_menu() :
#affichage des choix
    print("1. Encoder")
    print("2. Afficher la liste")
    print("3. Quitter")
    choix = int(input("Choisiser une option : "))
    return choix

def fn_encode(list_caract) :
    chn_caract = input("Entrer une chaine de caractere : ")
    list_caract.append(chn_caract)

def fn_affiche(list_caract) :
    for index, item in enumerate(list_caract, start=1):
        print(f"{index},{item}")

boucle = True

while boucle :
    fn_menu()

    if fn_menu() == 1:
        fn_encode()

    elif fn_menu() == 2:
        fn_affiche()

    elif fn_menu() == 3:
        boucle = False
    else:
        print("Le choix n'est pas valide")