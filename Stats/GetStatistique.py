"""
    Génere un grand nombre de temps de convergence pour des paramètres de départ similaire
    Permettant ainsi d'en faire des stats
"""
import time
import json
import sys
import subprocess

# Nombre de ville de départ
echantillon = 1000
# Nombre de test différent
iteration = 25
data = []

# On éxecute le programme x fois
for f in range(iteration):
    result = False
    print(f"Essaie pour un echantillon de " + str(echantillon) + " villes : ")
    while not result:
        # On note le temps de base
        t1 = time.time()
        print("Lancement de l'algo")
        try:
            # On lance le programme
            output = subprocess.check_output(["python", "main.py", str(echantillon), "20"], timeout=30)
        # On gère les exeptions
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:
            print("Timeouted", file=sys.stderr)
            output = ""
        # On note le temps après l'éxecution de l'algorithme
        t2 = time.time()
        print("Analyse du résultat")
        result = len(output) > 0
        print("La répons est " + str(result))
        if result:
            # On mesure le temps d'éxécution
            timeF = round(t2 - t1, 2)
            print("Le temps de résolution est de : " + str(timeF) + " seconde(s)")
            data.append(timeF)
            # On inscrit la liste des temps de convergence dans un JSON
            json.dump(data, open('statEchantillonGreedyAvecContrainte.json', 'w'))
