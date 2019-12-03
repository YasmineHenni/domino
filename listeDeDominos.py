
from domino import Domino

class ListeDeDominos:
    def __init__(self):
        self.lesDominos = []

    def __extend__(self,uneListeDeDominos):
        """N'est pas considere appropriee ici."""
        raise NotImplementedError('Ne doit pas etre appelee/implementee.')

    def __setitem__(self, k, d):
        """N'est pas considere appropriee ici."""
        raise NotImplementedError('Ne doit pas etre appelee/implementee.')
    
    def __contains__(self,d):
        """Verifie si un domino d est contenu dans la liste de dominos."""
        pass
    
    def __getitem__(self, k):
        """N'est pas considere appropriee ici."""
        raise NotImplementedError('Ne doit pas etre appelee/implementee.')
    
    def __eq__(self,l):
        """N'est pas considere appropriee ici."""
        raise NotImplementedError('Ne doit pas etre appelee/implementee.')
        
    def __len__(self):
        """Retourne le nombre de Domino dans la liste de dominos."""
        return self.lesDominos.__len__()


    def __str__(self):
        """Retourne la chaine de caracteres des Dominos et 'vide' si elle est vide."""
        str = "vide"
        if len(self) != 0:
            str =  self.lesDominos.__str__()
        return str

    def __repr__(self):
        """Retourne une chaine de catacteres voir __str__."""
        return self.lesDominos.__repr__()

    def append(self,d):
        """Insere un domino d à la fin de la liste de dominos."""
        pass

    def copy(self):
        """N'est pas considere appropriee ici."""
        raise NotImplementedError('Ne doit pas etre appelee/implementee.')

    def extend(self,uneListeDeDominos):
        """N'est pas considere appropriee ici."""
        raise NotImplementedError('Ne doit pas etre appelee/implementee.')
    
    def insert(self,i,d):
        """Insere un domino a la position i de la liste de dominos."""
        pass
    
    def remove(self,unDomino):
        """N'est pas considere appropriee ici."""
        raise NotImplementedError('Ne doit pas etre appelee/implementee.')
    
    def sort(self,reverse=False):
        """Ordonne les points pour faciliter certaines operations.
        L'odre n'a pas de sens en tant que tel. 
        Cette opération se base sur les  relations d'ordre de la classe domino."""
        self.lesDominos.sort()
        
    def clear(self):
        """N'est pas considere appropriee ici."""
        raise NotImplementedError('Ne doit pas etre appelee/implementee.')
        
    def count(self,unDomino):
        """N'est pas considere appropriee ici."""
        raise NotImplementedError('Ne doit pas etre appelee/implementee.')
    
    def index(self,d):
        """Retourne l'indice de la première (et unique) occurrence d'un domino."""
        pass
    
    def pop(self,i=-1):
        """Extrait et retourne le domino en position i."""
        pass
    
    def reverse(self):
        """Tri la liste dans l'ordre décroissant. Voir sort."""
        raise NotImplementedError('Pourrait etre implementee.')
        pass

    def estVide(self):
        """Retourne vrai si la liste est vide."""
        pass

    def contientUnDouble(self):
        """Retourne vrai si la liste contient un double."""
        reponse = False
        pass

    def rendreLesDominos(self,jeu):
        """Extrait les dominos contenus dans la liste et les ajoute a jeu."""
        pass

    def getValeurDuPlusGrandDouble(self):
        valeur = None
        pass

    def getIndiceDuPlusGrandDouble(self):
        """Retourne l'indice du plus grand double."""
        pass
    
    def derniereValeur(self):
        """Retourne la derniere valeur du dernier domino."""
        pass

    def premiereValeur(self):
        """Retourne la premiere valeur du premier domino."""
        pass

if __name__ == "__main__":

    #from warnings import warn
    from random import randint

    nombreDePoints = 6

    print('\nCreation de la liste avec ajouts et retraits')
    print('--------------------------------------------')

    uneListe = ListeDeDominos() 
    print("La liste:",uneListe)

    unDomino = Domino(1,2)
    print('On ajoute:',unDomino)
    uneListe.append(unDomino)
    print("La liste:",uneListe)

    print("On ajoute des dominos.")
    while len(uneListe) < 7:
        unDomino = Domino(randint(0,nombreDePoints),randint(0,nombreDePoints))
        if not unDomino in uneListe:
            uneListe.append(unDomino)
    print("La liste:",uneListe)

    print("On extrait un domino a la fin :",uneListe.pop())
    print("La liste:",uneListe)

    print('\nTri la liste')
    print('------------')
    
    print('On trie la liste')
    uneListe.sort()
    print("La liste:",uneListe)

    k = 2
    print(f"On extrait le domino d'indice {k}:",uneListe.pop(k))
    print("La liste:",uneListe)

    print('premiere valeur: ',uneListe.premiereValeur())
    print('derniere valeur: ',uneListe.derniereValeur())

    if uneListe.contientUnDouble():
        print('valeur du plus grand double : ',
              uneListe.getValeurDuPlusGrandDouble())
        print('indice du plus grand double : ',
              uneListe.getIndiceDuPlusGrandDouble())
    else:
        print('pas de double.')

    #from jeuDeDominos import Jeu
    l =  ListeDeDominos() 
    uneListe.rendreLesDominos(l)
    print('La liste rend les dominos:')
    print('--------------------------')
    print("La liste:",uneListe)
    print('les dominos rendus:', l)

    
