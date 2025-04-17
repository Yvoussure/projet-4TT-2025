annee = int(input("Entrer l'annee actuel :"))
bisex = 0
var = True

while var == True:
    bisex = bisex + 4
    
    if bisex == annee:
        print("cette année est bisextile")
        var = False
    elif bisex > annee:
        print("cette année n'est PAS bisextile")
        var = False