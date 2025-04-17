
def fn_leave() :
#affichage des choix
    print("1. Continuer")
    print("2. Afficher la liste et Continuer")
    print("3. Quitter")
    cont = input("Choisiser une option : ")

#si la variable cont a la valeur 1 la boucle recommence
#si la variable cont à la valeur 3 ou 4 il quitte la boucle
#si la variable cont à la valeur 2 ou 4 il affiche la liste
    if cont == 1:
        boucle = True
    
    elif cont == 2:
        boucle = True
        print(liste_carct)
    
    elif cont == 3:
        boucle = False