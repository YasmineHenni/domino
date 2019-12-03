
from math import floor

from joueurDeDominos import Joueur
from jeuDeDominos import Jeu
from dominosSurLaTable import DominosSurLaTable
from talon import Talon


class Partie:
    def __init__(self,nombreDeJoueurs=3,lesNoms=None,nombreDePoints=6):
        self.lesDominosADistribuer = Jeu(nombreDePoints)
        self.leTalon = Talon()
        self.lesDominosSurLaTable = DominosSurLaTable()
        if nombreDeJoueurs*2 > len(self.lesDominosADistribuer):
            raise ValueError('Trop de joueur ou pas assez de dominos.')
        
        if lesNoms == None:
            lesNoms = [None]*nombreDeJoueurs
        self.lesJoueurs = list()
        for i in range(nombreDeJoueurs):
            self.lesJoueurs.append(Joueur())

    def melanger(self):
        """Melange les dominos avant de les distribuer."""
        pass
    
    def distribuer(self):
        """Distribue les dominos entre les joueurs. Une fois la distribution terminee. Les dominos restant finissent dans le talon."""
        pass
    
    def reordonnerLesJoueurs(self):
        """Ici on determine le joueur qui va jouer en premier.
        (Le premier joueur est celui qui a le plus grand double.)
        On doit ensuite positionner la sous-liste de joueurs le 
        precedent en fin de liste.
        On pourra ainsi effectuer un tour en parcourant simplement 
        la liste de joueurs."""
        """"""
        pass
    
    def aucunDominoSurLaTable(self):
        """Retourne vrai si aucun domino n'est sur la table."""
        pass
    
    def jouerUnTour(self):
        """ Chaque joueur joue une fois dans l'ordre. 
        Si un joueur a termine sa main.
        On sort sans laisser les joueurs suivants jouer.
        (Dans ce cas, la manche est terminee.)
        """
        # le joueur peut dire domino s'il a termine
        # on peut s'amuser a genere une exception rattrapee dans jouerUneManche
        pass

    def mancheTerminee(self):
        """Retourne vrai si la manche est terminee.
        Pour cela il faut qu'un joueur est pose tous ses dominos sur la table. 
        (Il faut donc verifier qu'il y a des dominos sur la table.)
        La partie peut aussi estre bloquee.
        (Aucun joueur ne peut jouer.)
        """
        pass
    
    def calculeEtAjoutDesPointsDUneManche(self):
        """Une fois la manche terminee. 
        On doit calculer les points et les attribuer.
        Pour cela, on doit savoir qui a gagne.
        Les points de la manche correspondent a la somme des points des perdants moins ceux du gagnant.
        (Si la partie est bloquee, il reste des dominos au gagnant.)
        On attribue les points de la manche au joueur gagnant.
        """
        pass
            
    def indiceDuJoueurGagnantDeLaPartie(self):
        """Retourne l'indice du joueur qui a 100 points ou plus.
        Il doit etre le seul dans ce cas."""
        pass
    
    def indiceDuJoueurGagnantDeLaManche(self):
        """Retourne l'indice du joueur gagnant.
        Si la partie est gagnee, il s'agit du joueur n'ayant plus de dominos a la fin de la partie. 
        Si la partie est bloque, il s'agit de celui ayant le moins de points.
        (Cela ne revient-il pas au meme ?)"""
        pass
    
    def indiceDuJoueurAvecLeMoinsDePoints(self):
        """Retourne l'indice du joueur avec le moins de points."""
        indiceDuJoueurAvecLeMoinsDePoints = 0
        sesPoints = self.lesJoueurs[0].getPoints()
        pass
        
    def jouerUneManche(self):
        """Pour jouer une manche :
         - on melange les dominos
         - on les distribue
         - on determine qui commence la partie
         - on joue des tours tant que la manche n'est pas terminee 
         En fin de manche, on calcule et ajoute les points
         et on remet tous les dominos pour qu'ils puissent etre 
        distribues a nouveau."""
        pass

    def afficherLesScores(self):
        """Affiche les scores de tous les joueurs sur une meme ligne.
        Pour chaque joueur on affiche son nom et ses points."""
        pass
        
    def rangerLesDominos(self):
        """On recupere l'ensemble des dominos des acteurs de la partie pour les remettre dans lesDominosADistribuer."""
        pass
        
    def partieTerminee(self):
        """Quand un joueur a 100 points ou plus (et qu'il est le seul) 
        il a gagne et la partie est terminee."""
        pass

    def retournerLeNomDuGagnantDeLaManche(self):
        """Retourne le nom du gagnant de la manche."""
        pass
    
    def retournerLeNomDuGagnantDeLaPartie(self):
        """Retourne le nom du gagnant de partie."""
        pass
    
    def jouerUnePartie(self):
        """Joue des manches tant que la partie n'est pas termine."""        
        pass

        
    def __str__(self):
        str  = ( 'a distribuer : '
                 + self.lesDominosADistribuer.__str__()
                 + '\n' )
        str += 'le talon : '+self.leTalon.__str__()+'\n'
        for j in self.lesJoueurs:
            str += j.__str__()+'\n'
        str += ( 'la table : '
                 + self.lesDominosSurLaTable.__str__()
                 + '\n' )
        return str
    
if __name__ == "__main__":
    if False:
        print('On cree une partie :')
        print('--------------------')
        unePartie = Partie()
        print(unePartie)

        print('On melange les dominos :')
        print('------------------------')
        unePartie.melanger()
        print(unePartie)

        print('On distribue les dominos :')
        print('--------------------------')
        unePartie.distribuer()
        print(unePartie)

        print('On determine qui commence :')
        print('--------------------------')
        unePartie.reordonnerLesJoueurs()
        print(unePartie)

        print('On joue un tour :')
        print('-----------------')
        unePartie.jouerUnTour()
        print(unePartie)

    if True:
        print('On cree une partie :')
        print('--------------------')
        unePartie = Partie()
        print(unePartie)

        print('On joue une partie :')
        print('--------------------')
        unePartie.jouerUnePartie()
        #print(unePartie)
   
