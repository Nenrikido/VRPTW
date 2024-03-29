"""
    VRP solving implementation (GRASP, Several vehicles, no constraint)
    Depot is index 0 by instance, (if we choose to change it we can implement a swaping algorithm)
"""

import generator as gen
import sys
import random as rn
import instances


# Handles command line arguments
matrix = None
if len(sys.argv) == 3:
    if sys.argv[1] == "instance":
        size, vehicles_amount, matrix, _ = instances.load(sys.argv[2])
    else:
        size = int(sys.argv[1])
        vehicles_amount = int(sys.argv[2])
else:
    size = 20
    vehicles_amount = 5

if matrix is None:
    matrix = gen.generate_matrix(size)

staying_nodes = list(range(1, len(matrix)))
current_node = 0
vehicles = []
iterations = 0

# First, random choose of path for each vehicles and fills paths array with it
for start_path in rn.sample(staying_nodes, vehicles_amount):
    vehicles.append({"path": [0, start_path]})
    staying_nodes.remove(start_path)

total_duration = 0
while len(staying_nodes) > 0:
    for vehicle in vehicles:
        # If an other vehicle passed in the last node
        if len(staying_nodes) == 0:
            break

        iterations += 1
        # Makes a key value dictionary of costs
        current_costs = {}
        for x, y in enumerate(matrix[vehicle['path'][-1]]):
            if x in staying_nodes:
                current_costs[x] = y

        # Sort it in ascending order
        sorted_costs = sorted(current_costs.items(), key=lambda kv: kv[1])

        # Takes the first index (minimal one) which is in staying nodes
        min_index = sorted_costs[0][0]

        total_duration += sorted_costs[0][1]
        # Append it to the vehicle path
        vehicle["path"].append(min_index)

        # Remove it from the staying nodes
        staying_nodes.remove(min_index)

# Comes back to start
for vehicle in vehicles:
    iterations += 1
    vehicle['path'].append(0)

print(f"The sum of all vehicle's travel duration is : {total_duration}\nThe amount of iterations is : {iterations}")

