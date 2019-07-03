# """
#     Test
# """
#
# from __future__ import print_function
# from ortools.constraint_solver import routing_enums_pb2
# from ortools.constraint_solver import pywrapcp
# import generator as gen
#
#
# def create_data_model():
#     """Stores the data for the problem."""
#     data = {
#         'time_matrix': gen.generate_matrix(size=200, edges_max_len=10, edges_proba=1),
#         'time_windows': gen.generate_time_windows(200),
#         'num_vehicles': 2,
#         'depot': 0
#     }
#     print("Input data :\nTime matrix : \n{0}\nTime windows : \n{1}\nAmount of vehicles : {2}\nId of depot : {3}\n".format(
#         data['time_matrix'],
#         data['time_windows'],
#         data['num_vehicles'],
#         data['depot']
#     ))
#     return data
#
#
# def print_solution(data, manager, routing, assignment):
#     """Prints assignment on console."""
#     time_dimension = routing.GetDimensionOrDie('Time')
#     total_time = 0
#     for vehicle_id in range(data['num_vehicles']):
#         index = routing.Start(vehicle_id)
#         plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
#         while not routing.IsEnd(index):
#             time_var = time_dimension.CumulVar(index)
#             plan_output += '{0} Time({1},{2}) -> '.format(
#                 manager.IndexToNode(index), assignment.Min(time_var),
#                 assignment.Max(time_var))
#             index = assignment.Value(routing.NextVar(index))
#         time_var = time_dimension.CumulVar(index)
#         plan_output += '{0} Time({1},{2})\n'.format(
#             manager.IndexToNode(index), assignment.Min(time_var),
#             assignment.Max(time_var))
#         plan_output += 'Time of the route: {} hours\n'.format(
#             assignment.Min(time_var))
#         print(plan_output)
#         total_time += assignment.Min(time_var)
#     print('Total time of all routes: {} hours'.format(total_time))
#
#
# def main():
#     """Solve the VRP with time windows."""
#     data = create_data_model()
#     manager = pywrapcp.RoutingIndexManager(
#         len(data['time_matrix']), data['num_vehicles'], data['depot'])
#     routing = pywrapcp.RoutingModel(manager)
#
#     def time_callback(from_index, to_index):
#         """Returns the travel time between the two nodes."""
#         # Convert from routing variable Index to time matrix NodeIndex.
#         from_node = manager.IndexToNode(from_index)
#         to_node = manager.IndexToNode(to_index)
#         return data['time_matrix'][from_node][to_node]
#
#     transit_callback_index = routing.RegisterTransitCallback(time_callback)
#     routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
#     time = 'Time'
#     routing.AddDimension(
#         transit_callback_index,
#         99999999999,
#         99999999999,
#         False,
#         time)
#     time_dimension = routing.GetDimensionOrDie(time)
#     # Add time window constraints for each location except depot.
#     for location_idx, time_window in enumerate(data['time_windows']):
#         if location_idx == 0:
#             continue
#         index = manager.NodeToIndex(location_idx)
#         time_dimension.CumulVar(index).SetRange(time_window[0], time_window[1])
#     # Add time window constraints for each vehicle start node.
#     for vehicle_id in range(data['num_vehicles']):
#         index = routing.Start(vehicle_id)
#         time_dimension.CumulVar(index).SetRange(data['time_windows'][0][0],
#                                                 data['time_windows'][0][1])
#     for i in range(data['num_vehicles']):
#         routing.AddVariableMinimizedByFinalizer(
#             time_dimension.CumulVar(routing.Start(i)))
#         routing.AddVariableMinimizedByFinalizer(
#             time_dimension.CumulVar(routing.End(i)))
#     search_parameters = pywrapcp.DefaultRoutingSearchParameters()
#     search_parameters.first_solution_strategy = (
#         routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
#     assignment = routing.SolveWithParameters(search_parameters)
#     if assignment:
#         print_solution(data, manager, routing, assignment)
#
#
# if __name__ == '__main__':
#     main()
