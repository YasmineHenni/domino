
class Domino:
    # devrait etre un dictionnaire non modifiable
    VALEUR = {0:' ',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',
              10:'10',11:'11',12:'12',13:'13',14:'14',15:'15',16:'16',
              17:'17',18:'18'}
    def __init__(self,x,y):
        """Un domino est caractérisé par les valeurs de ces deux faces.
        Un domino ne devrait pas pouvoir etre modifie en dehors de sa classe."""
        if ( not isinstance(x,int) or
             not min(Domino.VALEUR.keys())<= x <=max(Domino.VALEUR.keys()) ):
            raise ValueError('x inattendu',x)
        if ( not isinstance(y,int) or
             not min(Domino.VALEUR.keys())<= y <=max(Domino.VALEUR.keys()) ): 
            raise ValueError('y inattendu',y)
        self.valeurs = (x,y)

    def __eq__(self,d):
        """ Teste l'egalite de deux dominos. 
        Attention, les deux faces d'un domino sont interchangeables."""
        pass

    def __lt__(self, other):
        """Opération < comme négation de == et de >."""
        if not isinstance(other,Domino):
            raise TypeError('Domino attendu.')
        return not self == other and not self > other 

    def __le__(self, other):
        """Opération <=  comme negation de >."""
        if not isinstance(other,Domino):
            raise TypeError('Domino attendu.')
        return not self.__gt__(other) 

    def __gt__(self, other):
        """Opération d'ordre >.
        Un domino est superieur si sa valeur max est superieur au max de l'autre.
        Si les deux max sont egaux on ordonne relativement a la valeur de l'autre face (ou au nombre de points du domino).
        """
        pass

    def __ge__(self, other):
        """Opération >= comme negation de <."""
        if not isinstance(other,Domino):
            raise TypeError('Domino attendu.')
        return not self.__lt__(other) 

    def __str__(self):
        return '({},{})'.format(self.VALEUR[self.valeurs[0]],
                                self.VALEUR[self.valeurs[1]])
    
    def __repr__(self):
        return self.__str__()

    def estUnDouble(self):
        """Retourne vrai si on a un double."""
        pass

    def __getitem__(self, k):
        """Permet de connaitre les valeurs des faces d'un domino."""
        pass
    
    def permute(self):
        """Permet de permuter les faces d'un domino. Cela correspond 
        au fait de poser un domino a l'envers dans le jeu."""
        pass
        
    def getLeNombreDePoints(self):
        """Retourne le nombre de points d'un domino. 
        Cela sera particulierement utile pour calculer les points restant 
        dans la main des joueurs en fin de manche."""
        pass
    
if __name__ == "__main__":
    from random import randint
    nombreDePoints = 6

    # genration d'un domino aleatoire
    # avec deux valeurs distinctes
    f1 = randint(0,nombreDePoints)
    while f1 == 0:
        f1 = randint(0,nombreDePoints)
    f2 = randint(0,nombreDePoints)
    while f1 == f2 or f2 == 0:
        f2 = randint(0,nombreDePoints)
    unDomino = Domino(f1,f2)
    
    # generation d'une liste de dominos (pour tester > et ==)
    desDominosAComparer = [Domino(f1,f1),Domino(f2,f2),
                        Domino(f1-1,f2-1),Domino(f1-1,f2),Domino(f1-1,f2+1),
                        Domino(f1,f2-1),Domino(f1,f2),Domino(f1,f2+1),
                        Domino(f1+1,f2-1),Domino(f1+1,f2),Domino(f1+1,f2+1)]
    print("un domino         :",unDomino)

    unDomino.permute()
    print("le domino permute :",unDomino)

    print("Le nombre de points :",unDomino.getLeNombreDePoints())

    for i in desDominosAComparer:
        print(' {}  > {} : {!s:5}'.format(unDomino,i,unDomino>i),end='    ')
        print(' {} == {} : {!s:5}'.format(unDomino,i,unDomino==i))
