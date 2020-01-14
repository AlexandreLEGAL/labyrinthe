# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module carte
   ~~~~~~~~~~~~
   
   Ce module gère les cartes du labyrinthe. 
"""
import random

"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'code du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'code ne correspond pas à une carte
"""
listeCartes = ['╬', '╦', '╣', '╗', '╩', '═', '╝', 'Ø', '╠', '╔', '║', 'Ø', '╚', 'Ø', 'Ø', 'Ø']


def Carte(nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """
    return {"Mur": (nord, est, sud, ouest), "Tresor": tresor, "Pions": pions}


def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
    paramètre: c une carte
    """
    return sum(c["Mur"]) < 3


def murNord(c):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    return c["Mur"][0]


def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    return c["Mur"][2]


def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    return c["Mur"][1]


def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    return c["Mur"][3]


def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return c["Pions"]


def setListePions(c, listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    c["Pions"] = listePions


def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    return len(c["Pions"])


def possedePion(c, pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    """
    return pion in c["Pions"]


def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return c["Tresor"]


def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res = c["Tresor"]
    c["Tresor"] = 0
    return res


def mettreTresor(c, tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res = c["Tresor"]
    c["Tresor"] = tresor
    return res


def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion in c["Pions"]:
        c["Pions"].remove(pion)


def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion not in c["Pions"]:
        c["Pions"].append(pion)


def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    (nord, est, sud, ouest) = c["Mur"]
    c["Mur"] = (ouest, nord, est, sud)


def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    (nord, est, sud, ouest) = c["Mur"]
    c["Mur"] = (est, sud, ouest, nord)


def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    for i in range(random.randint(1, 4)):
        tournerHoraire(c)


def coderMurs(c):
    """
    code les murs sous la forme d'un entier dont le codage binaire 
    est de la forme bNbEbSbO où bN, bE, bS et bO valent 
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'code du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre c une carte
    retourne un entier code du caractère semi-graphique de la carte
    """
    res = 0
    for i in range(4):
        if c["Mur"][i]:
            res += 2 ** i
    return res


def decoderMurs(c, code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    res = []
    for i in reversed(range(4)):
        if code - 2 ** i >= 0:
            code -= 2 ** i
            res.append(True)
        elif code - 2 ** i < 0:
            res.append(False)
    c["Mur"] = (res[3], res[2], res[1], res[0])


def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    # listeCartes = ['╬', '╦', '╣', '╗', '╩', '═', '╝', 'Ø', '╠', '╔', '║', 'Ø', '╚', 'Ø', 'Ø', 'Ø']
    # {"Mur": (nord, est, sud, ouest), "Tresor": tresor, "Pions": pions}
    return listeCartes[coderMurs(c)]


def char_to_carte(char):
    """
    renvoie la valeur associer au caractère semi graphique
    paramètres char un caractère semi graphique
    """
    ok = False
    code = 0
    while code < len(listeCartes) and not ok:  # code = indice du caractère semi graphique
        if char == listeCartes[code]:
            ok = True
            code -= 1
        code += 1
    carte = Carte(False, False, False, False)
    decoderMurs(carte, code)
    return carte  # char_to_carte('╦') = {'Mur': (True, False, False, False), 'Tresor': 0, 'Pions': []}


def passageNord(carte1, carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    return not (carte1["Mur"][0] or carte2["Mur"][2])


def passageSud(carte1, carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    return not (carte1["Mur"][2] or carte2["Mur"][0])


def passageOuest(carte1, carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    return not (carte1["Mur"][3] or carte2["Mur"][1])


def passageEst(carte1, carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen    
    """
    return not (carte1["Mur"][1] or carte2["Mur"][3])
