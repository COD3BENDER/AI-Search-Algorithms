'''
Reference: compiled this function with help from lab 3 solution
'''

def construct_path_bfs(node, root,nxobject,node_attributes):
    """the non-recursive way!"""

    path_from_root = [node['label']]
    while node['parent']:
        node = node['parent']
        path_from_root = [node['label']] + path_from_root
    for i in path_from_root:
        print("BFS - Node Attributes: ", i,node_attributes[i],"\n")
    return path_from_root

def breadth_first_search(nxobject, root_node, goal, compute_exploration_cost=True, reverse=False):
    if root_node == goal:  # just in case, because now we are checking the children
        return None

    number_of_explored_nodes = 1
    frontier = [{'label': root_node, 'parent': None}]
    # FIFO queue should NOT be implemented with a list, this is slow! better to use deque
    explored = {root_node}

    while frontier:
        node = frontier.pop()  # pop from the right of the list

        neighbours = reversed(list(nxobject.neighbors(node['label']))) if reverse else nxobject.neighbors(node['label'])

        for child_label in neighbours:
            child = {'label': child_label, 'parent': node}
            if child_label == goal:
                if compute_exploration_cost:
                    print('number of explorations = {}'.format(number_of_explored_nodes))
                return child

            if child_label not in explored:
                frontier = [child] + frontier  # added to the left of the list, so a FIFO!
                number_of_explored_nodes += 1
                explored.add(child_label)

    return None