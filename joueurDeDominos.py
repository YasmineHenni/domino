
from random import randint

from domino import Domino
from listeDeDominos import ListeDeDominos
from dominosSurLaTable import DominosSurLaTable
from talon import Talon
from jeuDeDominos import Jeu


class Joueur(ListeDeDominos):
    cpt=0
    def __init__(self,n=6,nom=None):
        super().__init__()
        if nom==None:
            Joueur.cpt+=1
            self.nom = "joueur {}".format(self.cpt)
        self.points = 0
        
    def __str__(self):
        """Chaine de caractere caracteristique d'un joueur."""
        str = self.nom + " > main "
        str += ': ' + super().__str__()
        return str

    def __repr__(self):
        """Chaine de caractere caracteristique d'un joueur.
        (voir __str__)"""
        return self.__str__()

    def getNom(self):
        """Retourne le nom du joueur (attribut)."""
        pass

    def getPoints(self):
        """Retourne les points du joueur (attribut)."""
        pass

    def tirerUnDomino(self,unJeu):
        """Tire (aleatroirement) l'un des dominos du jeuDeDomino en argument."""
        pass
    
    def tirerDesDominos(self,unJeu,n):
        """Tire (aleatoirement) n dominos du jeuDeDomino en argument."""
        pass

    def peutIlDebuterUnePartie(self):
        """"Retourne vrai si un joueur peut debuter la partie.
        (Il faut qu'il ait un double pour pouvoir debuter.)
        Dans le cadre de la partie, celui qui commencera sera celui qui aura le plus grand double. 
        Cela ne se decide pas ici."""
        pass
               
    def choisirUnDominoAJouer(self,lesDominosSurLaTable):
        """S'il n'y a pas de dominos sur la table, le joueur retourne l'indice de son plus grand double.
        Sinon, il retourne l'indice d'un domino qui a une valeur adequate relativement aux dominos sur la table.
        S'il n'a rien a jouer, il retourne None."""
        pass
        
    def jouerOuPiocherUnDomino(self,lesDominosSurLaTable,leTalon):
        """Il choisit un domino a jouer et il le joue.
        S'il ne peut pas jouer, il pioche."""
        pass
                
    def calculerLesPointsDeSaMain(self):
        """Retourne la somme de tous les points des dominos presents dans la liste."""
        pass
        
    def mettreLesPointsAJour(self,points):
        """Ajoute les points fournis en arguements a ceux de l'attribut."""
        pass
    
if __name__ == "__main__":

    nombreDeJoueurs = 4

    print("Pour une partie on a besoin de joueurs")
    print("--------------------------------------")
    lesJoueurs = []
    for i in range(nombreDeJoueurs):
        lesJoueurs.append(Joueur())
        print(lesJoueurs[-1])


    print('')
    print("On a besoin d'un jeu de domino")
    print("------------------------------")
    unJeuDeSix = Jeu()
    unJeuDeSix.melanger()
    print(unJeuDeSix)

    
    # distribuer et afficher
    nombreDeDominosParJoueur = ( unJeuDeSix.nombreDeDominosDUnJeu()
                                 // nombreDeJoueurs )
    # on distribue les dominos entre les joueurs
    for j in lesJoueurs:
        j.tirerDesDominos(unJeuDeSix,nombreDeDominosParJoueur)
    print('')
    print("Les joueurs ont recus leurs domino")
    print("----------------------------------")
    for i in range(len(lesJoueurs)):
        print(lesJoueurs[i])

    print('')
    print("Les joueurs ont recus leurs domino")
    print("----------------------------------")
    for j in lesJoueurs:
        points = j.calculerLesPointsDeSaMain()
        j.mettreLesPointsAJour(points)
        print('points : ',j.getPoints())
    
    print('')
    print("parmi les joueurs qui commence")
    print("------------------------------")
    for j in lesJoueurs:
        print(j.getNom(),'pourrait debuter :', j.peutIlDebuterUnePartie())
