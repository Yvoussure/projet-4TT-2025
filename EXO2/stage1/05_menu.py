from annee_bisex_opti import fn_bisex

var = True

while var == True:
    fn_bisex()
    cont = input("voulez vous continuer (True ou False) ?")
    if cont == "False" or "false":
        var = False