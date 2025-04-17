from fonction_utile.fonction_menu import fn_menu

#definition des variable
boucle = True
liste_carct = []

#boucle d'ajout d'elements
while boucle :

#ecriture et ajout des elements de la liste_caract
    caract = input("Entrer une chaine de caractere :")
    liste_carct.append(caract)

    fn_menu()