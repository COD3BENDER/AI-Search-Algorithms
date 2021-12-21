from queue import PriorityQueue

'''
Reference: compiled this function with help from lab 4 solution astar Author: Dr Huy Phan 
 as we know that the Astar algorithm becomes UCS when the heuristic os set to 0

'''

def uniform_cost_search_extended(tubedatagraph, current_node, goal_node, node_attributes,
                                 compute_exploration_cost=True):
    frontier = PriorityQueue()  # create priority queue for frontier
    frontier.put((0, [current_node], 0))  # add the start node to frontier
    explored_nodes = {}  # This will contain the data of how to get to any node
    explored_nodes[current_node] = (0, [current_node])  # add start node to explored
    goal_train_line = node_attributes[current_node]['service']  # get train line attribute for goal node

    while not frontier.empty():  # when frontier is not empty

        _, path, path_cost = frontier.get()  # get the node that has smallest cost
        current_node = path[-1]

        if current_node == goal_node:  # if current node is goal node
            if compute_exploration_cost:  # print the number of explorations to get to goal node
                print('number of explorations = {}'.format(len(explored_nodes)))

            return explored_nodes[goal_node]
        neighbors = tubedatagraph.neighbors(current_node)  # I get all the neighbors of the current path

        for neighbor in neighbors: # retrive the weight for the neighbour node to work out the cost from the current
            current_train_line = node_attributes[neighbor]['service']
            edge_data = tubedatagraph.get_edge_data(path[-1], neighbor)
            cost_to_neighbor = edge_data["weight"]  # graph weights
            if current_train_line == goal_train_line: # if the train line is the same
                cost = path_cost + cost_to_neighbor
                cost_extended = cost + 0
            else: # if it isnt
                cost = path_cost + cost_to_neighbor
                cost_extended = cost + 5  # add weight if the tube line is transfered to keep path on same tube line as much as possible

            if (neighbor not in explored_nodes) or (explored_nodes[neighbor][  # if node wasnt explored or the cost is better than previous node
                                                        0] > cost_extended):
                next_node = (cost_extended, path + [neighbor], cost_extended)
                explored_nodes[neighbor] = next_node   # add node to explored
                frontier.put(next_node)  # add it to frontier to get evaluated

    return explored_nodes[
        goal_node]  #  return the goal node
