#les fonctions

#ajouter avec , ou +
"""nom = "toto"
print("Je suis", nom,) # 2 paramètres 
print()
print("Je suis" + nom) #concaténé la chaine 1 seul paramètre

nom = input("Votre nom est :")
print("Tu es :", nom)"""


#exo, utilisation fonction
"""pers = int(input("Combien etes vous ?"))

def afficher_info(nom, age):
    print("La personne est", nom, "votre age est", age, "ans")
    print("Le nom comporte", len(nom), "caractere(s)", "l'age comporte", len(age), "caractere(s)")

for x in range (pers):
    afficher_info(input("Quel est votre nom ? "), input("Quel est votre age ? "))""" 

#exo if else
pers = int(input("Combien etes vous ?"))

nom = 0
age = 0
def afficher_info(nom, age):
    if len (age) <=9:
        if len(nom) <=1:
            print("caractere")
        else:
            print("caracteres")            
    else:
        if len(nom) <= 9:
            print("caractere")
        else: 
            print("carcteres") 

for x in range (pers):
    afficher_info(input("Quel est votre nom ? "), input("Quel est votre age ? "))









