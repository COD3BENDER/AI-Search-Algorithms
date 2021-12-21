'''
Reference: compiled this function  from lab 3 solution Author Dr Huy Phan
'''

def construct_path_bfs(node, root,nxobject,node_attributes):

    path_from_root = [node['label']]
    while node['parent']:
        node = node['parent']
        path_from_root = [node['label']] + path_from_root
    for i in path_from_root:
        print("BFS - Node Attributes: ", i,node_attributes[i],"\n")
    return path_from_root

def breadth_first_search(tubedatagraph, current_node, goal_node, compute_exploration_cost=True, reverse=False):
    if current_node == goal_node:
        return None

    number_of_explored_nodes = 1
    frontier = [{'label': current_node, 'parent': None}]

    explored = {current_node}

    while frontier:
        node = frontier.pop() # get from right of frontier for FIFO

        neighbours = reversed(list(tubedatagraph.neighbors(node['label']))) if reverse else tubedatagraph.neighbors(node['label'])

        for child_label in neighbours:
            child = {'label': child_label, 'parent': node}
            if child_label == goal_node:
                if compute_exploration_cost:
                    print('number of explorations = {}'.format(number_of_explored_nodes))
                return child

            if child_label not in explored:
                frontier = [child] + frontier  # add to left of frontier to make FIFO
                number_of_explored_nodes += 1
                explored.add(child_label)

    return None