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
import numpy as np
import seaborn as sns

import structify_net as stn
# from structify_net.viz import plot_adjacency_matrix


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
    NODES = 128
    EDGES = 512

    # Step 2: Structure definion
    # --------------------------

    # We start by defining a structure, by ordering the pairs of nodes in the graph
    # from the most likely to appear to the less likely to appear.

    # For instance, if we assume that our network is a spatial network,
    # and that each node has a position in an euclidean space,
    # we can define that the pairs of nodes are ranked according to their distance
    # in this space.

    # Many classic structures are already implemented in Structify-Net.
    #
    # For the sake of example, here we define a very simple organisation,
    # which actually correspond to a nested structure, by defining a sorting function.
    # This simple function only requires the nodes ids.
    # We could provide node attributes in the third parameter.


    # We then generate a Rank_model object using Structify-net
    rank_nested = stn.Rank_model(NODES, r_nestedness)

    # A way to visualize the resulting structure is to plot the node pairs order
    # as a matrix
    fig = plt.figure(figsize=(4, 4), dpi=80)

    # Apply Seaborn default theme
    sns.set_theme()

    # viz._plot_rank_matrix() retourne une heatmap Seaborn
    # mais Rank_model.plot_matrix() ne la retourne pas
    # implicitement Jupyter l'affiche
    matrix_axes = rank_nested.plot_matrix()

    # UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
    # Pb de backend d'affichage, voir seaborn_example.py
    # plt.show()
    plt.savefig("rank_nested_matrix.png")

    # Step 3: Edge probability definition

    # Now that we know which node pairs are the most likely to appear,
    # we need to define a function $f$ that assign edge probabilities on each node pair,
    # byrespecting some constraints:

    # * The expected number of edges must be equal to the chosen parameter `m`,
    # i.e. $\sum_{u,v\in G}f(rank(u,v))=m$
    # * For any two node pairs $e_1$ and $e_2$,
    #   if $rank(e_1)>rank(e_2)$,
    #   then $f(e_1)\geq f(e_2)$

    # Although any such function can be provided, Structify-net provides a convenient
    # function generator, using a constraint parameter $\epsilon \in [0,1]$,
    # such as 0 corresponds to a deterministic structure,
    # the m pairs of highest rank being connected by an edge,
    # while 1 corresponds to a fully random network.

    probas = rank_nested.get_generator(epsilon=0.5,m=EDGES)

    # We can plot the probability as a function of rank for various values of `epsilon`

    fig, ax = plt.subplots()
    for epsilon in np.arange(0,1.1,1/6):
        probas = rank_nested.get_generator(epsilon=epsilon,m=EDGES)
        elt = probas.plot_proba_function(ax=ax)
        #elt=viz.plot_proba_function(probas,ax=ax)
        elt[-1].set_label(format(epsilon, '.2f'))
        #fig_tem.plot(label="pouet"+str(epsilon))
    ax.legend(title=r"$\epsilon$")

    # plt.show()
    plt.savefig("rank_nested_probas.png")

    # Step 4: Generate a graph from edge probabilities

    generator = rank_nested.get_generator(epsilon=0.5,m=EDGES)
    g_generated = generator.generate()

    adjacency_matrix_axes = stn.viz.plot_adjacency_matrix(g_generated)

    # plt.show()
    plt.savefig("rank_nested_adjacency_matrix.png")
