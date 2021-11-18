from queue import PriorityQueue


def heuristic(node):  # Calculates the admissible heuristic of a node
    # I know the format is [X,Y]
    node = node.replace('[', '')  # remove brackets
    node = node.replace(']', '')
    x, y = node.split(',', maxsplit=2)  # Split values by ,
    x = float(x)
    y = float(y)
    return abs(x - 9) + abs(y - 9)  # Return calculation of admissible heuristic (manhattan distance)


def Astar(graph, origin, goal):
    admissible_heuristics = {}  # Will save the values of h so i don't need to calculate multiple times for every node
    h = heuristic(origin)
    admissible_heuristics[origin] = h
    visited_nodes = {}  # This will contain the data of how to get to any node
    visited_nodes[origin] = (h, [
        origin])  # I add the data for the origin node: "Travel cost + heuristic", "Path to get there" and "Admissible Heuristic"

    paths_to_explore = PriorityQueue()
    paths_to_explore.put((h, [origin], 0))  # Add the origin node to paths to explore, also add cost without h
    # I add the total cost, as well as the path to get there (they will be sorted automatically)

    while not paths_to_explore.empty():  # While there are still paths to explore
        # Pop elemenet with lower path cost in the queue
        _, path, total_cost = paths_to_explore.get()
        current_node = path[-1]
        neighbors = graph.neighbors(current_node)  # I get all the neighbors of the current path

        for neighbor in neighbors:
            edge_data = graph.get_edge_data(path[-1], neighbor)
            if "weight" in edge_data:
                cost_to_neighbor = edge_data["weight"]  # If the graph has weights
            else:
                cost_to_neighbor = 1  # If the graph does not have weights I use 1

            if neighbor in admissible_heuristics:
                h = admissible_heuristics[neighbor]
            else:
                h = heuristic(neighbor)
                admissible_heuristics[neighbor] = h

            new_cost = total_cost + cost_to_neighbor
            new_cost_plus_h = new_cost + h
            if (neighbor not in visited_nodes) or (visited_nodes[neighbor][
                                                       0] > new_cost_plus_h):  # If this node was never explored, or the cost to get there is better than te previous ones
                next_node = (new_cost_plus_h, path + [neighbor], new_cost)
                visited_nodes[neighbor] = next_node  # Update the node with best value
                paths_to_explore.put(next_node)  # Also will add it as a possible path to explore

    return visited_nodes[goal]  # I will return the goal information, it will have both the total cost and the path