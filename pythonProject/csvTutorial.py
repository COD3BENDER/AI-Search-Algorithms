import networkx as nx
import matplotlib.pyplot as plt
import csv
from operator import itemgetter
from networkx.algorithms import community

with open('quakers_nodelist.csv', 'r') as nodecsv: # open file
    nodereader = csv.reader(nodecsv) # read csv
    nodes = [n for n in nodereader][1:] # retrive data using python list comprehension and list slicing to remove the header row, footnote 3
node_names = [n[0] for n in nodes] # get a list of only the node names

with open('quakers_edgelist.csv', 'r') as edgecsv: # open file
    edgereader = csv.reader(edgecsv)# read csv
    edges = [tuple(e) for e in edgereader][1:] # retrive data

print(len(node_names))
print(len(edges))
G = nx.Graph()
G.add_nodes_from(node_names)
G.add_edges_from(edges)
print(nx.info(G))

hist_sig_dict = {}
gender_dict = {}
brith_dict = {}
death_dict = {}
id_dict = {}

for node in nodes: # loop through the list one row at a time in mines they are the bullet points for 2
    hist_sig_dict[node[0]] = node[1]
    gender_dict[node[0]] = node[2]
    brith_dict[node[0]] = node[3]
    death_dict[node[0]] = node[4]
    id_dict[node[0]] = node[5]

nx.set_node_attributes(G,hist_sig_dict,'historical_significance')
nx.set_node_attributes(G,gender_dict,'gender')
nx.set_node_attributes(G,brith_dict,'birth_year')
nx.set_node_attributes(G,death_dict,'death_year')
nx.set_node_attributes(G,id_dict,'sdfb_id')

for n in G.nodes():
    print(n,G.nodes[n]['birth_year'])

density = nx.density(G)
print("Network density:", density)
nx.draw_networkx(G, with_labels=True)
plt.show()
