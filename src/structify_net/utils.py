import networkx as nx


def n_to_graph(n):
    """
    _summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    g = nx.Graph()
    g.add_nodes_from(range(n))
    return g
