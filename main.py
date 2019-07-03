"""
    VRP solving implementation
    Depot is index 0 by instance, (if we choose to change it we can implement a swaping algorithm)
"""

import sys
import generator as gen
from clock import HourClock as Clock
import random as rn

if len(sys.argv) > 1:
    size = int(sys.argv[-2])
    vehicles_amount = int(sys.argv[-1])
else:
    size = 20
    vehicles_amount = 5

# Generates a time cost matrix and time window list
matrix = gen.generate_matrix(size)
tws = gen.generate_time_windows(size)

staying_nodes = list(range(1, len(matrix)))
current_node = 0
vehicles = []

# First, random choose of path for each vehicles and fills paths array with it
for start_path in rn.sample(staying_nodes, vehicles_amount):
    vehicles.append({"path": [0, start_path], "clock": Clock(), "travel_duration": 0, "infos": []})
    staying_nodes.remove(start_path)

# Iterations counter
iterations = 0

# Main loop (while there are staying nodes)
while len(staying_nodes) > 0:
    for vehicle in vehicles:
        # If an other vehicle passed in the last node
        if len(staying_nodes) == 0:
            break

        iterations += 1

        # Makes a key value dictionary of costs and time windows => index : (cost, time window start, time window end)
        current_costs = {}
        current_node = vehicle['path'][-1]
        for x, y in enumerate(matrix[current_node]):
            iterations += 1
            if x in staying_nodes and x != current_node:
                current_costs[x] = (y, *tws[x])

        # Sorts it in "difference between clock and ending time of TW" order then ascending value order
        sorted_costs = sorted(current_costs.items(), key=lambda kv: kv[1][2].delta(vehicle['clock'] + kv[1][0]))

        # Choose randomly between the first few indexes
        min_index, (time_cost, twx, twy) = rn.choice(sorted_costs[:int(size/10) + 1])

        # Append it to the vehicle path
        vehicle["path"].append(min_index)

        # Handles waiting time if not in time window (compares with starting time of time window)
        vehicle['travel_duration'] += vehicle['clock'].delta(twx)

        # Changes vehicle clock and travel duration since start
        vehicle['clock'].add(time_cost)
        vehicle['travel_duration'] += time_cost

        # Remove the travelled node from the staying nodes
        staying_nodes.remove(min_index)

# Comes back to start + sums travel durations
total_duration = 0

for vehicle in vehicles:
    iterations += 1
    vehicle['travel_duration'] += matrix[vehicle['path'][-1]][0]
    vehicle['path'].append(0)

    total_duration += vehicle['travel_duration']

print("The paths are : ", *[])
print(f"The sum of all vehicle's travel duration is : {total_duration}\nThe amount of iterations is : {iterations}")

# TODO : printing paths
# print()
