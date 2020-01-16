# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module labyrinthe
   ~~~~~~~~~~~~~~~~~
   
   Ce module gère sur le jeu du labyrinthe (observation et mise à jour du jeu).
"""

from listeJoueurs import *
from plateau import *


def Labyrinthe(nomsJoueurs=["joueur1","joueurs2"],nbTresors=24, nbTresorsMax=0):
    """
    permet de créer un labyrinthe avec nbJoueurs joueurs, nbTresors trésors
    chacun des joueurs aura au plus nbTresorMax à trouver
    si ce dernier paramètre est à 0, on distribuera le maximum de trésors possible 
    à chaque joueur en restant équitable
    un joueur courant est choisi et la phase est initialisée
    paramètres: nomsJoueurs est la liste des noms des joueurs participant à la partie (entre 1 et 4)
                nbTresors le nombre de trésors différents il en faut au moins 12 et au plus 49
                nbTresorMax le nombre de trésors maximum distribué à chaque joueur
    résultat: le labyrinthe crée
    """
    labyrinthe={}
    labyrinthe["Plateau"]=Plateau(len(nomsJoueurs),nbTresors)
    labyrinthe["Joueurs"]=ListeJoueurs(nomsJoueurs)
    distribuerTresors(labyrinthe["Joueurs"],nbTresors,nbTresorsMax)
    labyrinthe["Phase"]=1
    labyrinthe["CoupAvant"]=(None,None)
    return labyrinthe

def getPlateau(labyrinthe):
    """
    retourne la matrice représentant le plateau de jeu
    paramètre: labyrinthe le labyrinthe considéré
    résultat: la matrice représentant le plateau de ce labyrinthe
    """
    return labyrinthe["Plateau"]

def getNbParticipants(labyrinthe):
    """
    retourne le nombre de joueurs engagés dans la partie
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de joueurs de la partie
    """
    return len(labyrinthe["Joueurs"])

def getNomJoueurCourant(labyrinthe):
    """
    retourne le nom du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nom du joueurs courant
    """
    return nomJoueurCourant(labyrinthe["Joueurs"])

def getNumJoueurCourant(labyrinthe):
    """
    retourne le numero du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numero du joueurs courant
    """
    return numJoueurCourant(labyrinthe["Joueurs"])

def getPhase(labyrinthe):
    """
    retourne la phase du jeu courante
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numéro de la phase de jeu courante
    """   
    return labyrinthe["Phase"]


def changerPhase(labyrinthe):
    """
    change de phase de jeu en passant la suivante
    paramètre: labyrinthe le labyrinthe considéré
    la fonction ne retourne rien mais modifie le labyrinthe
    """    
    if labyrinthe["Phase"]==1:
        labyrinthe["Phase"]=2
    else:
        labyrinthe["Phase"]=1


def getNbTresors(labyrinthe):
    """
    retourne le nombre de trésors qu'il reste sur le labyrinthe
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de trésors sur le plateau
    """
    res=0
    listerand = []
    for i in range(0, 7):
        for j in range(0, 7):
            listerand.append((i, j))
    for (k,l) in listerand:
        dico=getVal(getPlateau(labyrinthe)[0],k,l)
        if dico["Tresor"]>0:
            res+=1
    return res

def getListeJoueurs(labyrinthe):
    """
    retourne la liste joueur structures qui gèrent les joueurs et leurs trésors
    paramètre: labyrinthe le labyrinthe considéré
    résultat: les joueurs sous la forme de la structure implémentée dans listeJoueurs.py    
    """
    return labyrinthe["Joueurs"]


def enleverTresor(labyrinthe,lin,col,numTresor):
    """
    enleve le trésor numTresor du plateau du labyrinthe. 
    Si l'opération s'est bien passée le nombre total de trésors dans le labyrinthe
    est diminué de 1
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    # print(labyrinthe['Plateau'][0]["Val"][lin][col]["Tresor"])
    prendreTresorPlateau(getPlateau(labyrinthe), lin, col, numTresor)
    # print(labyrinthe['Plateau'][0]["Val"][lin][col]["Tresor"])

def prendreJoueurCourant(labyrinthe,lin,col):
    """
    enlève le joueur courant de la carte qui se trouve sur la case lin,col du plateau
    si le joueur ne s'y trouve pas la fonction ne fait rien
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe    
    """
    print(labyrinthe['Plateau'][0]["Val"][lin][col]["Pions"])
    prendrePionPlateau(getPlateau(labyrinthe), lin, col, getJoueurCourant(getListeJoueurs(labyrinthe))['numJoueur'])
    print(labyrinthe['Plateau'][0]["Val"][lin][col]["Pions"])

