"""
Ce fichier contient des fonctions pour vérifier si un nombre est premier.
"""
from math import sqrt

#### Fonction secondaire


    # votre code ici

def isprime(p):
    """
    Permet de vérifier si un nombre est premier,
    c'est a dire un nombre qui est dvisible uniquement par 1 et lui meme 
    p=entier positif

    >>> isprime(29)
    True 
    """
    if p==1:
        return False
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
        return True

#### Fonction principale


def main():
    """
    permet de faire des appels de la fonction
    """
    print(isprime(10))
    print(isprime(79))
    print(isprime(1))

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
