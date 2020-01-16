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
from copy import deepcopy


def Plateau(nbJoueurs, nbTresors):
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: une structure contenant
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
        # # print("liste_joueur = " + str(liste_joueur))
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
                    # # print(indice)
                    setVal(semi_plateau, i, j, carte_fixe_sans_angles[indice])
                    indice += 1
            else:
                for j in range(0, 7, 2):
                    # # print(indice)
                    setVal(semi_plateau, i, j, carte_fixe_sans_angles[indice])
                    indice += 1

        # # print("semi_plateau = " + str(semi_plateau))

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
        # # print("carte_amovible = " + str(carte_amovible))

        # Mettre des trésors dans les premières cartes

        for i in range(nbTresors - 12):  # On met des trésors dans les nbTresors premières carte puis on remélange
            mettreTresor(carte_amovible[i], i + 13)  # i+13 car les trésor de 1 à 12 sont placé sur les carte fixes
        # # print("carte_amovible = " + str(carte_amovible))

        # Mélanger

        random.shuffle(carte_amovible)
        # # print("carte_amovible avec tresor melanger = " + str(carte_amovible))

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
                    # # print("carte_amovible = " + str(carte_amovible))
            else:
                for j in range(getNbColonnes(semi_plateau)):
                    setVal(semi_plateau, i, j, Carte(nord, est, sud, ouest, carte_amovible[0]["Tresor"]))
                    carte_amovible.pop(0)
                    # # print("carte_amovible = " + str(carte_amovible))
        # # print("semi_plateau avec carte amovible = " + str(semi_plateau))
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
        mettreTresor(carte_amovible[i],
                     i + 13 + tresorDebut)  # i+13 car les trésor de 1 à 12 sont placé sur les carte fixes
    # print("carte_amovible = " + str(carte_amovible))

    # Mélanger

    random.shuffle(carte_amovible)
    return carte_amovible


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
    trouver = False
    if getVal(plateau[0], lig, col)["Tresor"] == numTresor:
        trouver = True
    return trouver


