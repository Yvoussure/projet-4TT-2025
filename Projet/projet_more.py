import pandas as pd

df = pd.read_csv('steamdb.csv')

def display_menu():
    print("Menu:")
    print("1. Trier par nom")
    print("2. Trier par current players")
    print("3. Trier par 24h peak")
    print("4. Trier par all-time peak")
    print("5. Trier par ID")
    print("6. Quitter")

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
    else:
        return None

while True:
    display_menu()
    try:
        choice = int(input("Entrez votre choix: "))
        if choice == 6:
            print("Au revoir!")
            break
        elif choice in [1, 2, 3, 4, 5]:
            sorted_df = sort_dataframe(choice)
            print(sorted_df.head())
        else:
            print("Choix invalide. Veuillez réessayer.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")