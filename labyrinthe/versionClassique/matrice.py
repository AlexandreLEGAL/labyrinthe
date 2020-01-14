# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module matrice
   ~~~~~~~~~~~~~~~
   
   Ce module gère une matrice. 
"""


# -----------------------------------------
# contructeur et accesseurs
# -----------------------------------------

def Matrice(nbLignes, nbColonnes, valeurParDefaut=0):
    """
    crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant 
    valeurParDefaut dans chacune des cases
    paramètres: 
      nbLignes un entier strictement positif qui indique le nombre de lignes
      nbColonnes un entier strictement positif qui indique le nombre de colonnes
      valeurParDefaut la valeur par défaut
    résultat la matrice ayant les bonnes propriétés
    """
    val = []
    for i in range(nbLignes):
        val += [[valeurParDefaut] * nbColonnes]
    return {"Ligne": nbLignes, "Colonne": nbColonnes, "Val": val}


def getNbLignes(matrice):
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    return matrice["Ligne"]


def getNbColonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    return matrice["Colonne"]


def getVal(matrice, ligne, colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    return matrice["Val"][ligne][colonne]


def setVal(matrice, ligne, colonne, valeur):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cette fonction ne retourne rien mais modifie la matrice
    """
    matrice["Val"][ligne][colonne] = valeur


def afficheMatrice(mat):
    for i in range(getNbLignes(mat)):
        li = ''
        for j in mat['Val'][i]:
            li += (str(j) + " |").rjust(5)
        print(li)
        print('-' * 7 * 5)


# ------------------------------------------
# decalages
# ------------------------------------------


def decalageLigneAGauche(matrice, numLig, nouvelleValeur=0):
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """
    res = matrice["Val"][numLig][0]
    matrice["Val"][numLig] = matrice["Val"][numLig][1:] + [nouvelleValeur]
    return res


def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    res = matrice["Val"][numLig][-1]
    matrice["Val"][numLig] = [nouvelleValeur] + matrice["Val"][numLig][:-2]  #  modifie au lieu de -1
    return res


def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    res = matrice['Val'][0][numCol]
    for i in range(getNbLignes(matrice) - 1):
        setVal(matrice, i, numCol, getVal(matrice, i + 1, numCol))
    setVal(matrice, getNbLignes(matrice) - 1, numCol, nouvelleValeur)
    return res


def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    res = matrice['Val'][-1][numCol]
    for i in range(getNbLignes(matrice) - 1, 0, -1):
        setVal(matrice, i, numCol, getVal(matrice, i - 1, numCol))
    setVal(matrice, 0, numCol, nouvelleValeur)
    return res
