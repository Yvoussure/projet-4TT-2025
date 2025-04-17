def age() :
    blaguenul = ""

    age = int(input("entrer votre age :"))
    pegi = 18
    
    if age < pegi:
        while blaguenul != "non" :
            print("votre age est", age, "alors que l'age néccesaire est de", pegi)
            blaguenul = input("est-vos sur de vouloir coninuer ?")
    else:
        print("votre age est de", age, "merci d'avoir partager vos informations personnel. mtn jvais pirater sale nul")

age()