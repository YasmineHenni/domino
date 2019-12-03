
from random import shuffle

from domino import Domino
from listeDeDominos import ListeDeDominos

def __creerUnJeuDeSix__(n=6):
    return [Domino(i,j) for i in range(n+1) for j in range(i+1)]
            
class Jeu(ListeDeDominos):
    def __init__(self,n=6):
        super().__init__()
        self.nombreDePoints = n
        self.lesDominos.extend(__creerUnJeuDeSix__(n))

    def __str__(self):
        str = "jeu double-{}: ".format(self.nombreDePoints)
        if len(self) == 0:
            str += "(vide)"
        else:
            str += super().__str__()
        return str

    def melanger(self):
        pass

    def nombreDeDominosDUnJeu(self):
        """Retourne le nombreDeDominos d'un jeu."""
        pass
    
    def estPlein(self):
        """Retourne vrai si le jeu contient tout ses dominos."""
        pass
        
if __name__ == "__main__":

    print("Creation d'un jeu de domino")
    print("---------------------------")
    unJeuDeSix = Jeu()
    print(unJeuDeSix)

    print('')
    print("Melange du jeu de domino")
    print("------------------------")
    unJeuDeSix.melanger()
    print(unJeuDeSix)

    print('')
    print("Divers operations")
    print("-----------------")
    print("un domino extrait: ",unJeuDeSix.pop())
    print('le jeu apres extraction: \n',unJeuDeSix)
    print('le jeu est-il plein ? : ',unJeuDeSix.estPlein())
    print('le nombre de dominos du jeu :',unJeuDeSix.nombreDeDominosDUnJeu())
