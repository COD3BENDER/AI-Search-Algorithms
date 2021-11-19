def construct_path_ucs(node, root):
    """the non-recursive way!"""

    path_from_root = [node['label']]
    while node['parent']:
        node = node['parent']
        path_from_root = [node['label']] + path_from_root
    return path_from_root