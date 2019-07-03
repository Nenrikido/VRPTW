"""
    VRP solving implementation (Greedy, no constraint)
    Depot is index 0 by instance, (if we choose to change it we can implement a swaping algorithm)
"""


import generator as gen
import time

t0 = time.time()

size = 500

edges_max_len = 50

vehicles_amount = 5

matrix = gen.generate_matrix(size=size, edges_max_len=edges_max_len, edges_proba=1)

staying_nodes = list(range(len(matrix)))
current_node = 0
path = "0"

while len(staying_nodes) > 0:

    # Makes a key value dictionary of costs
    current_costs = {}
    for x, y in enumerate(matrix[current_node]):
        if x in staying_nodes:
            current_costs[x] = y

    # Sort it in ascending order
    sorted_costs = sorted(current_costs.items(), key=lambda kv: kv[1])

    # Takes the first index which is in staying nodes
    current_node = sorted_costs[0][0]

    staying_nodes.remove(current_node)

    path += f" -> {current_node}"

print(path)

print(str(time.time() - t0)[:5])