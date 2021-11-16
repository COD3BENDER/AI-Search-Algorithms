simple_graph = {"node_A" : {"node_B" : 10, "node_C" : 75, "node_D" : 20},
                "node_B" : {"node_A" : 10, "node_C" : 35, "node_D" : 25},
                "node_C" : {"node_B" : 35, "node_A" : 15, "node_D" : 30},
                "node_D" : {"node_B" : 25, "node_A" : 20, "node_C" : 30}}
# https://www.youtube.com/watch?v=Ub4-nG09PFw for more help (tutorial)

def dijkstra(simple_graph, start, goal):
    shortest_distance = {} # cost to this node
    track_predecessor = {} # keep track of previously visted node (keep track of path that leads to node)
    unseenNodes = simple_graph # to iterate through the entire graph to see unseen nodes
    infinity = 999999999 # considered a very large number
    track_path = []# after reaching goal node we need to trace back to source node to find path

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes: #iterate through graph
        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] <shortest_distance[min_distance_node]: # this else if determines what the
                # min distance node is so only replace pointer if the shorter distance is lower
                min_distance_node = node
        path_options = simple_graph[min_distance_node].items() # each time you figure out min distance node you want to find the paths you can take

        for child_node, weight in path_options:
            if weight +shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight +shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node # used to trace back journey

        unseenNodes.pop(min_distance_node)

    currentNode = goal

    while currentNode != start:
        try:
            track_path.insert(0,currentNode)
            currentNode = track_predecessor[currentNode]#help to move backwards
        except KeyError:
            print("path is not reachable")
            break
    track_path.insert(0,start)

    if shortest_distance[goal] != infinity:
        print("shortest distance is" + str(shortest_distance[goal]))
        print("optimal Path is" + str(track_path))

dijkstra(simple_graph,"node_A","node_C")