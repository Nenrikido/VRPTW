""""
    On affiche sous forme de graphique le nombre d'iteration en fonction de la taille de l'échantillon
"""
import matplotlib.pyplot as plt
import json

x = []
y = []

# On selectionne un fichier génerer au préalable
file = open("dataGreedySansContrainte.json", "r")
obj = json.load(file)
# On trie les données au cas ou
obj = sorted(obj)

# On ajoute le nombre de ville en absice et le temps de convergence en ordonnée
for f in obj:
    x.append(f[0])
    y.append(f[4])

# On affiche notre graphique
plt.title("Graphique du nombre d'itération en fonction de la taille de l'échantillion")
plt.plot(x, y)
plt.xlabel('Taille de l\'échantilltion en nombre de ville')
plt.ylabel('Nombre d\'itération')
plt.show()