def poserJoueurCourant(labyrinthe,lin,col):
    """
    pose le joueur courant sur la case lin,col du plateau
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe     
    """
    print(labyrinthe['Plateau'][0]["Val"][lin][col]["Pions"])
    poserPionPlateau(getPlateau(labyrinthe), lin, col, getJoueurCourant(getListeJoueurs(labyrinthe))['numJoueur'])
    print(labyrinthe['Plateau'][0]["Val"][lin][col]["Pions"])

def getCarteAJouer(labyrinthe):
    """
    donne la carte à jouer
    paramètre: labyrinthe: le labyrinthe considéré
    résultat: la carte à jouer    
    """    
    return getPlateau(labyrinthe)[1]

def coupInterdit(labyrinthe,direction,rangee):
    """ 
    retourne True si le coup proposé correspond au coup interdit
    elle retourne False sinon
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    résultat: un booléen indiquant si le coup est interdit ou non
    """
    res=True
    if labyrinthe["CoupAvant"][0]==rangee:
        if labyrinthe["CoupAvant"][1]=="N" and direction=="S":
            res = False
        if labyrinthe["CoupAvant"][1]=="S" and direction=="N":
            res = False
        if labyrinthe["CoupAvant"][1]=="O" and direction=="E":
            res = False
        if labyrinthe["CoupAvant"][1]=="E" and direction=="O":
            res = False
    return res

def jouerCarte(labyrinthe,direction,rangee):
    """
    fonction qui joue la carte amovible dans la direction et sur la rangée passées 
    en paramètres. Cette fonction
       - met à jour le plateau du labyrinthe
       - met à jour la carte à jouer
       - met à jour la nouvelle direction interdite
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe
    """
    while not coupInterdit(labyrinthe,direction,rangee):
        direction=input("Coup interdit. Redonnez une direction (N, S, E, O).")
        rangee=input("Coup interdit. Redonnez une rangée (1, 3, 5).")
    if direction == "N":
        carte = getVal(getPlateau(labyrinthe)[0], 0, rangee)
        carteajouer = getCarteAJouer(labyrinthe)
        carteajouer["Pions"] = carte["Pions"]
        carte["Pions"] = []
        labyrinthe["Plateau"]=(getPlateau(labyrinthe)[0],decalageColonneEnHaut(getPlateau(labyrinthe)[0],rangee,getCarteAJouer(labyrinthe)))
    if direction == "S":
        carte=getVal(getPlateau(labyrinthe)[0],6, rangee)
        carteajouer=getCarteAJouer(labyrinthe)
        carteajouer["Pions"]=carte["Pions"]
        carte["Pions"]=[]
        labyrinthe["Plateau"] = (getPlateau(labyrinthe)[0],decalageColonneEnBas(getPlateau(labyrinthe)[0], rangee, getCarteAJouer(labyrinthe)))
    if direction == "O":
        carte = getVal(getPlateau(labyrinthe)[0], rangee, 0)
        carteajouer = getCarteAJouer(labyrinthe)
        carteajouer["Pions"] = carte["Pions"]
        carte["Pions"] = []
        labyrinthe["Plateau"] = (getPlateau(labyrinthe)[0],decalageLigneAGauche(getPlateau(labyrinthe)[0], rangee, getCarteAJouer(labyrinthe)))
    if direction == "E":
        carte = getVal(getPlateau(labyrinthe)[0], rangee,6)
        carteajouer = getCarteAJouer(labyrinthe)
        carteajouer["Pions"] = carte["Pions"]
        carte["Pions"] = []
        labyrinthe["Plateau"] = (getPlateau(labyrinthe)[0],decalageLigneADroite(getPlateau(labyrinthe)[0], rangee, getCarteAJouer(labyrinthe)))
    labyrinthe["CoupAvant"] = (rangee, direction)
    changerPhase(labyrinthe)




def tournerCarte(labyrinthe,sens='H'):
    """
    tourne la carte à jouer dans le sens indiqué en paramètre (H horaire A antihoraire)
    paramètres: labyritnthe: le labyrinthe considéré
                sens: un caractère indiquant le sens dans lequel tourner la carte
     Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe    
    """
    if sens=="H":
        tournerHoraire(getCarteAJouer(labyrinthe))
    if sens=="A":
        tournerAntiHoraire(getCarteAJouer(labyrinthe))

