#! /usr/bin/env python3

""" Implémentation des parcours de l’arbre de calculs à la volée :
- parcours en profondeur d’abord itératif
- parcours en profondeur d’abord récursif
- parcours en largeur d’abord itératif """

from TAD.piles_listes_python import Pile
#from TAD.files_listes_python import File
#from TAD.piles_listes_simplement_chainees import Pile
from TAD.files_listes_doublement_chainees import File
from notation_polonaise_inverse import *

operations = ['+', '-', '*', '/']
def parcours_DFS(cartons, cible) : 
    # cartons : une liste
    # cible : entier 
    nb_noeuds=0
    meilleure_expression = []
    ecart_min=cible
    pile_suiv=operations+cartons.copy()
    meilleure_expression_suiv=[0,0,0,0,0,0,0,0,0,0,0]
    k=0
    possibles =[[[],cartons.copy()]]
    while len(possibles)>0:
        match possibles.pop():
            case [expr_a_tester,restants_a_tester]:
                for i in range (len(restants_a_tester)):
                    nb_noeuds+=1
                    test=expr_a_tester + [restants_a_tester[i]]
                    resultat=eval_NPI_liste(test, afficher = False)
                    if resultat[0] and not resultat[1]==None:
                        if abs(resultat[1]-cible)<ecart_min:
                            ecart_min=abs(resultat[1]-cible)
                            meilleure_expression=test
                    if resultat[0]:
                        possibles.append ([test,restants_a_tester[:i]+restants_a_tester[i+1:]])

                test=expr_a_tester + ["-"]
                resultat=eval_NPI_liste(test, afficher = False)
                if resultat[0] and not resultat[1]==None:
                    if abs(resultat[1]-cible)<ecart_min:
                        ecart_min=abs(resultat[1]-cible)
                        meilleure_expression=test
                if resultat[0]:
                    possibles.append ([test,restants_a_tester])
                nb_noeuds+=4

                test=expr_a_tester + ["/"]
                resultat=eval_NPI_liste(test, afficher = False)
                if resultat[0] and not resultat[1]==None:
                    if abs(resultat[1]-cible)<ecart_min:
                        ecart_min=abs(resultat[1]-cible)
                        meilleure_expression=test
                if resultat[0]:
                    possibles.append ([test,restants_a_tester])
                        
                test=expr_a_tester + ["+"]
                resultat=eval_NPI_liste(test, afficher = False)
                if resultat[0] and not resultat[1]==None:
                    if abs(resultat[1]-cible)<ecart_min:
                        ecart_min=abs(resultat[1]-cible)
                        meilleure_expression=test
                if resultat[0]:
                    possibles.append ([test,restants_a_tester])

                test=expr_a_tester + ["*"]
                resultat=eval_NPI_liste(test, afficher = False)
                if resultat[0] and not resultat[1]==None:
                    if abs(resultat[1]-cible)<ecart_min:
                        ecart_min=abs(resultat[1]-cible)
                        meilleure_expression=test
                if resultat[0]:
                    possibles.append ([test,restants_a_tester])
                print(meilleure_expression)
                if ecart_min==0:
                    print ("Cible atteinte",nb_noeuds)
                    return (meilleure_expression,nb_noeuds)
    return meilleure_expression

def parcours_BFS(cartons, cible) : 
    # cartons : une liste
    # cible : entier 
    nb_noeuds = 0
    meilleure_expression = []
    ecart_min=cible
    pile_suiv=operations+cartons.copy()
    meilleure_expression_suiv=[0,0,0,0,0,0,0,0,0,0,0]
    k=0
    possibles =[[[],cartons.copy()]]
    while len(possibles)>0:
        match possibles.pop():
            case [expr_a_tester,restants_a_tester]:
                for i in range (len(restants_a_tester)):
                    test=expr_a_tester + [restants_a_tester[i]]
                    resultat=eval_NPI_liste(test, afficher = False)
                    if resultat[0] and not resultat[1]==None:
                        if abs(resultat[1]-cible)<ecart_min:
                            ecart_min=abs(resultat[1]-cible)
                            meilleure_expression=test
                    if resultat[0]:
                        possibles.append ([test,restants_a_tester[:i]+restants_a_tester[i+1:]])

                test=expr_a_tester + ["-"]
                resultat=eval_NPI_liste(test, afficher = False)
                if resultat[0] and not resultat[1]==None:
                    if abs(resultat[1]-cible)<ecart_min:
                        ecart_min=abs(resultat[1]-cible)
                        meilleure_expression=test
                if resultat[0]:
                    possibles.append ([test,restants_a_tester])

                test=expr_a_tester + ["/"]
                resultat=eval_NPI_liste(test, afficher = False)
                if resultat[0] and not resultat[1]==None:
                    if abs(resultat[1]-cible)<ecart_min:
                        ecart_min=abs(resultat[1]-cible)
                        meilleure_expression=test
                if resultat[0]:
                    possibles.append ([test,restants_a_tester])
                        
                test=expr_a_tester + ["+"]
                resultat=eval_NPI_liste(test, afficher = False)
                if resultat[0] and not resultat[1]==None:
                    if abs(resultat[1]-cible)<ecart_min:
                        ecart_min=abs(resultat[1]-cible)
                        meilleure_expression=test
                if resultat[0]:
                    possibles.append ([test,restants_a_tester])

                test=expr_a_tester + ["*"]
                resultat=eval_NPI_liste(test, afficher = False)
                if resultat[0] and not resultat[1]==None:
                    if abs(resultat[1]-cible)<ecart_min:
                        ecart_min=abs(resultat[1]-cible)
                        meilleure_expression=test
                if resultat[0]:
                    possibles.append ([test,restants_a_tester])
                print(meilleure_expression)
                if ecart_min==0:
                    print ("Cible atteinte")
                    return meilleure_expression
    meilleure_expression = []


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
    parcours_DFS([5, 25, 7, 9, 3, 50], 859)
    #parcours_BFS([3,5, 7, 9, 25, 50], 859)
    #parcours_DFS_recursif([3,5, 7, 9, 25, 50], 859)

