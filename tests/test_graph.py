# coding: utf-8
import networkx as nx
import numpy as np
import pytest
from faker import Faker

from structify_net.zoo import sort_core_distance

# =============================================================================
# First test to show with Faker
# =============================================================================


@pytest.fixture
def fake_graph():
    fake = Faker()

    # https://faker.readthedocs.io/en/master/index.html#seeding-the-generator
    Faker(5825)

    g = nx.Graph()

    colors = ['gray', 'white', 'yellow', 'fuchsia', 'silver', 'purple',
              'yellow', 'green', 'aqua', 'teal']

    for i in range(10):
        # Use a fixed color list, to be sure that when ordered by colors
        # the order of the nodes is not the order of the added nodes (0, 1, 2, …, 9)

        # color=fake.safe_color_name(),
        g.add_node(
            i,
            color=colors[i],
            age=fake.pyint(max_value=100),
            date=fake.date(),
        )

    # show data : https://networkx.org/documentation/stable/tutorial.html#node-attributes
    # g.nodes.data()

    return g


def test_sort_graph(fake_graph):
    """
    Test that node order changes after sort.

    Args:
        fake_graph (networkX graph): A graph with fake attributes
    """
    sorted_graph = sorted(fake_graph.nodes, key=lambda n: fake_graph.nodes[n]["color"])

    assert sorted_graph != list(fake_graph.nodes)


# =============================================================================
# What could be interesting as test graph ?
# Paramétrisation des fixtures (plusieurs tailles de graphes ?)
# - https://perso.liris.cnrs.fr/francoise.conil/les-tests-avec-pytest/#/36
# =============================================================================


@pytest.fixture
def int_graph():
    """
    Create a simple graph with integer nodes and attributes.

    Returns:
        networkX graph: A graph with integer nodes and attributes
    """
    g = nx.Graph()
    g.add_nodes_from(range(5))
    return g


# =============================================================================
# First manual tests of sort_core_distance
# Expliquer les attributs de Rank_model de src/structify_net/structureClasses.py :
# - self.node_properties : le graphe
# - self.node_order : les nodes (NodeView) éventuellement ordonnés avec node_order_function
# - self.sorted_pairs :
#   - crée toutes les combinaisons de 2 noeuds
#   -  … puis expliquer
# Ça fait pas mal de choses stockées ?
# =============================================================================
def test_sort_core_distance_from_int():
    r_model = sort_core_distance(10, dimensions=5)
    assert r_model.node_properties.number_of_nodes() == 10


def test_sort_core_distance_node_order(monkeypatch):
    def set_ordinal_attributes(n, d, g):
        l_dim = [f"d{i + 1}" for i in range(d)]
        # The node_order_function sorts on first dimension
        nx.set_node_attributes(
            g,
            {
                0: np.float64(0.5093166811590025),
                1: np.float64(0.4496117715217497),
                2: np.float64(0.3952370716742116),
                3: np.float64(0.30457813703916603),
                4: np.float64(0.9701433481839707),
                5: np.float64(0.5491798410768358),
                6: np.float64(0.12196318151973218),
                7: np.float64(0.5370223724413283),
                8: np.float64(0.31230704752321337),
                9: np.float64(0.743627734369157),
            },
            l_dim[0],
        )
        for i_dim in range(1, d):
            attributes = np.random.random(n)
            nx.set_node_attributes(
                g, {i: a for i, a in enumerate(attributes)}, l_dim[i_dim]
            )

        return g, l_dim

    monkeypatch.setattr(
        "structify_net.zoo._assign_ordinal_attributes", set_ordinal_attributes
    )
    r_model = sort_core_distance(10, dimensions=5)

    # node_order_function trie les noeuds selon "d1"
    assert list(r_model.node_order) == [6, 3, 8, 2, 1, 0, 7, 5, 9, 4]


# =============================================================================
# TODO : Tester Hypothesis
# https://hypothesis.readthedocs.io/en/latest/
# https://github.com/HypothesisWorks/hypothesis
# =============================================================================
