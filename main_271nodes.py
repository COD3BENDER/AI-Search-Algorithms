import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


from bfs import breadth_first_search , construct_path_bfs
from dfs import depth_first_search, construct_path_dfs

tube_data_graph = nx.Graph()
tube_data_dict = {}
node_attributes = {}
tubedata = pd.read_csv('tubedata.csv',sep=",", low_memory=False,quotechar='"', names=['starting_station', 'destination_station', 'train_line',
                                                                              'average_time_taken', 'primary_zone','secondary_zone'], index_col = None, header=None)
tubedata_no_duplicate = tubedata.drop_duplicates(inplace=False)
tube_data_dict = tubedata_no_duplicate.to_dict(orient='records')
tubedata_edge = {}


for i in range(len(tube_data_dict)):

    tubedata_edge.update({tube_data_dict[i]['starting_station'].replace("","").strip('" "'): {tube_data_dict[i]['destination_station'].replace("","").strip('" "'): {'weight':tube_data_dict[i]['average_time_taken'].strip('"')}}})
    node_attributes.update(
        {tube_data_dict[i]['starting_station']: {'destination': tube_data_dict[i]['destination_station'],
                                                 'service': tube_data_dict[i]['train_line'],
                                                 'time': tube_data_dict[i]['average_time_taken'],
                                                 'primary': tube_data_dict[i]['primary_zone'],
                                                 'secondary': tube_data_dict[i]['secondary_zone']}})
    nx.set_node_attributes(tube_data_graph, values=node_attributes, name='node_type')
tube_data_graph = nx.Graph(tubedata_edge)
nx.draw_networkx(tube_data_graph, with_labels=True)

print(tube_data_graph.edges(data=True))

plt.show()
print(tube_data_graph)
dfs = depth_first_search(tube_data_graph, 'Euston', 'Victoria')
print("Depth First Search:", construct_path_dfs(dfs, 'Euston'))

bfs = breadth_first_search(tube_data_graph, 'Euston', 'Victoria')
print("Breadth First Search:",construct_path_bfs(bfs, 'Euston'))