"""
    VRP solving implementation
    Depot is index 0 by instance, (if we choose to change it we can implement a swaping algorithm)
"""

import sys
import generator as gen
from clock import HourClock as Clock
import random as rn
import instances
import itertools

# Handles command line arguments
matrix = None
tws = None
if len(sys.argv) == 3:
    if sys.argv[1] == "instance":
        size, vehicles_amount, matrix, tws = instances.load(sys.argv[2])
    else:
        size = int(sys.argv[1])
        vehicles_amount = int(sys.argv[2])
else:
    size = 20
    vehicles_amount = 5

# Generates a time cost matrix and time window list
if matrix is None:
    matrix = gen.generate_matrix(size)
    tws = gen.generate_time_windows(size)

staying_nodes = list(range(1, len(matrix)))
current_node = 0
vehicles = []

# First, random choose of path for each vehicles and fills paths array with it
for start_path in rn.sample(staying_nodes, vehicles_amount):
    vehicles.append({"path": [0, start_path], "clock": Clock(), "travel_duration": 0})
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
                time_window = tws[x]
                current_costs[x] = (y, *time_window, time_window[1].delta(vehicle['clock'] + y))

        # Sorts it in "difference between clock and ending time of TW + time of travel" order then ascending value order
        sorted_costs = sorted(current_costs.items(), key=lambda kv: kv[1][3])

        # Choose randomly between the minimal choices
        min_index, (time_cost, twx, twy, cost_with_constraint) = rn.choice(
            [*itertools.takewhile(lambda cost: cost[1][3] == sorted_costs[0][1][3], sorted_costs)])

        # Appends it to the vehicle path
        vehicle["path"].append(min_index)

        # Changes vehicle clock to add travel duration to specific node
        vehicle['clock'].add(time_cost)

        # Handles waiting time if not in time window and adds it to the total travel duration and the vehicle clock
        if not vehicle['clock'].between(twx, twy):
            waiting_time = vehicle['clock'].delta(twx)

            vehicle['travel_duration'] += waiting_time
            vehicle['clock'].add(waiting_time)

        # Adds travel duration to specific node to total travel duration
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

print("The paths are : ",
      *[f"Vehicle {i + 1} : {vehicle['path']} Duration : {vehicle['travel_duration']}" for i, vehicle in
        enumerate(vehicles)], sep="\n")
print(f"The sum of all vehicle's travel duration is : {total_duration}\nThe amount of iterations is : {iterations}")
