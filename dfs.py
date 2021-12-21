'''
Reference: compiled this function  from lab 3 solution Author Dr Huy Phan
'''

def construct_path_dfs(node, root,nxobject,node_attributes):

    #print(attributes_node)
    path_from_root = [node['label']]
    while node['parent']:
        node = node['parent']
        path_from_root = [node['label']] + path_from_root
    for i in path_from_root:
        print("DFS - Node Attributes: ",i ,node_attributes[i],"\n")
    return path_from_root


def depth_first_search(tubedatagraph, current_node, goal_node, compute_exploration_cost=True, reverse=False):

    frontier = [{'label': current_node, 'parent': None}]
    explored = {current_node}
    number_of_explored_nodes = 1

    while frontier:
        node = frontier.pop()  # get from right of frontier list LIFO
        number_of_explored_nodes += 1
        if node['label'] == goal_node:
            if compute_exploration_cost:
                print('number of explorations = {}'.format(number_of_explored_nodes))
            return node

        neighbours = reversed(list(tubedatagraph.neighbors(node['label']))) if reverse else tubedatagraph.neighbors(node['label'])
        for child_label in neighbours:

            child = {'label': child_label, 'parent': node}
            if child_label not in explored:
                frontier.append(child)  # added to the right LIFO
                explored.add(child_label)
    return None
