import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

from astar import Astar
from bfs import breadth_first_search
from dfs import depth_first_search, construct_path_from_root

tube_data_graph = nx.Graph()
tube_data_dict = {}
tubedata = pd.read_csv('tubedata.csv',sep=",", low_memory=False,quotechar='"', names=['starting_station', 'destination_station', 'train_line',
                                                                              'average_time_taken', 'primary_zone','secondary_zone'], index_col = None, header=None)
tubedata_no_duplicate = tubedata.drop_duplicates(inplace=False)
tube_data_dict = tubedata_no_duplicate.to_dict(orient='records')

for i in range(len(tube_data_dict)):
    start_station = tube_data_dict[i]['starting_station'].replace("","").strip('" "')
    tube_data_dict[i]['starting_station'] = start_station

    destination_station = tube_data_dict[i]['destination_station'].replace("","").strip('" "')
    tube_data_dict[i]['destination_station'] = destination_station

    average_time = tube_data_dict[i]['average_time_taken'].strip('"')
    tube_data_dict[i]['average_time_taken'] = average_time

    tube_data_graph.add_node(tube_data_dict[i]['starting_station'])
    tube_data_graph.add_edge(tube_data_dict[i]['starting_station'],tube_data_dict[i]['destination_station'],weight=tube_data_dict[i]['average_time_taken'])

nx.draw_networkx(tube_data_graph, with_labels=True)
#print(tube_data_dict)

plt.show()
print(tube_data_graph)
dfs = depth_first_search(tube_data_graph, 'Euston', 'Victoria')
print("Depth First Search:", construct_path_from_root(dfs, 'Euston'))

bfs = breadth_first_search(tube_data_graph, 'Euston', 'Victoria')
print("breadth First Search:",construct_path_from_root(bfs, 'Euston'))



