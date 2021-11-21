from queue import PriorityQueue

def uniform_cost_search_extended(nxobject, initial, goal, node_attributes):

    frontier = PriorityQueue()
    frontier.put((0, [initial], 0))  # Add the origin node to paths to explore, also add cost 0
    explored_nodes = {}  # This will contain the data of how to get to any node
    explored_nodes[initial] = (0, [initial])  # I add the data for the origin node: "Travel cost + heuristic", "Path to get there" and "Admissible Heuristic"
    # I add the total cost, as well as the path to get there (they will be sorted automatically)
    initial_train_line = node_attributes[initial]['service']
    while not frontier.empty():  # While there are still paths to explore
        # Pop elemenet with lower path cost in the queue
        _, path, path_cost = frontier.get()
        current_node = path[-1]
        neighbors = nxobject.neighbors(current_node)  # I get all the neighbors of the current path

        for neighbor in neighbors:
            neighbor_train_line = node_attributes[neighbor]['service']
            edge_data = nxobject.get_edge_data(path[-1], neighbor)
            cost_to_neighbor = edge_data["weight"]  # graph weights
            if neighbor_train_line == initial_train_line:
                cost = path_cost + cost_to_neighbor
                cost_extended = cost + 0
            else:
                cost = path_cost + cost_to_neighbor
                cost_extended = cost + 8 # add weight if the tube line is transfered to keep path on same tube line as much as possible

            if (neighbor not in explored_nodes) or (explored_nodes[neighbor][0] > cost_extended):  # If this node was never explored, or the cost to get there is better than te previous ones
                next_node = (cost_extended, path + [neighbor], cost_extended)
                explored_nodes[neighbor] = next_node  # Update the node with best value
                frontier.put(next_node)  # Also will add it as a possible path to explore

    return explored_nodes[goal]  # I will return the goal information, it will have both the total cost and the path





'''
procedure uniform_cost_search(Graph, start, goal) is
    node ← start
    cost ← 0
    frontier ← priority queue containing node only
    explored ← empty set
    do
        if frontier is empty then
            return failure
        node ← frontier.pop()
        if node is goal then
            return solution
        explored.add(node)
        for each of node's neighbors n do
            if n is not in explored then
                frontier.add(n)
'''
