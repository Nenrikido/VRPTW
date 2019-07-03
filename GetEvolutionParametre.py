"""
    Test avec différent nombre de camion la résolution d'un même problème
"""
import time
import json
import sys
import subprocess

# Nombre de ville de départ
echantillon = 500
# Nombre de test différent
data = []

camion = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# On éxecute le programme x fois
for f in camion:
    result = False
    print(f"Essaie pour un echantillon de " + str(echantillon) + " villes : ")
    while not result:
        # On note le temps de base
        t1 = time.time()
        print("Lancement de l'algo")
        try:
            # On lance le programme
            output = subprocess.check_output(["python", "main.py", str(echantillon), str(f)], timeout=100)
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
            solution = output.split(b"The sum of all vehicle's travel duration is : ")[1].split(b"\r\n")[0]
            solution = str(solution)[2:-1]
            iteration = output.split(b"The amount of iterations is : ")[1].split(b"\r\n")[0]
            iteration = str(iteration)[2:-1]
            print(f"Solution : " + solution + " heures")
            print(f"Solution : " + iteration + " iteration")
            # On mesure le temps d'éxécution
            timeF = round(t2 - t1, 2)
            print("Le temps de résolution est de : " + str(timeF) + " seconde(s)")
            data.append([f, timeF, solution, iteration])
            # On inscrit la liste des temps de convergence dans un JSON
            json.dump(data, open('StatEvolutionParametre.json', 'w'))
