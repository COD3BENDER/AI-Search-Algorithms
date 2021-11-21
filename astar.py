from queue import PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from showweightedgraph import show_weighted_graph

tube_data_graph = nx.Graph()
tube_data_dict = {}
node_attributes = {}
node_name_change = "Heathrow Terminals 1,2,3"
tubedata = pd.read_csv('tubedata.csv', sep=",", low_memory=False, quotechar='"',
                       names=['starting_station', 'destination_station', 'train_line',
                              'average_time_taken', 'primary_zone', 'secondary_zone'], index_col=None, header=None)
tubedata.loc[341]['destination_station'] = node_name_change
# aligning the heathrow terminal 4 columns as it is out of place
tubedata.loc[342]['destination_station'] = node_name_change
tubedata.loc[342]['train_line'] = ' "Piccadilly"'
tubedata.loc[342]['average_time_taken'] = ' 5'
tubedata.loc[342]['primary_zone'] = ' "6"'
tubedata.loc[342]['secondary_zone'] = ' "0"'
#preprocess main zone for nodes set with alphabets
tubedata.loc[249]['primary_zone'] = ' "7"' # Croxley
tubedata.loc[251]['primary_zone'] = ' "7"' # Rickmansworth
tubedata.loc[252]['primary_zone'] = ' "7"' # Chorleywood
tubedata.loc[253]['primary_zone'] = ' "8"' # Chalfont & Latimer
tubedata.loc[254]['primary_zone'] = ' "9"' # Chesham
# preprocess secondary zone for nodes set with alphabets
tubedata.loc[248]['secondary_zone'] = ' "7"' # Moor Park
tubedata.loc[250]['secondary_zone'] = ' "7"' # Moor Park

tubedata_no_duplicate = tubedata.drop_duplicates(inplace=False)
tube_data_dict = tubedata_no_duplicate.to_dict(orient='records')
for i in range(len(tube_data_dict)):
    start_station = tube_data_dict[i]['starting_station'].replace("", "").strip('" "')
    tube_data_dict[i]['starting_station'] = start_station

    destination_station = tube_data_dict[i]['destination_station'].replace("", "").strip('" "')
    tube_data_dict[i]['destination_station'] = destination_station

    average_time = tube_data_dict[i]['average_time_taken'].strip('"')
    tube_data_dict[i]['average_time_taken'] = average_time

    tube_data_graph.add_node(tube_data_dict[i]['starting_station'], )
    node_attributes.update(
        {tube_data_dict[i]['starting_station']: {'destination': tube_data_dict[i]['destination_station'],
                                                 'service': tube_data_dict[i]['train_line'],
                                                 'Average Time': tube_data_dict[i]['average_time_taken'],
                                                 'primary': tube_data_dict[i]['primary_zone'],
                                                 'secondary': tube_data_dict[i]['secondary_zone']}})
    nx.set_node_attributes(tube_data_graph, values=node_attributes, name=tube_data_dict[i]['starting_station'])
    if tube_data_dict[i]['destination_station'] not in node_attributes:
        node_attributes.update(
            {tube_data_dict[i]['destination_station']: {'Starting': tube_data_dict[i]['starting_station'],
                                                        'service': tube_data_dict[i]['train_line'],
                                                        'Average Time': tube_data_dict[i]['average_time_taken'],
                                                        'primary': tube_data_dict[i]['primary_zone'],
                                                        'secondary': tube_data_dict[i]['secondary_zone']}})
    tube_data_graph.add_edge(tube_data_dict[i]['starting_station'], tube_data_dict[i]['destination_station'],
                             weight=float(tube_data_dict[i]['average_time_taken']))

show_weighted_graph(tube_data_graph, 1500, 15, (10, 5))
plt.show()

def heuristic(node,goal):  # Calculates the admissible heuristic of a node
    '''
    # I know the format is [X,Y]
    node = node.replace('[', '')  # remove brackets
    node = node.replace(']', '')
    x, y = node.split(',', maxsplit=2)  # Split values by ,
    x = float(x)
    y = float(y)
    #return abs(x - 9) + abs(y - 9)  # Return calculation of admissible heuristic (manhattan distance)
    '''
    main_zone_inital = int(node_attributes[node]['primary'].strip('" "'))
    main_zone_destination = int(node_attributes[goal]['primary'].strip('" "'))
    score = abs(main_zone_inital-main_zone_destination)
    print(score)
    return score

def Astar(graph, origin, goal):
    admissible_heuristics = {}  # Will save the values of h so i don't need to calculate multiple times for every node
    h = heuristic(origin,goal) # prints 0
    admissible_heuristics[origin] = h
    visited_nodes = {}  # This will contain the data of how to get to any node
    visited_nodes[origin] = (h, [origin])  # I add the data for the origin node: "Travel cost + heuristic", "Path to get there" and "Admissible Heuristic"

    paths_to_explore = PriorityQueue()
    paths_to_explore.put((h, [origin], 0))  # Add the origin node to paths to explore, also add cost without h
    # I add the total cost, as well as the path to get there (they will be sorted automatically)

    while not paths_to_explore.empty():  # While there are still paths to explore
        # Pop elemenet with lower path cost in the queue
        _, path, total_cost = paths_to_explore.get()
        current_node = path[-1]
        neighbors = graph.neighbors(current_node)  # I get all the neighbors of the current path

        for neighbor in neighbors:
            edge_data = graph.get_edge_data(path[-1], neighbor)
            if "weight" in edge_data:
                cost_to_neighbor = edge_data["weight"]  # If the graph has weights
                #print(cost_to_neighbor)
            else:
                cost_to_neighbor = 1  # If the graph does not have weights I use 1

            if neighbor in admissible_heuristics:
                h = admissible_heuristics[neighbor]
            else:
                h = heuristic(neighbor,goal)
                admissible_heuristics[neighbor] = h

            new_cost = total_cost + cost_to_neighbor
            new_cost_plus_h = new_cost + h
            #print(new_cost_plus_h)
            if (neighbor not in visited_nodes) or (visited_nodes[neighbor][
                                                       0] > new_cost_plus_h):  # If this node was never explored, or the cost to get there is better than te previous ones
                next_node = (new_cost_plus_h, path + [neighbor], new_cost)
                visited_nodes[neighbor] = next_node  # Update the node with best value
                paths_to_explore.put(next_node)  # Also will add it as a possible path to explore

    return visited_nodes[goal]  # I will return the goal information, it will have both the total cost and the path

start = 'Euston'
destination = 'Victoria'

solution = Astar(tube_data_graph, start, destination)
print("astar", solution)