
# fonction affichant le menu du script et renvoyant le choix de l'utilisateur
def fn_menu():
    print(f"\nMenu :")
    print(f"1. Ajouter les informations d'un jeu video à la liste")
    print(f"2. Afficher le contenu de la liste")
    print(f"3. Réinisialiser le fichier")
    print(f"4. Quitter le programme")
    choix = input(f"Entrez votre choix (1, 2, 3 ou 4) : ")
    return choix

# fonction d'encodage des données d'un utilisateur dans une liste et renvoyant celle-ci
def fn_encode_data_game():
    title = input("Entrez le nom du jeu video : ")
    genre = input("Entrez le genre : ")
    date_de_sortie = input("Entrez la date de sortie : ")
    devloppeur = input("Entrez le nom du développeur : ")
    platforme = input("Entrer la/les platforme du jeu : ")
    data_game = [title, genre, date_de_sortie, devloppeur, platforme]
    return data_game

# fonction qui récupère les données d'un utilisateur sous forme de liste et les ajoute dans une liste
def fn_list_data_game(data_game, list_data_game):
    list_data_game.append(data_game)


# fonction d'affichage des données de la liste de liste
def fn_display_list(list_data_game):
    num = 1
    for data in list_data_game:
        print(f"\nJeux video encoder {num}.")
        print(f"Titre du jeu video : {data[0]}")
        print(f"Genre du jeu : {data[1]}")
        print(f"Date de sortie : {data[2]}")
        print(f"Developpeur : {data[3]}")
        print(f"Platfrome jouable : {data[4]}")
        num += 1

def fn_write_list_data_game_to_file(game_file, list_data_game):
    with open(game_file, "a") as file:
        for game in list_data_game:      
            file.write(",".join(str(data) for data in game) + "\n")
    return f"Les données ont été écrites dans le fichier '{game_file}'"

def fn_read_game_file(game_file):
    with open(game_file, "r") as file:
        games_list = file.read()
        print(games_list)

def fn_supp_game_file(game_file):
    with open(game_file, "w") as file:
        file.write

def fn_app():    
    script_run = True
    game_file = "game_file.txt"
    while script_run:
        list_data_game = []
        choix = fn_menu()
        match choix:
            case "1" :
                data_game = fn_encode_data_game()
                fn_list_data_game(data_game, list_data_game)
                debug_msg = fn_write_list_data_game_to_file(game_file, list_data_game)
                print (debug_msg)
            case '2':
                try :
                    fn_read_game_file(game_file)
                except FileNotFoundError:
                    print(f"\nERREUR : Le fichier {game_file} n'existe pas")
            case '3':
                try :
                    fn_supp_game_file(game_file)
                except FileNotFoundError:
                    print(f"\nERREUR : Le fichier {game_file} n'existe pas")
                else:
                    print("Les éléments u fichier on été supprimer")
            case '4':
                script_run = False
                print(f"Fermeture de l'application")
            case _:
                print("Choix non-valide")

# exécution de la fonction principale
fn_app()