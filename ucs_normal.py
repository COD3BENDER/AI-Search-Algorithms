from queue import PriorityQueue

'''
Reference: compiled this function with help from lab 4 solution astar Author: Dr Huy Phan 
 as we know that the Astar algorithm becomes UCS when the heuristic os set to 0
 
'''

def uniform_cost_search(tubedatagraph, current_node, goal_node, node_attributes, compute_exploration_cost=True):

    frontier = PriorityQueue() # create priority queue for frontier
    frontier.put((0, [current_node], 0)) # add the start node to frontier
    number_of_explored_nodes = 1
    explored = {}  # This will contain the data of how to get to any node
    explored[current_node] = (0, [
        current_node])  # add start node to explored

    while not frontier.empty():  # when frontier is not empty

        _, path, path_cost = frontier.get() # get the node that has smallest cost
        current_node = path[-1]

        if current_node== goal_node: # if current node is goal node
            if compute_exploration_cost:
                print('number of explorations = {}'.format(len(explored)))# print the number of explorations to get to goal node
            return explored[goal_node] # return goal node

        neighbors = tubedatagraph.neighbors(current_node)  # I get all the neighbors of the current path

        for neighbor in neighbors:
            edge_attributes = tubedatagraph.get_edge_data(path[-1], neighbor) # retrive the weight for the neighbour node to work out the cost from the current node
            cost_to_neighbor = edge_attributes["weight"]  # get weight
            cost = path_cost + cost_to_neighbor # calculate cost
            # cost_extended = cost + 0
            if (neighbor not in explored) or (explored[neighbor][  # if node wasnt explored or the cost is better than previous node
                                                        0] > cost):
                next_node = (cost, path + [neighbor], cost)

                explored[neighbor] = next_node   # add node to explored
                frontier.put(next_node)   # add it to frontier to get evaluated

    return explored[goal_node] #  return the goal node

