
from domino import Domino

from listeDeDominos import ListeDeDominos
from jeuDeDominos import Jeu

class Talon(ListeDeDominos):
    def __init__(self,n=6):
        super().__init__()

    def remplir(self,unJeu):
        """Permet au talon de recuperer les dominos restant dans unJeu.""" 
        pass

    
if __name__ == "__main__":

    from joueurDeDominos import Joueur
    
    leTalon = Talon()
    print(leTalon)

    print('')
    print("On a besoin d'un jeu de domino")
    print("------------------------------")
    unJeuDeSix = Jeu()
    unJeuDeSix.melanger()
    print(unJeuDeSix)

    print('')
    print("On a besoin de joueurs")
    print("----------------------")
    nombreDeJoueurs = 2
    lesJoueurs = []
    for i in range(nombreDeJoueurs):
        lesJoueurs.append(Joueur())

    nombreDeDominosParJoueur = 10
    # on distribue les dominos entre les joueurs
    for j in lesJoueurs:
        j.tirerDesDominos(unJeuDeSix,nombreDeDominosParJoueur)
    print('')
    for i in range(len(lesJoueurs)):
        print(lesJoueurs[i])

        
    # remplir le talon et afficher
    print('')
    print("Remplir le talon")
    print("----------------")
    leTalon.remplir(unJeuDeSix)
    print("le talon:", leTalon)

    ## ici on peut pas tester tirerUnDomino
    ## car ici on utilise une classe de test : 
    # __main__.Talon
    ## Cela resulterait donc en message d'erreur
    # piocher/vider le talon et afficher
    #print('')
    #print("Les joueurs piochent un domino")
    #print("------------------------------")
    #for j in lesJoueurs:
    #    j.tirerUnDomino(leTalon)
    #    print(lesJoueurs[i])


    