def getCoordonneesTresor(plateau, numTresor):
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """
    res = None
    # print(plateau)
    for i in range(getNbLignes(plateau[0])):
        for j in range(getNbColonnes(plateau[0])):
            if getTresor(getVal(plateau[0], i, j)) == numTresor:
                res = i, j
    return res


def getCoordonneesJoueur(plateau, numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    res = None
    for i in range(getNbLignes(plateau[0])):
        for j in range(getNbColonnes(plateau[0])):
            if possedePion(getVal(plateau[0], i, j), numJoueur):
                res = i, j
    return res


def prendrePionPlateau(plateau, lin, col, numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    # print(getVal(plateau[0], lin, col))
    prendrePion(plateau[0]["Val"][lin][col], numJoueur)
    # print(getVal(plateau[0], lin, col))


def poserPionPlateau(plateau, lin, col, numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    poserPion(plateau[0]["Val"][lin][col], numJoueur)


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
    trouver = False
    case_parcouru = 0
    liste_chemin = [(ligD, colD)]
    # print(liste_chemin)
    cpt = 0
    indice_chemin = []
    while case_parcouru < 49 and not trouver:
        if len(
                liste_chemin) > 1:  # Pour tout les autre déplacements ajoute les différents chemins possible dans liste_chemin
            cpt = 0
            for indice in indice_chemin:  # len(liste_chemin)-cpt, len(liste_chemin)-1 ## 1, nbchemin * 2, 2
                # for chemin_poss in range(1, nbchemin * 2, 2):
                nb = 0
              # print("nb" + str(nb))
                if 0 <= liste_chemin[indice][0] - 1 < 7:
                    if passageNord(getVal(plateau[0], liste_chemin[indice][0], liste_chemin[indice][1]),
                                   getVal(plateau[0], liste_chemin[indice][0] - 1, liste_chemin[indice][1])):
                        liste_chemin.append((liste_chemin[indice][0] - 1, liste_chemin[indice][1]))
                        cpt += 1
                        # indice_chemin.append(indice_chemin[-1] + 1)
                        nb += 1
                      # print("nb" + str(nb))
                        # print("nord")
                        # print(liste_chemin)
                if 0 <= liste_chemin[indice][1] + 1 < 7:
                    if passageEst(getVal(plateau[0], liste_chemin[indice][0], liste_chemin[indice][1]),
                                  getVal(plateau[0], liste_chemin[indice][0], liste_chemin[indice][1] + 1)):
                        liste_chemin.append((liste_chemin[indice][0], liste_chemin[indice][1] + 1))
                        cpt += 1
                        # indice_chemin.append(indice_chemin[-1] + 1)
                        nb += 1
                      # print("nb" + str(nb))
                        # print("est")
                        # print(liste_chemin)
                if 0 <= liste_chemin[indice][0] + 1 < 7:
                    if passageSud(getVal(plateau[0], liste_chemin[indice][0], liste_chemin[indice][1]),
                                  getVal(plateau[0], liste_chemin[indice][0] + 1, liste_chemin[indice][1])):
                        liste_chemin.append((liste_chemin[indice][0] + 1, liste_chemin[indice][1]))
                        cpt += 1
                        # indice_chemin.append(indice_chemin[-1] + 1)
                        nb += 1
                      # print("nb" + str(nb))
                        # print("Sud")
                        # print(liste_chemin)
                if 0 <= liste_chemin[indice][1] - 1 < 7:
                    if passageOuest(getVal(plateau[0], liste_chemin[indice][0], liste_chemin[indice][1]),
                                    getVal(plateau[0], liste_chemin[indice][0], liste_chemin[indice][1] - 1)):
                        liste_chemin.append((liste_chemin[indice][0], liste_chemin[indice][1] - 1))
                        cpt += 1
                        # indice_chemin.append(indice_chemin[-1] + 1)
                        nb += 1
                      # print("nb" + str(nb))
                        # print("ouest")
                        # print(liste_chemin)
                # # print(case_parcouru)
                case_parcouru += 1
                if (ligA, colA) in liste_chemin:
                    trouver = True
                # print("indice_chemin" + str(indice_chemin))
                for elem in range(nb):
                    indice_chemin.append(indice_chemin[-1] + 1)
              # print("indice_chemin après append" + str(indice_chemin))
                for elem in range(nb):
                    indice_chemin.pop(0)
                  # print("indice_chemin après pop" + str(indice_chemin))
                    # print(liste_chemin)
                    # print(cpt)
                    # print(case_parcouru)
        elif len(
                liste_chemin) == 1:  # Pour le premier déplacement ajoute les différents chemins possible dans liste_chemin
            if 0 <= ligD - 1 < 7:
                if passageNord(getVal(plateau[0], ligD, colD), getVal(plateau[0], ligD - 1, colD)):
                    liste_chemin.append((ligD - 1, colD))
                    cpt += 1
                    indice_chemin.append(cpt)
            if 0 <= colD + 1 < 7:
                if passageEst(getVal(plateau[0], ligD, colD), getVal(plateau[0], ligD, colD + 1)):
                    liste_chemin.append((ligD, colD + 1))
                    cpt += 1
                    indice_chemin.append(cpt)
            if 0 <= ligD + 1 < 7:
                if passageSud(getVal(plateau[0], ligD, colD), getVal(plateau[0], ligD + 1, colD)):
                    liste_chemin.append((ligD + 1, colD))
                    cpt += 1
                    indice_chemin.append(cpt)
            if 0 <= colD - 1 < 7:
                if passageOuest(getVal(plateau[0], ligD, colD), getVal(plateau[0], ligD, colD - 1)):
                    liste_chemin.append((ligD, colD - 1))
                    cpt += 1
                    indice_chemin.append(cpt)
            case_parcouru = +1

            # print(liste_chemin)
            # print(cpt)
            # print(case_parcouru)
            # print(indice_chemin)
        if len(liste_chemin) == 1:  # Si il n'y a pas de chemin à partir de la case de départ retourne None
            case_parcouru = 50
    return trouver


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
    trouver = None
    case_parcouru = 0
    liste_chemin = [[(ligD, colD)]]
    # print(liste_chemin)
    cpt = 0
    nb = 0
    indice_chemin = []
    while case_parcouru < 49 and trouver is None:
        if len(
                liste_chemin) > 1:  # Pour tout les autre déplacements ajoute les différents chemins possible dans liste_chemin
            cpt = 0
            # print("avant  = " + str(indice_chemin))
            avant = len(indice_chemin)
            # print("avant  = " + str(avant))
            for indice in indice_chemin:  # len(liste_chemin)-cpt, len(liste_chemin)-1 ## 1, nbchemin * 2, 2
                # for chemin_poss in range(1, nbchemin * 2, 2):
                # print("nb" + str(nb))
                if 0 <= liste_chemin[indice][-1][0] - 1 < 7:
                    if passageNord(getVal(plateau[0], liste_chemin[indice][-1][0], liste_chemin[indice][-1][1]),
                                   getVal(plateau[0], liste_chemin[indice][-1][0] - 1, liste_chemin[indice][-1][1])):
                        liste_chemin.append(deepcopy(liste_chemin[indice]))
                        liste_chemin[-1].append((liste_chemin[indice][-1][0] - 1, liste_chemin[indice][-1][1]))
                        # liste_chemin.append((liste_chemin[indice][0] - 1, liste_chemin[indice][1]))
                        cpt += 1
                        # indice_chemin.append(indice_chemin[-1] + 1)
                        nb += 1
                        # print("Liste chemin possible = " + str(liste_chemin))
                        # print("nb" + str(nb))
                        # print("nord")
                        # print(liste_chemin)
                if 0 <= liste_chemin[indice][-1][1] + 1 < 7:
                    if passageEst(getVal(plateau[0], liste_chemin[indice][-1][0], liste_chemin[indice][-1][1]),
                                  getVal(plateau[0], liste_chemin[indice][-1][0], liste_chemin[indice][-1][1] + 1)):
                        liste_chemin.append(deepcopy(liste_chemin[indice]))
                        liste_chemin[-1].append((liste_chemin[indice][-1][0], liste_chemin[indice][-1][1] + 1))
                        # liste_chemin.append((liste_chemin[indice][0], liste_chemin[indice][1] + 1))
                        cpt += 1
                        # indice_chemin.append(indice_chemin[-1] + 1)
                        nb += 1
                        # print("Liste chemin possible = " + str(liste_chemin))
                        # print("nb" + str(nb))
                        # print("est")
                        # print(liste_chemin)
                if 0 <= liste_chemin[indice][-1][0] + 1 < 7:
                    if passageSud(getVal(plateau[0], liste_chemin[indice][-1][0], liste_chemin[indice][-1][1]),
                                  getVal(plateau[0], liste_chemin[indice][-1][0] + 1, liste_chemin[indice][-1][1])):
                        liste_chemin.append(deepcopy(liste_chemin[indice]))
                        liste_chemin[-1].append((liste_chemin[indice][-1][0] + 1, liste_chemin[indice][-1][1]))
                        # liste_chemin.append((liste_chemin[indice][0] + 1, liste_chemin[indice][1]))
                        cpt += 1
                        # indice_chemin.append(indice_chemin[-1] + 1)
                        nb += 1
                        # print("Liste chemin possible = " + str(liste_chemin))
                        # print("nb" + str(nb))
                        # print("Sud")
                        # print(liste_chemin)
                if 0 <= liste_chemin[indice][-1][1] - 1 < 7:
                    if passageOuest(getVal(plateau[0], liste_chemin[indice][-1][0], liste_chemin[indice][-1][1]),
                                    getVal(plateau[0], liste_chemin[indice][-1][0], liste_chemin[indice][-1][1] - 1)):
                        liste_chemin.append(deepcopy(liste_chemin[indice]))
                        liste_chemin[-1].append((liste_chemin[indice][-1][0], liste_chemin[indice][-1][1] - 1))
                        # liste_chemin.append((liste_chemin[indice][0], liste_chemin[indice][1] - 1))
                        cpt += 1
                        # indice_chemin.append(indice_chemin[-1] + 1)
                        nb += 1
                        # print("Liste chemin possible = " + str(liste_chemin))
                        # print("nb" + str(nb))
                        # print("ouest")
                        # print(liste_chemin)
                # # print(case_parcouru)
                case_parcouru += 1
                for elem in liste_chemin:
                    if (ligA, colA) in elem:
                        trouver = elem
                        # trouver = "Chemin trouver ! " + str(elem)
                # print("indice_chemin" + str(indice_chemin))
            # print(nb)
            for elem in range(nb):
                indice_chemin.append(indice_chemin[-1] + 1)
            # print("indice_chemin après append" + str(indice_chemin))
            for elem in range(avant):
                indice_chemin.pop(0)
            nb = 0
            # print("indice_chemin après pop" + str(indice_chemin))
            # print("Liste chemin possible = " + str(liste_chemin))
            # print(liste_chemin)
            # trouver = True
            # print(cpt)
            # print(case_parcouru)
        elif len(
                liste_chemin) == 1:  # Pour le premier déplacement ajoute les différents chemins possible dans liste_chemin
            if 0 <= ligD - 1 < 7:
                if passageNord(getVal(plateau[0], ligD, colD), getVal(plateau[0], ligD - 1, colD)):
                    liste_chemin.append(deepcopy(liste_chemin[0]))
                    liste_chemin[-1].append((ligD - 1, colD))
                    cpt += 1
                    indice_chemin.append(cpt)
            if 0 <= colD + 1 < 7:
                if passageEst(getVal(plateau[0], ligD, colD), getVal(plateau[0], ligD, colD + 1)):
                    liste_chemin.append(deepcopy(liste_chemin[0]))
                    liste_chemin[-1].append((ligD, colD + 1))
                    cpt += 1
                    indice_chemin.append(cpt)
            if 0 <= ligD + 1 < 7:
                if passageSud(getVal(plateau[0], ligD, colD), getVal(plateau[0], ligD + 1, colD)):
                    liste_chemin.append(deepcopy(liste_chemin[0]))
                    liste_chemin[-1].append((ligD + 1, colD))
                    cpt += 1
                    indice_chemin.append(cpt)
            if 0 <= colD - 1 < 7:
                if passageOuest(getVal(plateau[0], ligD, colD), getVal(plateau[0], ligD, colD - 1)):
                    liste_chemin.append(deepcopy(liste_chemin[0]))
                    liste_chemin[-1].append((ligD, colD - 1))
                    cpt += 1
                    indice_chemin.append(cpt)
            case_parcouru = +1
            for elem in liste_chemin:
                if (ligA, colA) in elem:
                    trouver = elem
                    # trouver = "Chemin trouver ! " + str(elem)

            # print("Liste premier chemin possible = " + str(liste_chemin))
            # print(cpt)
            # print(case_parcouru)
            # print(indice_chemin)
        if len(liste_chemin) == 1:
            case_parcouru = 50
    return trouver
