""""
    Comparatif des solutions trouvé entre notre Algorithme et celui d'OR-TOOLS
"""
import matplotlib.pyplot as plt
import json

x = []
y = []

a = []
b = []

# On ouvre le fichier de résultat d'OR-TOOLS
file = open("export.json", "r")
obj = json.load(file)
obj = sorted(obj)

# On ouvre le fichier de résultat de notre Algorithme
file2 = open("dataGreedyAvecContrainte.json", "r")
obj2 = json.load(file2)
obj2 = sorted(obj2)

max = 0

# On compare quelle liste a la valeur d'abscisse la plus élevé
if obj[len(obj) - 1][0] > obj2[len(obj2) - 1][0]:
    max = obj2[len(obj2) - 1][0]
else:
    max = obj[len(obj) - 1][0]

# On récupère les valeurs et on les ajoutes dans des listes
for f in obj:
    if f[0] > max:
        break
    x.append(f[0])
    y.append(f[2])

# On récupère les valeurs et on les ajoutes dans des listes
for f in obj2:
    if f[0] > max:
        break
    a.append(f[0])
    b.append(f[2])

# On affiche les deux courbe sur le même graphe
plt.title("Graphique de la solution trouvée en fonction de la taille de l'échantillon")
plt.plot(x, y, color='blue', linestyle='solid', label='or-tools')
plt.plot(a, b, color='red', linestyle='solid', label='Algo')
plt.xlabel('Taille de l\'échantillon en nombre de ville')
plt.ylabel('Solution trouvée en heures')
plt.legend(loc="upper left")
plt.show()
