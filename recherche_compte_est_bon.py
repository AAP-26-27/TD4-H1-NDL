#! /usr/bin/env python3

""" Implémentation des parcours de l’arbre de calculs à la volée :
- parcours en profondeur d’abord itératif
- parcours en profondeur d’abord récursif
- parcours en largeur d’abord itératif """

from TAD.piles_listes_python import Pile
from TAD.files_listes_python import File
from TAD.piles_listes_simplement_chainees import Pile
from TAD.files_listes_doublement_chainees import File
from notation_polonaise_inverse import *

operations = ['+', '-', '*', '/']

def suppr(L,elt):
    B=L.copy()
    B.pop(elt)
    return B


def parcours_DFS(cartons, cible) : 
    # cartons : une liste
    # cible : entier 
    nb_noeuds = 0
    meilleure_expression = []
    meilleur_tot=0
    ecart_min=cible
    atteint=False
    suiv=operations+cartons.copy()
    iterate=0
    while not atteint and iterate<11:
        meilleure_expression_suiv=meilleure_expression
        for carac in suiv:
            a_tester=meilleure_expression + carac
            resultat=eval_NPI_liste(a_tester, afficher = False)
            if resultat[0] and abs(resultat[1]-cible)<ecart_min:
                ecart_min=abs(resultat[1]-cible)
                meilleure_expression.append(resultat[1])


        

    return meilleure_expression, nb_noeuds

def parcours_BFS(cartons, cible) : 
    # cartons : une liste
    # cible : entier 
    nb_noeuds = 0
    meilleure_expression = []

    return meilleure_expression, nb_noeuds 

def parcours_DFS_recursif(cartons, cible) :
    meilleure_expression = []
    nb_noeuds = 0

    def parcours_DFSR_aux(choisis, restants) :
        nonlocal meilleure_expression
        nonlocal nb_noeuds
        nonlocal cible
        pass
        
    # Appeler parcours_DFSR_aux ! 

    return meilleure_expression, nb_noeuds


if __name__ == "__main__":
    parcours_DFS([3,5, 7, 9, 25, 50], 859)
    parcours_BFS([3,5, 7, 9, 25, 50], 859)
    parcours_DFS_recursif([3,5, 7, 9, 25, 50], 859)

