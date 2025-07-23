"""
# Introduction to Structify_Net

Structify_Net is a network generator provided as a python library.

It allows to generate networks with:

* A chosen number of nodes and edges
* A chosen structure
* A constrolled amount of randomness
"""

# import matplotlib

# Pb de backend d'affichage, voir seaborn_example.py

# https://matplotlib.org/stable/users/explain/figure/backends.html
# Using use will require changes in your code if users want to use a different backend.
# Therefore, you should avoid explicitly calling use unless absolutely necessary.
# Using MPLBACKEND environment variable instead
# export MPLBACKEND=qtagg
# matplotlib.use('QtAgg')

import matplotlib.pyplot as plt
import seaborn as sns

import structify_net as stn
# from structify_net import structureClasses as sc

def r_nestedness(u, v, _):
    """
    _summary_

    Args:
        u (_type_): _description_
        v (_type_): _description_
        _ (_type_): _description_

    Returns:
        _type_: _description_
    """
    return u + v

if __name__ == '__main__':
    # Step 1: Graph properties definition
    # -----------------------------------

    # We start by defining the number of nodes and edges that we want
    NODES = 500
    EDGES = 512

    # We then generate a Rank_model object using Structify-net
    rank_nested = stn.Rank_model(NODES, r_nestedness)

    # A way to visualize the resulting structure is to plot the node pairs order
    # as a matrix
    fig = plt.figure(figsize=(4, 4), dpi=80)

    # Apply Seaborn default theme
    sns.set_theme()

    # Whole process in a function

    # The whole process of graph generation from a desired number of nodes and edges
    # can be done in a single function

    # PAS CLAIR !!!
    # LE GRAPHIQUE EST VIDE

    g_example = rank_nested.generate_graph(epsilon=0, m=EDGES)

    # plt.show()
    plt.savefig("rank_nested_generate_graph.png")
