# fonction affichant le menu du script et renvoyant le choix de l'utilisateur
def fn_menu():
    print(f"\nMenu :")
    print(f"1. Ajouter les informations d'un film à la liste")
    print(f"2. Afficher le contenu de la liste")
    print(f"3. Quitter le programme")
    choix = input(f"Entrez votre choix (1, 2 ou 3) : ")
    return choix

# fonction d'encodage des données d'un utilisateur dans une liste et renvoyant celle-ci
def fn_encode_data_film():
    nom = input("Entrez le nom d'un film : ")
    genre = input("Entrez le genre du film : ")
    date_de_sortie = input("Entrez la date de sortie : ")
    realisateur = input("Entrez le nom du réalisateur : ")
    note_imb = input("Entrer la note IMB du film : ")
    data_film = [nom, genre, date_de_sortie, realisateur,note_imb]
    return data_film


# fonction qui récupère les données d'un utilisateur sous forme de liste et les ajoute dans une liste
def fn_list_data_film(data_film, list_data_film):
    list_data_film.append(data_film)


# fonction d'affichage des données de la liste de liste
def fn_display_list(list_data_film):
    num = 1
    for data in list_data_film:        
        print(f"\nFilm encoder {num}.")
        print(f"Titre du film : {data[0]}")
        print(f"Genre du film : {data[1]}")
        print(f"Date de sortie : {data[2]}")
        print(f"Réalisateur : {data[3]}")
        print(f"Note IMB : {data[4]}")
        num += 1


# fonction principal du script
def fn_app():    
    script_run = True
    list_data_film = []
    while script_run:
        choix = fn_menu()
        match choix :
            case '1':
                data_film = fn_encode_data_film()
                fn_list_data_film(data_film, list_data_film)
            case '2' :
                if list_data_film:
                    fn_display_list(list_data_film)    
                else:
                    print("La liste est vide.")
            case '3' :
                script_run = False
                print(f"Fermeture de l'application")
    else:
        print("Choix non-valide")


# exécution de la fonction principale
fn_app()