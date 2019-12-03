
from domino import Domino
from listeDeDominos import ListeDeDominos

class DominosSurLaTable(ListeDeDominos):
    def __init__(self):
        super().__init__()

    def ordonneCorrectement(self):
        """Retourne vrai si les faces des dominos consecutifs sont coherentes.
        Dans un jeu de domino, les dominos sur la table sont positionnes pour que deux dominos accoles aient des faces qui se correspondent."""
        reponse = True
        pass
    
    def ajouter(self,d,debut=False):
        """Ajoute un domino sur la table.
        Il essaie d'ajouter le domino a la fin des dominos sur la table.
        Ensuite il essaie d'ajouter le domino au debut des dominos sur la table.
        S'il n'a pas reussi a ajouter le domino il genere une erreur.
        """
        pass
        
    def valeursQueLOnPeutAjouter(self):
        """Retourne un tuple contenant les valeurs que l'on peut ajouter sur la table;
        Ces deux valeurs correspondent aux deux faces libres a l'extremite de la liste courrante.
"""
        pass
    
    def peutOnAjouterCeDominoALaFin(self,unDomino):
        """Retourne vrai si on peut ajouter un domino a la fin de la liste."""
        reponse = False
        pass

    def peutOnAjouterCeDominoAuDebut(self,unDomino):
        """Retourne vrai si on peut ajouter un domino au debut de la liste."""
        reponse = False
        pass

    def peutOnAjouterCeDomino(self,unDomino):
        """Retourne vrai si on peut ajouter un domino au debut ou a la fin de la liste."""
        pass
    
if __name__ == '__main__':
    dSurLaTable = DominosSurLaTable()
    dSurLaTable.append(Domino(3,1))
    dSurLaTable.append(Domino(1,2))
    print('dSurLaTable: ',dSurLaTable)
    
    if not dSurLaTable.ordonneCorrectement():
        print('dSurLaTable pas ordonnee correctement.')
    else:
        print('dSurLaTable ordonnee correctement.')
        print("valeurs que l'on peut ajouter :",
              dSurLaTable.valeursQueLOnPeutAjouter())
        l = [Domino(3,3), Domino(2,2)]
        for d in l:
            print('ajout possible au debut:',
                  dSurLaTable.peutOnAjouterCeDominoAuDebut(d))
            print('ajout possible a la fin:',
                  dSurLaTable.peutOnAjouterCeDominoALaFin(d))
            if dSurLaTable.peutOnAjouterCeDomino(d):
                print('ajout de ;', d)
                dSurLaTable.ajouter(d)
        print('dSurLaTable: ',dSurLaTable)
