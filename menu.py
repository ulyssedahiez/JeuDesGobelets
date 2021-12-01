import deuxJoueurs
import configurations
import partieIA

def menu():
    print("\n --- JEU DES GOBLETS --- \n\n - [1] Nouvelle Partie \n - [2] Options \n - [3] Credits \n - [4] Quitter")
    value = input("\n Selectionnez un numéro : ")
    if(value == "1"):
        newPartie()
    elif(value == "2"):
        configurations.optionsC()
        menu()
    elif(value == "3"):
        print("\n\n Dévelopeur : Ulysse Dahiez \n python version : 3.9.5 \n liste des librairies utilisé : re (Pour les Regex) \n\n")
        input("Pressez entrer pour revenir au menu.\n ")
        menu()
    elif(value == "4"):
        exit()
    else:
        print("\n Mauvaise touche, essayez une touche entre 1 et 4 \n\n")
        menu()
    
def newPartie():
    ficL = open("C:\\Users\\Ulysse Dahiez\\Documents\\AP3\\Algorithmique\\DM_1\\config.txt", "r")
    nbPlayer = int(list(str(ficL.read()))[0])
    ficL.close()
    if(nbPlayer == 2):
        deuxJoueurs.Partie2Players()
        menu()
    if(nbPlayer == 1):
        partieIA.PartieIA()
        menu()







# "11":" ","12":" ","13":" ","21":" ","22":" ","23":" ","31":" ","32":" ","33":" "

       
        


menu()


