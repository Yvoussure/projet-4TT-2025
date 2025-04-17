from fonction_utile.fonction_menu import fn_menu, fn_encode,fn_affiche

#definition des variable
boucle = True
#boucle d'ajout d'elements
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