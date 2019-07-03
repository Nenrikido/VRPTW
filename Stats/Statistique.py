"""
    Calcul des statistiques descriptive sur un echantillon de plusieurs test avec les mêmes paramètre de départ
"""
import math
import json


def calcul_moyenne(liste):
    """

        :param liste: liste de nos temps de convergence
        :return: moyenne des temps de convergence
    """

    x = 0
    for f in liste:
        x += f
    x = x / len(liste)
    return round(x, 2)


def calcul_mediane(liste):
    """

        :param liste: liste de nos temps de convergence
        :return: mediane des temps de convergence
    """

    liste = sorted(liste)
    l_len = len(liste)
    if l_len < 1:
        return None
    if l_len % 2 == 0:
        v1 = int(l_len / 2)
        v2 = int(l_len / 2)
        return (liste[v1 - 1] + liste[v2]) / 2
    else:
        return liste[int((l_len - 1) / 2)]


def minimum_value(liste):
    """

        :param liste: liste de nos temps de convergence
        :return: borne inférieur des temps de convergence
    """

    liste = sorted(liste)
    return liste[0]


def maximum_value(liste):
    """

        :param liste: liste de nos temps de convergence
        :return: borne supérieur des temps de convergence
    """
    liste = sorted(liste)
    return liste[len(liste) - 1]


def premier_quartile(liste):
    """

        :param liste: liste de nos temps de convergence
        :return: premier des quartiles des temps de convergence
    """
    v1 = math.ceil(len(liste) * 0.25)
    return liste[v1 - 1]


def troisieme_quartile(liste):
    """

        :param liste: liste de nos temps de convergence
        :return: troisieme des quartiles des temps de convergence
    """
    v1 = math.ceil(len(liste) * 0.75)
    return liste[v1 - 1]


def calcul_etendue(liste):
    """

        :param liste: liste de nos temps de convergence
        :return: étendue des temps de convergence
    """
    return round(maximum_value(liste) - minimum_value(liste), 2)


file = open("statEchantillonGreedySansContrainte.json", "r")
obj = json.load(file)

# Affichage des statistiques descriptives
print("Echantillon de 25 tests avec 1000 Villes de départ")
print("Moyenne : " + str(calcul_moyenne(obj)) + " secondes")
print("Mediane : " + str(calcul_mediane(obj)) + " secondes")
print("Minimum value : " + str(minimum_value(obj)) + " secondes")
print("Maximum value : " + str(maximum_value(obj)) + " secondes")
print("Premier quartile : " + str(premier_quartile(obj)) + " secondes")
print("Troisieme quartile : " + str(troisieme_quartile(obj)) + " secondes")
print("Etendue : " + str(calcul_etendue(obj)) + " secondes")
