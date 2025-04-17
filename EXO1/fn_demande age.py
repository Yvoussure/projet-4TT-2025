def fn_age() :
    age = int(input("entrer votre age :"))
    return age

def fn_majeur(age_param) :
    if age_param >= 18 :
        print("majeur tu es vieux padaoine")
    else:
        print("trop jeune pour visioner des film pour adulte tu es")

age_global = fn_age()
fn_majeur(age_global)
