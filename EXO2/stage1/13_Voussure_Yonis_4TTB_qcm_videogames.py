def poser_question(elm, nmb_libelle) :
    choix_user = 0
    print(f"{elm.get("libelle")}")
    for chx in elm.get("choix"):
        choix_user += 1
        print(f"{choix_user} : {chx}")
    reponse = int(input("choisi la bonne reponse "))
    if reponse == elm.get("reponse"):
        return True
    else: 
        return False
    
    
    

qcm = [{"libelle": "Who is the first friend/alliy we make in Cyberpunk 2077 ?"
    ,"choix": ["Jackie", "Johnny Sliverhand", "Yurinobu","Adam Smasher"]
    ,"reponse": 1},
    {"libelle": "What happen if we withdraw the puce ?"
    ,"choix": ["we exit the simulation", "Johnny Silverhand take our controle", "we die","the game just end"]
    ,"reponse": 3},
    {"libelle": "What is the objective of our charactere ?"
    ,"choix": ["Save the world", "Kill yurinobu and destroy arasaka", "Revive Jackie", "Take the puce out without dying"]
    ,"reponse": 4},
    {"libelle": "How many end have Cyberpunk 2077 ?"
    ,"choix": ["1", "5", "7", "3"]
    ,"reponse": 2},
    {"libelle":"Who kill his/herelf ?"
    ,"choix": ["Evelyn", "Jackie", "Our character", "A random NPC in a mission"]
    ,"reponse": 1},
    {"libelle": "What are the name of the group of Johnny Silverhand ?"
    ,"choix": ["The Silverhands", "Destroyers", "Samourai", "The peacemakers"]
    ,"reponse": 3},
    {"libelle": "Who is the name of our best friend(ripperdocs )"
    ,"choix": ["Jackie", "Judy", "Viktor", "Panam"]
    ,"reponse": 3},
    {"libelle": "What is the name of our character ?"
    ,"choix": ["Viktor", "Vincent", "Just 'V'", "David martinez"]
    ,"reponse": 2 and 3}]

nmb_libelle = 0

# on parcourt la liste des questions et on calcule le score de l'utilisateur
score = 0

for elm in qcm:
    nmb_libelle += 1
    if poser_question(elm,nmb_libelle) == True:
        score += 1

final_score = 10/nmb_libelle*score

print("Vous avez obtenu un score de ", final_score)