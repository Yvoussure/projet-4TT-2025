import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV
try:
    df = pd.read_csv('steamdb.csv')
except FileNotFoundError:
    print("Erreur : Le fichier 'steamdb.csv' est introuvable.")
    exit()

def display_main_menu():
    print("\nMenu Principal:")
    print("1. Statistiques et Graphiques")
    print("2. Tri et Filtrage")
    print("3. Quitter")

def display_stats_menu():
    print("\nMenu Statistiques et Graphiques:")
    print("1. Moyenne, médiane, maximum et minimum")
    print("2. Nombre d’items groupés par catégories choisies")
    print("3. Créer un graphique en camembert")
    print("4. Créer un graphique en histogramme")
    print("5. Retour au menu principal")

def display_sort_menu():
    print("\nMenu Tri et Filtrage:")
    print("1. Trier par ordre croissant")
    print("2. Filtrer (10 premières lignes triées)")
    print("3. Afficher le nombre d’items au-dessus de la moyenne/médiane")
    print("4. Retour au menu principal")

def stats_menu():
    while True:
        display_stats_menu()
        try:
            choice = int(input("Entrez votre choix: "))
            if choice == 1:
                print("Moyenne:\n", df.mean(numeric_only=True))
                print("Médiane:\n", df.median(numeric_only=True))
                print("Maximum:\n", df.max(numeric_only=True))
                print("Minimum:\n", df.min(numeric_only=True))
            elif choice == 2:
                print("Colonnes disponibles :", df.columns.tolist())
                category = input("Entrez la colonne pour regrouper les données: ")
                if category in df.columns:
                    print(df.groupby(category).size())
                else:
                    print("Colonne invalide.")
            elif choice == 3:
                print("Colonnes disponibles :", df.columns.tolist())
                category = input("Entrez la colonne pour le graphique en camembert: ")
                if category in df.columns:
                    df[category].value_counts().plot.pie(autopct='%1.1f%%')
                    plt.title(f"Graphique en camembert pour {category}")
                    plt.show()
                else:
                    print("Colonne invalide.")
            elif choice == 4:
                print("Colonnes disponibles :", df.columns.tolist())
                column = input("Entrez la colonne pour l'histogramme: ")
                if column in df.columns:
                    df[column].plot.hist(bins=10)
                    plt.title(f"Histogramme pour {column}")
                    plt.show()
                else:
                    print("Colonne invalide.")
            elif choice == 5:
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def sort_menu():
    while True:
        display_sort_menu()
        try:
            choice = int(input("Entrez votre choix: "))
            if choice == 1:
                print("Colonnes disponibles :", df.columns.tolist())
                column = input("Entrez la colonne pour trier les données: ")
                if column in df.columns:
                    print(df.sort_values(by=column, ascending=True).head())
                else:
                    print("Colonne invalide.")
            elif choice == 2:
                print("Colonnes disponibles :", df.columns.tolist())
                column = input("Entrez la colonne pour filtrer les données: ")
                if column in df.columns:
                    print(df.sort_values(by=column, ascending=True).head(10))
                else:
                    print("Colonne invalide.")
            elif choice == 3:
                print("Colonnes disponibles :", df.columns.tolist())
                column = input("Entrez la colonne pour calculer les items au-dessus de la moyenne/médiane: ")
                if column in df.columns:
                    above_mean = df[df[column] > df[column].mean()]
                    above_median = df[df[column] > df[column].median()]
                    print(f"Nombre d'items au-dessus de la moyenne: {len(above_mean)}")
                    print(f"Nombre d'items au-dessus de la médiane: {len(above_median)}")
                else:
                    print("Colonne invalide.")
            elif choice == 4:
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

while True:
    display_main_menu()
    try:
        choice = int(input("Entrez votre choix: "))
        if choice == 1:
            stats_menu()
        elif choice == 2:
            sort_menu()
        elif choice == 3:
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")