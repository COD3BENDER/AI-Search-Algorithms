import heapq
from queue import PriorityQueue

 #reference https://github.com/santiagoLabs/UniformCostSearch-Shortest_path_between_2_UK_cities/blob/master/src/ucs.py
 #this code was compiled using the reference


def uniform_cost_search_online(nxobject, initial, goal, compute_exploration_cost=True):
    number_of_explored_nodes = 1
    frontier = []
    node_in_frontier = {}
    node = (0, initial, [initial])
    # Use a dictionary to keep track of the elements inside the frontier (queue)
    node_in_frontier[node[1]] = [node[0], node[2]]
    # Insert the node inside the frontier (queue)
    heapq.heappush(frontier, node)
    explored = set()

    while frontier:
        if len(frontier) == 0:
            return None
        # Pop elemenet with lower construct_path_ucs cost in the queue
        node = heapq.heappop(frontier)
        # Delete from the dicitonary the element that has beeen popped
        del node_in_frontier[node[1]]
        # Check if the solution has been found
        if node[1] == goal:
            if compute_exploration_cost:
                print('number of explorations = {}'.format(number_of_explored_nodes))
            return node

        explored.add(node[1])
        # Get a list of all the child_label nodes of node
        neighbours = list(nxobject.neighbors(node[1]))
        construct_path_ucs = node[2]

        for child_label in neighbours:
            construct_path_ucs.append(child_label)
            # create the child_label node that will be inserted in frontier
            child = (node[0] + nxobject.get_edge_data(node[1], child_label)["weight"], child_label, construct_path_ucs) #have a look at this
            #print("frontier = {}".format(child))
            # Check the child_label node is not explored and not in frontier thorugh the dictionary

            if child_label not in explored and child_label not in node_in_frontier:
                heapq.heappush(frontier, child)
                node_in_frontier[child_label] = [child[0], child[2]]
                number_of_explored_nodes += 1

            elif child_label in node_in_frontier:
                # Checks if the child_label node has a lower construct_path_ucs cost than the node already in frontier
                if child[0] < node_in_frontier[child_label][0]:
                    remove_node = (node_in_frontier[child_label][0], child_label, node_in_frontier[child_label][1])
                    frontier.remove(remove_node)
                    heapq.heapify(frontier)
                    del node_in_frontier[child_label]

                    heapq.heappush(frontier, child)
                    node_in_frontier[child_label] = [child[0], child[2]]
            construct_path_ucs = construct_path_ucs[:-1]





