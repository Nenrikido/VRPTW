""""
    Lance notre algorithme de recherche de chemin x fois avec a chaque fois un nombre différent de ville de départ
    On exportera nos temps de convergence dans un JSON
"""

import time
import json
import sys
import subprocess

# Création des différent échantillon de départ que nous allons utiliser
echantillion = list(range(50, 1000, 10))
data = []

# On execute le programme pour chaque echantillon
for f in echantillion:
    # On défini un resultat null au départ
    result = False
    print(f"Essaie pour un echantillon de {f} villes : ")
    # Tant qu'on n'a pas de résultat
    while not result:
        # On note le temps avant execution de l'algorithme
        t1 = time.time()
        print("Lancement de l'algo")
        try:
            # On lance notre algorithme avec en paramètre la taille de l'échantillon de ville de départ
            output = subprocess.check_output(["python", "main.py", str(f), "20"], timeout=35)
        # On gère ici les exeptions
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:
            print("Timeouted", file=sys.stderr)
            output = ""
        # On note le temps après l'éxecution de l'algorithme
        t2 = time.time()
        print("Analyse du résultat")
        # On vérifie si on a bien un résultat et si donc l'algorithme a trouver un chemin
        result = len(output) > 0
        print("La répons est " + str(result))
        # Si on a eu un resultat on continue sinon on relance l'algorithme
        if result:
            # On mesure la différence de temps qui est le temps d'éxecution de notre algorithme
            solution = output.split(b"The sum of all vehicle's travel duration is : ")[1].split(b"\r\n")[0]
            solution = str(solution)[2:-1]
            iteration = output.split(b"The amount of iterations is : ")[1].split(b"\r\n")[0]
            iteration = str(iteration)[2:-1]
            print(f"Solution : " + solution + " heures")
            print(f"Solution : " + iteration + " iteration")
            timeF = round(t2 - t1, 2)
            print("Le temps de résolution est de : " + str(timeF) + " seconde(s)")
            # On note le temps de convergence pour la taille de l'échantillon dans une liste
            data.append([f, timeF,solution,20,iteration])
            # On écrit la liste dans un JSON
            json.dump(data, open('dataGreedyAvecContrainte.json', 'w'))
