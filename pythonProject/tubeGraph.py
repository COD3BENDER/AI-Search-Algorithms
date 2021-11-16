import networkx as nx
import matplotlib.pyplot as plt
import csv
from operator import itemgetter
from networkx.algorithms import community

with open('tubedata.csv', 'r') as datacsv: # open file
    datareader = csv.reader(datacsv) # read csv
    nodes = [n for n in datareader] # retrive data using python list
node_names = [n[0] for n in nodes] # get a list of only the node names


with open('tubedata.csv', 'r') as edgecsv: # open file
    data = [(int(line['begin']), int(line['end'])) for line in csv.DictReader(edgecsv)]
    edgereader = csv.reader(edgecsv)# read csv
    edges = [tuple(e) for e in edgereader] # retrive data for edges -- this is where i have the issue

print(len(node_names))
print(len(edges))
G = nx.Graph()
G.add_nodes_from(node_names)
G.add_edges_from(edges)
print(nx.info(G))

start_station_dict = {}
end_station_dict = {}
tube_line_dict = {}
average_time_taken_dict = {}
main_zone_dict = {}
secondary_zone_dict = {}

for node in nodes: # loop through the list one row at a time
    start_station_dict[node[0]] = node[0]
    end_station_dict[node[0]] = node[1]
    tube_line_dict[node[0]] = node[2]
    average_time_taken_dict[node[0]] = node[3]
    main_zone_dict[node[0]] = node[4]
    secondary_zone_dict[node[0]] = node[5]

nx.set_node_attributes(G,start_station_dict,'start_station')
nx.set_node_attributes(G,end_station_dict,'end_station')
nx.set_node_attributes(G,tube_line_dict,'tube_line')
nx.set_node_attributes(G,average_time_taken_dict,'average_time_taken')
nx.set_node_attributes(G,main_zone_dict,'main_zone')
nx.set_node_attributes(G,secondary_zone_dict,'secondary_zone')

for n in G.nodes():
    print(n,G.nodes[n]['end_station'])

density = nx.density(G)
print("Network density:", density)
nx.draw_networkx(G, with_labels=True)
plt.show()
