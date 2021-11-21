'''
Reference: compiled this function with help from lab 3 solution
'''

def construct_path_dfs(node, root,nxobject,node_attributes):
    """the non-recursive way!"""

    #print(attributes_node)
    path_from_root = [node['label']]
    while node['parent']:
        node = node['parent']
        path_from_root = [node['label']] + path_from_root
    for i in path_from_root:
        print("DFS - Node Attributes: ",i ,node_attributes[i],"\n")
    return path_from_root


def depth_first_search(nxobject, root_node, goal, compute_exploration_cost=True, reverse=False):
    """the no-oop way!"""

    frontier = [{'label': root_node, 'parent': None}]
    explored = {root_node}
    number_of_explored_nodes = 1

    while frontier:
        node = frontier.pop()  # pop from the right of the list
        number_of_explored_nodes += 1
        if node['label'] == goal:
            if compute_exploration_cost:
                print('number of explorations = {}'.format(number_of_explored_nodes))
            return node

        neighbours = reversed(list(nxobject.neighbors(node['label']))) if reverse else nxobject.neighbors(node['label'])
        for child_label in neighbours:

            child = {'label': child_label, 'parent': node}
            if child_label not in explored:
                frontier.append(child)  # added to the right of the list, so it is a LIFO
                explored.add(child_label)
    return None
