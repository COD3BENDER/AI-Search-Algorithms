
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from bfs import breadth_first_search, construct_path_bfs
from dfs import depth_first_search, construct_path_dfs
from showweightedgraph import show_weighted_graph

tube_data_graph = nx.Graph()
tube_data_dict = {}
node_attributes = {}
tubedata = pd.read_csv('tubedata.csv',sep=",", low_memory=False,quotechar='"', names=['starting_station', 'destination_station', 'train_line',
                                                                              'average_time_taken', 'primary_zone','secondary_zone'], index_col = None, header=None)
tubedata.loc[341]['destination_station'] = "Heathrow Terminals 1,2,3"
tubedata.loc[342]['destination_station'] = "Heathrow Terminals 1,2,3"
tubedata_no_duplicate = tubedata.drop_duplicates(inplace=False)
tube_data_dict = tubedata_no_duplicate.to_dict(orient='records')

for i in range(len(tube_data_dict)):
    start_station = tube_data_dict[i]['starting_station'].replace("","").strip('" "')
    tube_data_dict[i]['starting_station'] = start_station

    destination_station = tube_data_dict[i]['destination_station'].replace("","").strip('" "')
    tube_data_dict[i]['destination_station'] = destination_station

    average_time = tube_data_dict[i]['average_time_taken'].strip('"')
    tube_data_dict[i]['average_time_taken'] = average_time

    tube_data_graph.add_node(tube_data_dict[i]['starting_station'],)
    node_attributes.update(
        {tube_data_dict[i]['starting_station']: {'destination': tube_data_dict[i]['destination_station'], 'service': tube_data_dict[i]['train_line'],
                                                 'time': tube_data_dict[i]['average_time_taken'],'primary': tube_data_dict[i]['primary_zone'],'secondary': tube_data_dict[i]['secondary_zone'] }})

    nx.set_node_attributes(tube_data_graph,values= node_attributes,name= tube_data_dict[i]['starting_station'])
    tube_data_graph.add_edge(tube_data_dict[i]['starting_station'],tube_data_dict[i]['destination_station'],weight=float(tube_data_dict[i]['average_time_taken']))

show_weighted_graph(tube_data_graph, 1500, 15, (10,5))
plt.show()

print(tube_data_graph)

dfs = depth_first_search(tube_data_graph, "Euston", 'Stepney Green')
print("Depth First Search:", construct_path_dfs(dfs, "Euston",tube_data_graph,node_attributes),"\n")

bfs = breadth_first_search(tube_data_graph, "Euston", 'Stepney Green')
print("Breadth First Search:",construct_path_bfs(bfs, "Euston",tube_data_graph,node_attributes),"\n")