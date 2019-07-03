""""
    On affiche sous forme de graphique le temps de convergence en fonction du nombre de camion
"""
import matplotlib.pyplot as plt
import json

x = []
y = []

# On selectionne un fichier génerer au préalable
file = open("StatEvolutionParametre.json", "r")
obj = json.load(file)
# On trie les données au cas ou
obj = sorted(obj)

# On ajoute le nombre de ville en absice et le temps de convergence en ordonnée
for f in obj:
    x.append(f[0])
    y.append(f[1])

# On affiche notre graphique
plt.title("Graphique du temps de convergence en secondes en fonction du nombre de camions")
plt.plot(x, y)
plt.xlabel('Nombre de camions')
plt.ylabel('Temps de convergence en secondes')
plt.show()
