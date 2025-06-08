import pandas as pd

# Charger le fichier CSV
try:
    df = pd.read_csv('steamdb.csv')
except FileNotFoundError:
    print("Erreur : Le fichier 'steamdb.csv' est introuvable.")
    exit()

def display_menu():
    print("\nMenu:")
    print("1. Trier par nom")
    print("2. Trier par current players")
    print("3. Trier par 24h peak")
    print("4. Trier par all-time peak")
    print("5. Trier par ID")
    print("6. Afficher le nombre total de données")
    print("7. Quitter")

def sort_dataframe(option):
    if option == 1:
        return df.sort_values(by='Name')
    elif option == 2:
        return df.sort_values(by='Current Players', ascending=False)
    elif option == 3:
        return df.sort_values(by='24h Peak', ascending=False)
    elif option == 4:
        return df.sort_values(by='All-Time Peak', ascending=False)
    elif option == 5:
        return df.sort_values(by='ID', ascending=True)
    elif option == 6:
        print(f"Nombre total de données: {len(df)}")
        return None
    else:
        print("Option invalide.")
        return None

while True:
    display_menu()
    try:
        choice = int(input("Entrez votre choix: "))
        if choice == 7:
            print("Au revoir!")
            break
        elif choice in [1, 2, 3, 4, 5]:
            sorted_df = sort_dataframe(choice)
            if sorted_df is not None:
                print(sorted_df.head())
        elif choice == 6:
            sort_dataframe(choice)
        else:
            print("Choix invalide. Veuillez réessayer.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")