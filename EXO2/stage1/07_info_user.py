# fonction affichant le menu du script et renvoyant le choix de l'utilisateur
def fn_menu():
    print(f"\nMenu :")
    print(f"1. Ajouter les informations d'un utilisateur à la liste")
    print(f"2. Afficher le contenu de la liste")
    print(f"3. Quitter le programme")
    choix = input(f"Entrez votre choix (1, 2 ou 3) : ")
    return choix

# fonction d'encodage des données d'un utilisateur dans une liste et renvoyant celle-ci
def fn_encode():
    nom = input("Entrer votre nom : ")
    prenom = input("Entrer votre prénom : ")
    date = input("Entrer votre date naissence : ")
    code_postal = input("Entrer votre code postal : ")
    liste_user = [nom, prenom, date, code_postal]
    return liste_user

# fonction qui récupère les données d'un utilisateur sous forme de liste et les ajoute dans une liste
def fn_liste(liste_user, liste_liste):
    liste_liste.append(liste_user)
    return liste_liste

# fonction d'affichage des données de la liste de liste
def fn_affiche(liste_liste):
    print(liste_liste)
    
# Execution du script
boucle = True
liste_liste = []

while boucle :
    choix = fn_menu()
    if choix == "1":
        liste_user = fn_encode()
        fn_liste(liste_user,liste_liste)
    elif choix == "2":
        fn_affiche(liste_liste)
    elif choix == "3":
        boucle = False
    else:
        print("Le choix est invalide")