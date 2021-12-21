import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

from astar_search import astar_search
from bfs import breadth_first_search, construct_path_bfs
from dfs import depth_first_search, construct_path_dfs
from showweightedgraph import show_weighted_graph
from ucs_extendedcost import uniform_cost_search_extended
from ucs_normal import uniform_cost_search

tube_data_graph = nx.Graph() # create graph
tube_data_dict = {} # create dictionary
node_attributes = {} # create dictionary to store node attributes
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
# preprocess main zone for nodes set with alphabets
tubedata.loc[249]['primary_zone'] = ' "7"'  # Croxley
tubedata.loc[251]['primary_zone'] = ' "7"'  # Rickmansworth
tubedata.loc[252]['primary_zone'] = ' "7"'  # Chorleywood
tubedata.loc[253]['primary_zone'] = ' "8"'  # Chalfont & Latimer
tubedata.loc[254]['primary_zone'] = ' "9"'  # Chesham
# preprocess secondary zone for nodes set with alphabets
tubedata.loc[248]['secondary_zone'] = ' "7"'  # Moor Park
tubedata.loc[250]['secondary_zone'] = ' "7"'  # Moor Park

tubedata_no_duplicate = tubedata.drop_duplicates(inplace=False)
tube_data_dict = tubedata_no_duplicate.to_dict(orient='records') # remove duplicate entries
for i in range(len(tube_data_dict)):
    start_station = tube_data_dict[i]['starting_station'].replace("", "").strip('" "') # retrive the start node from dictionary
    tube_data_dict[i]['starting_station'] = start_station

    destination_station = tube_data_dict[i]['destination_station'].replace("", "").strip('" "') # retrive the goal node from dictionary
    tube_data_dict[i]['destination_station'] = destination_station

    average_time = tube_data_dict[i]['average_time_taken'].strip('"') # retrive the weight from dictionary
    tube_data_dict[i]['average_time_taken'] = average_time

    tube_data_graph.add_node(tube_data_dict[i]['starting_station'], )
    node_attributes.update( # update node attribute dictionary with the attributes of nodes
        {tube_data_dict[i]['starting_station']: {'destination': tube_data_dict[i]['destination_station'],
                                                 'service': tube_data_dict[i]['train_line'],
                                                 'Average Time': tube_data_dict[i]['average_time_taken'],
                                                 'primary': tube_data_dict[i]['primary_zone'],
                                                 'secondary': tube_data_dict[i]['secondary_zone']}})
    if tube_data_dict[i]['destination_station'] not in node_attributes:
        node_attributes.update(
            {tube_data_dict[i]['destination_station']: {'Starting station': tube_data_dict[i]['starting_station'],
                                                        'service': tube_data_dict[i]['train_line'],
                                                        'Average Time': tube_data_dict[i]['average_time_taken'],
                                                        'primary': tube_data_dict[i]['primary_zone'],
                                                        'secondary': tube_data_dict[i]['secondary_zone']}})

    nx.set_node_attributes(tube_data_graph, values=node_attributes, name=tube_data_dict[i]['starting_station']) # set node attributes
    tube_data_graph.add_edge(tube_data_dict[i]['starting_station'], tube_data_dict[i]['destination_station'], # add edges of start node destination node and weight
                             weight=float(tube_data_dict[i]['average_time_taken']))

show_weighted_graph(tube_data_graph, 1500, 15, (10, 5))
plt.show()

print(tube_data_graph, "\n")

'''
start = 'Euston'
destination = 'Victoria'

start = 'Canada Water'
destination = 'Stratford'

start = 'New Cross Gate'
destination = 'Stepney Green'

start = 'Ealing Broadway'
destination = 'South Kensington'

start = 'Baker Street'
destination = 'Wembley Park'

'''
start = 'Euston'
destination = 'Victoria'

dfs = depth_first_search(tube_data_graph, start, destination)  # dfs.py
print("Depth First Search Path: ", construct_path_dfs(dfs, start, tube_data_graph, node_attributes), "\n")

bfs = breadth_first_search(tube_data_graph, start, destination)  # bfs.py
print("Breadth First Search Path: ", construct_path_bfs(bfs, start, tube_data_graph, node_attributes), "\n")

ucs_search = uniform_cost_search(tube_data_graph, start, destination, node_attributes)  # ucs_normal.py
print("UCS", ucs_search, "\n")

ucs_search_extended = uniform_cost_search_extended(tube_data_graph, start, destination,node_attributes)  # ucs_extendedcost.py
print("UCS Extended Cost", ucs_search_extended, "\n")

astar = astar_search(tube_data_graph, start, destination, node_attributes)  # astar_search.py
print("astar", astar, "\n")
