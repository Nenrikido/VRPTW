"""
    Try in implementing savings algorithm
"""


import generator as gen

# Amount of nodes
size = 10

# Amount of vehicles
vehicles_amount = 1

# Input matrix generation
matrix = gen.generate_matrix(size=size, edges_max_len=10, edges_proba=1)

# List of savings for each edges
savings = {}

# List of routes
routes = []

for node_b_index in range(1, size):

    # Add initial route for the node
    routes.append(f"0 {node_b_index} 0")

    for node_a_index in range(1, node_b_index):

        # Applies the saving calculation
        cost_origin_to_node_a = matrix[0, node_a_index]
        cost_origin_to_node_b = matrix[0, node_b_index]
        cost_node_a_to_node_b = matrix[node_a_index, node_b_index]
        savings[(node_a_index, node_b_index)] = cost_origin_to_node_a + cost_origin_to_node_b - cost_node_a_to_node_b

# Sorts the dictionary by descending value
sorted_savings = sorted(savings.items(), key=lambda kv: kv[1], reverse=True)

for (node_a_index, node_b_index), _ in sorted_savings:
    routes.append(f"0 {node_a_index} {node_b_index} 0")
    for (next_node, _), _ in sorted_savings:
        if next_node == node_b_index and f"0 {node_b_index} 0" in routes:
            routes.remove(f"0 {node_b_index} 0")
            routes.append(f"0 {node_b_index} {next_node} 0")
            break