def getTresorCourant(labyrinthe):
    """
    retourne le numéro du trésor que doit cherche le joueur courant
    paramètre: labyritnthe: le labyrinthe considéré 
    resultat: le numéro du trésor recherché par le joueur courant
    """
    if len(labyrinthe['Joueurs'][0]["tresors"]) > 0:
        return getListeJoueurs(labyrinthe)[0]["tresors"][0]
    return None

def getCoordonneesTresorCourant(labyrinthe):
    """
    donne les coordonnées du trésor que le joueur courant doit trouver
    paramètre: labyritnthe: le labyrinthe considéré 
    resultat: les coordonnées du trésor à chercher ou None si celui-ci 
              n'est pas sur le plateau
    """
    return getCoordonneesTresor(getPlateau(labyrinthe),getTresorCourant(labyrinthe))


def getCoordonneesJoueurCourant(labyrinthe):
    """
    donne les coordonnées du joueur courant sur le plateau
    paramètre: labyritnthe: le labyrinthe considéré 
    resultat: les coordonnées du joueur courant ou None si celui-ci 
              n'est pas sur le plateau
    """
    return getCoordonneesJoueur(getPlateau(labyrinthe)[0],getNumJoueurCourant(labyrinthe))


def executerActionPhase1(labyrinthe,action,rangee):
    """
    exécute une action de jeu de la phase 1
    paramètres: labyrinthe: le labyrinthe considéré
                action: un caractère indiquant l'action à effecter
                        si action vaut 'T' => faire tourner la carte à jouer
                        si action est une des lettres N E S O et
                rangee: est un des chiffre 1,3,5
                        => insèrer la carte à jouer à la direction action sur la rangée rangee
                           et faire le nécessaire pour passer en phase 2
    résultat: un entier qui vaut
              0 si l'action demandée était valide et demandait de tourner la carte
              1 si l'action demandée était valide et demandait d'insérer la carte
              2 si l'action est interdite car l'opposée de l'action précédente
              3 si action et rangee sont des entiers positifs
              4 dans tous les autres cas
    """
    if action=="T":
        sens=input("Sens horaire (H) ou anti-horaire (A) ?")
        if sens=="H":
            tournerCarte(labyrinthe,"H")
            return 0
        elif sens=="A":
            tournerCarte(labyrinthe,"A")
            return 0
        else:
            return 4
    if (rangee==1 or rangee==3 or rangee==5) and (action=="N" or action=="S" or action=="O" or action=="E"):
        print(coupInterdit(labyrinthe,action,rangee))
        if coupInterdit(labyrinthe,action,rangee):
            jouerCarte(labyrinthe, action, rangee)
            return 1
        else:
            return 2
    else:
        print(rangee, action)
        # print(coupInterdit(labyrinthe, action, rangee))
        return 3

def accessibleDistJoueurCourant(labyrinthe, ligA,colA):
    """
    verifie si le joueur courant peut accéder la case ligA,colA
    si c'est le cas la fonction retourne une liste représentant un chemin possible
    sinon ce n'est pas le cas, la fonction retourne None
    paramètres: labyrinthe le labyrinthe considéré
                ligA la ligne de la case d'arrivée
                colA la colonne de la case d'arrivée
    résultat: une liste de couples d'entier représentant un chemin que le joueur
              courant atteigne la case d'arrivée s'il existe None si pas de chemin
    """
    (x,y)=getCoordonneesJoueur(getPlateau(labyrinthe)[0],getJoueurCourant(labyrinthe["Joueurs"]))
    return accessibleDist(getPlateau(labyrinthe)[0],x,y,ligA,colA)

def finirTour(labyrinthe):
    """
    vérifie si le joueur courant vient de trouver un trésor (si oui fait le nécessaire)
    vérifie si la partie est terminée, si ce n'est pas le cas passe au joueur suivant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: un entier qui vaut
              0 si le joueur courant n'a pas trouvé de trésor
              1 si le joueur courant a trouvé un trésor mais la partie n'est pas terminée
              2 si le joueur courant a trouvé son dernier trésor (la partie est donc terminée)
    """
    if getCoordonneesTresorCourant(labyrinthe) == getCoordonneesJoueurCourant(labyrinthe):
        joueurCourantTrouveTresor(getListeJoueurs(labyrinthe))
        if nbTresorsRestantsJoueur(labyrinthe['Joueurs'],numJoueurCourant(labyrinthe['Joueurs']))==0:
            return 2
        else:
            changerPhase(labyrinthe)
            changerJoueurCourant(labyrinthe["Joueurs"])
            return 1
    else:
        changerPhase(labyrinthe)
        changerJoueurCourant(labyrinthe["Joueurs"])
        return 0
