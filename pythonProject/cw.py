from _csv import reader
import pandas as pd
import scipy as sp
import networkx as nx
import csv
from operator import itemgetter
from matplotlib import pyplot as plt
from networkx.algorithms import community
from tqdm import tqdm

G = nx.DiGraph()
with open('tubedata.csv', 'r') as data_csv:
    data = csv.reader(data_csv)
    headers = next(data)
    for row in tqdm(data):
        G.add_node(row[0]) #superhero in first column
        G.add_node(row[1]) #superhero in second column
        if G.has_edge(row[0], row[1]):
            # edge already exists, increase weight by one
            G[row[0]][row[1]]['weight'] += 1
        else:
            # add new edge with weight 1
            G.add_edge(row[0], row[1], weight = 1)


nodes = G.number_of_nodes()
edges = G.number_of_edges()
print(edges)
print("Nodes = ", nodes, " Edges = ",edges)
nx.draw(G, with_labels=True)
plt.show()