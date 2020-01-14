# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans

   Module plateau
   ~~~~~~~~~~~~~~

   Ce module gère le plateau de jeu.
"""
import random
from matrice import *
from carte import *


def Plateau(nbJoueurs, nbTresors):
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: un couple contenant
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """
    if 12 <= nbTresors <= 45 and 1 <= nbJoueurs <= 4:
        for carte in listeCartes:  # modifie la liste de carte pour ne pas avoir formation de mur impossible
            if carte == "Ø":
                listeCartes.remove(carte)
        semi_plateau = Matrice(7, 7)
        # listeCartes_mur = [] # FACTORISER LA FONCTION
        # for carte in listeCartes:
        #
        # afficheMatrice(semi_plateau)
        ## Créer une matrice vide, ajouter les cartes fixes et les pions
        liste_joueur = [[], [], [], []]
        for i in range(nbJoueurs):
            liste_joueur[i].append(i + 1)
        # print("liste_joueur = " + str(liste_joueur))
        setVal(semi_plateau, 0, 0, Carte(True, False, False, True, 0, liste_joueur[0]))
        setVal(semi_plateau, 0, 6, Carte(True, False, False, False, 0, liste_joueur[1]))
        setVal(semi_plateau, 6, 0, Carte(True, False, False, False, 0, liste_joueur[2]))
        setVal(semi_plateau, 6, 6, Carte(True, True, False, False, 0, liste_joueur[3]))
        carte_fixe_sans_angles = [{"Mur": (True, False, False, False), "Tresor": 1, "Pions": []},
                                  {"Mur": (True, False, False, False), "Tresor": 2, "Pions": []},
                                  {"Mur": (False, True, False, False), "Tresor": 3, "Pions": []},
                                  {"Mur": (False, True, False, False), "Tresor": 4, "Pions": []},
                                  {"Mur": (True, False, False, False), "Tresor": 5, "Pions": []},
                                  {"Mur": (False, False, False, True), "Tresor": 6, "Pions": []},
                                  {"Mur": (False, True, False, False), "Tresor": 7, "Pions": []},
                                  {"Mur": (False, False, True, False), "Tresor": 8, "Pions": []},
                                  {"Mur": (True, False, False, True), "Tresor": 9, "Pions": []},
                                  {"Mur": (True, False, False, True), "Tresor": 10, "Pions": []},
                                  {"Mur": (False, False, True, False), "Tresor": 11, "Pions": []},
                                  {"Mur": (False, False, True, False), "Tresor": 12, "Pions": []},
                                  ]
        indice = 0
        for i in range(0, getNbLignes(semi_plateau), 2):
            if i == 0 or i == 6:
                for j in range(2, 5, 2):
                    # print(indice)
                    setVal(semi_plateau, i, j, carte_fixe_sans_angles[indice])
                    indice += 1
            else:
                for j in range(0, 7, 2):
                    # print(indice)
                    setVal(semi_plateau, i, j, carte_fixe_sans_angles[indice])
                    indice += 1

        # setVal(semi_plateau, 0, 2, Carte(True, False, False, True, 1))
        # setVal(semi_plateau, 0, 4, Carte(True, False, False, False, 2))
        #
        # setVal(semi_plateau, 2, 0, Carte(True, False, False, False, 3))
        # setVal(semi_plateau, 2, 2, Carte(True, True, False, False, 4))
        # setVal(semi_plateau, 2, 4, Carte(True, False, False, True, 5))
        # setVal(semi_plateau, 2, 6, Carte(True, False, False, False, 6))
        #
        # setVal(semi_plateau, 4, 0, Carte(True, False, False, False, 7))
        # setVal(semi_plateau, 4, 2, Carte(True, True, False, False, 8))
        # setVal(semi_plateau, 4, 4, Carte(True, False, False, True, 9))
        # setVal(semi_plateau, 4, 6, Carte(True, False, False, False, 10))
        #
        # setVal(semi_plateau, 6, 2, Carte(True, True, False, False, 11))
        # setVal(semi_plateau, 6, 4, Carte(True, False, False, True, 12))

        # print("semi_plateau = " + str(semi_plateau))

        ## ensuite la ou les valeurs de la matrice = 0 mettre des cartes amovible préalablement créer

        # créer une liste de carte amovible

        carte_amovible = []  # 6 jonction, 16 angles, 12 droit
        murAngle = Carte(True, False, False, True)
        murJonction = Carte(True, False, False, False)
        murDroit = Carte(True, False, True, False)
        for i in range(16):  #  On ajoute 16 angles tourner aléatoirement dans carte_amovible
            tourneAleatoire(murAngle)
            carte_amovible.append(murAngle.copy())
        for i in range(6):  #  On ajoute 6 jonction tourner aléatoirement dans carte_amovible
            tourneAleatoire(murJonction)
            carte_amovible.append(murJonction.copy())
        for i in range(12):  #  On ajoute 12 droit tourner aléatoirement dans carte_amovible
            tourneAleatoire(murDroit)
            carte_amovible.append(murDroit.copy())

        # Mélanger les carte amovible

        random.shuffle(carte_amovible)  # On mélange toute les cartes amovibles
        # print("carte_amovible = " + str(carte_amovible))

        # Mettre des trésors dans les premières cartes

        for i in range(nbTresors - 12):  # On met des trésors dans les nbTresors premières carte puis on remélange
            mettreTresor(carte_amovible[i], i + 13)  # i+13 car les trésor de 1 à 12 sont placé sur les carte fixes
        # print("carte_amovible = " + str(carte_amovible))

        # Mélanger

        random.shuffle(carte_amovible)
        # print("carte_amovible avec tresor melanger = " + str(carte_amovible))

        # Placer les cartes amovibles dans le plateau

        for i in range(getNbLignes(semi_plateau)):
            nord = carte_amovible[0]["Mur"][0]
            est = carte_amovible[0]["Mur"][1]
            sud = carte_amovible[0]["Mur"][2]
            ouest = carte_amovible[0]["Mur"][3]
            if i % 2 == 0:
                for j in range(1, getNbColonnes(semi_plateau), 2):
                    setVal(semi_plateau, i, j, Carte(nord, est, sud, ouest, carte_amovible[0]["Tresor"]))
                    carte_amovible.pop(0)
                    # print("carte_amovible = " + str(carte_amovible))
            else:
                for j in range(getNbColonnes(semi_plateau)):
                    setVal(semi_plateau, i, j, Carte(nord, est, sud, ouest, carte_amovible[0]["Tresor"]))
                    carte_amovible.pop(0)
                    # print("carte_amovible = " + str(carte_amovible))
        # print("semi_plateau avec carte amovible = " + str(semi_plateau))
        return semi_plateau, carte_amovible[0]


def creerCartesAmovibles(tresorDebut, nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    aléatoirement nbTresor trésors
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    résultat: la liste mélangée aléatoirement des cartes amovibles créees
    """
    pass


def prendreTresorPlateau(plateau, lig, col, numTresor):
    """
    prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """
    pass


def getCoordonneesTresor(plateau, numTresor):
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """
    pass


def getCoordonneesJoueur(plateau, numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    pass


def prendrePionPlateau(plateau, lin, col, numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    pass


def poserPionPlateau(plateau, lin, col, numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    pass


def accessible(plateau, ligD, colD, ligA, colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """
    pass


def accessibleDist(plateau, ligD, colD, ligA, colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
    mais la valeur de retour est None s'il n'y a pas de chemin, 
    sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
    de coordonées (couple de (lig,col))
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: une liste de coordonées indiquant un chemin possible entre la case
              de départ et la case d'arrivée
    """
    pass
