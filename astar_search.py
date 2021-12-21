from queue import PriorityQueue
'''
Reference: compiled this function from lab 4 solution Author: Dr Huy Phan
'''

def heuristic(node,goal,node_attributes):  # This function is used to calculate the heuristic to be added to the cost

    main_zone_current_node = int(node_attributes[node]['primary'].strip('" "')) # get the main zone attribute for the current node
    main_zone_destination_node = int(node_attributes[goal]['primary'].strip('" "')) # get the main zone attribute for the goal node
    main_zone_score = abs(main_zone_current_node-main_zone_destination_node) # subtract the zones to get a cost for the main zone difference and abs to always pass positive

    secondary_zone_current_node = int(node_attributes[node]['secondary'].strip('" "')) # get the secondary zone attribute for the current node
    secondary_zone_destination_node = int(node_attributes[goal]['secondary'].strip('" "')) # get the secondary zone attribute for the goal node
    secondary_zone_score = abs(secondary_zone_current_node - secondary_zone_destination_node)  # subtract the zones to get a cost for the secondary zone difference and abs to always pass positive
    score = abs(main_zone_score + secondary_zone_score) # add the score of the main zone and secondary zone and return positive value
    #print(score)
    return score # returns score to h

def astar_search(tubedatagraph, current_node, goal_node, node_attributes, compute_exploration_cost=True):
    stored_heuristics = {}  # this saves the score values of h into a dictionary so that it doesnt have to get calcualted everytime
    h = heuristic(current_node, goal_node, node_attributes) # prints 0
    stored_heuristics[current_node] = h
    explored = {}  # explored node dictionary set to empty, used to retrieve nodes
    explored[current_node] = (h, [current_node])  # I start node to explored

    frontier = PriorityQueue() # create empty priority queue and call it frontier
    frontier.put((h, [current_node], 0))  # Add start node to frontier
    #

    while not frontier.empty():  # While there are still paths to explore

        _, path, total_cost = frontier.get() # dequeue the node that has the smallest cost
        current_node = path[-1]
        neighbours = tubedatagraph.neighbors(current_node)  # retrieve all the neighbours of the current node

        if current_node == goal_node: # if current node is the goal node return goal node
            if compute_exploration_cost:
                print('number of explorations = {}'.format(len(explored))) # print the number of explorations to get to goal node
            return explored[goal_node]

        for neighbour in neighbours:
            edge_attributes = tubedatagraph.get_edge_data(path[-1], neighbour) # retrive the weight for the neighbour node to work out the cost from the current node to neighbour node
            if "weight" in edge_attributes:
                path_cost = edge_attributes["weight"]  # get weight
                #print(path_cost)
            else:
                path_cost = 1  # If the node does not have a weight just add 1


            if neighbour in stored_heuristics: # if the neighbour node is in the stored heuristics dictionary then retrieve its heuristic value
                h = stored_heuristics[neighbour]
            else:
                h = heuristic(neighbour, goal_node, node_attributes) # if it the node isnt stored in the heuristic dictionary then retrieve its heuristic value
                stored_heuristics[neighbour] = h

            cost = total_cost + path_cost # retrieve cost for current node
            cost_with_h = cost + h # add heuristic value to the cost
            #print(cost_with_h)
            if (neighbour not in explored) or (explored[neighbour][
                                                       0] > cost_with_h):  # if node wasnt explored or the cost is better than previous node
                next_node = (cost_with_h, path + [neighbour], cost)
                explored[neighbour] = next_node  # add node to explored
                frontier.put(next_node)  # add it to frontier to get evaluated

    return explored[goal_node]  #  return the goal node