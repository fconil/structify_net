"""
J'ai peut-être mal jugé le test que Copilot a produit.

Je m'attendais à ce qu'il m'aide à vérifier que à partir de valeurs définies,
les tests vérifient la validité des calculs.

Le "mock" de la classe Rank_model ne correspond pas à ce qui est fait dans __init__, mais :

1. Il permet de vérifier qu'un graphe a été créé à partir d'un entier
2. Le nombre de noeuds correspond à l'entier créé, utiliser
   model.g.number_of_nodes() plutôt que len(model.g.nodes) == n
3. Il vérifie que tous les noeuds ont bien un attribut "d1"
4. Il récupère la fonction "sort_function", l'exécute sur les noeuds 0 et 1 et
   vérifie qu'il récupère une valeur réelle

Cela ne teste pas la validité du résultat mais la bonne exécution de certaines parties. 

---

ok oui ça me semble pertinent aussi.

J’ai l’impression qu’il y a vraiment 2 types de tests unitaires, ceux dont le
but est de passer dans le plus grand pourcentage du code et ceux qui vérifient
la logique sous-jacente. Pour avoir les petits badges dans github avec des taux
de tests j’ai l’impression que c’est la première catégorie qui compte, et j’ai
l’impression qu’il se concentre sur ça.

Je pense que c’est déjà bien. Après un autre type de tests unitaires pourrait
être de transposer les notebooks déja fait. L’avantage est que ça consiste en
un usage en utilisation réelle. Là aussi un LLM doit pouvoir faire cette
traduction de manière automatique assez facilement ? (Chaque bloc du notebook
peut donner lieu à une fonction de test…).
"""

import pytest
import networkx as nx
import numpy as np
# from unittest import mock

from structify_net.zoo import sort_core_distance

# src/structify_net/test_zoo.py


# 1. Il a importé unittest.mock mais il utilise la fixture builtin pytest.monkeypatch
@pytest.fixture
def mock_rank_model(monkeypatch):
    class DummyRankModel:
        def __init__(self, g, rank_fn, sort_descendent=False, node_order_function=None):
            self.g = g
            self.rank_fn = rank_fn
            self.sort_descendent = sort_descendent
            self.node_order_function = node_order_function
    monkeypatch.setattr("structify_net.structureClasses.Rank_model", DummyRankModel)
    return DummyRankModel

# 2. Pas sûre que ce test soit utile
#    2.a. L'appel de rank_fn n'a pas de sens
#         sort_core_distance a sa propre node_order_function sur la propriété "d1"
#         elle n'utilise pas la 
def test_sort_core_distance_with_int_nodes(monkeypatch, mock_rank_model):
    n = 5
    model = sort_core_distance(n)
    assert hasattr(model, "g")
    assert len(model.g.nodes) == n
    # Check dimension attribute exists
    for node in model.g.nodes:
        assert "d1" in model.g.nodes[node]
    # Check rank function returns a float
    val = model.rank_fn(0, 1, model.g)
    assert isinstance(val, float)

def test_sort_core_distance_with_graph(monkeypatch, mock_rank_model):
    g = nx.Graph()
    g.add_nodes_from(range(4))
    model = sort_core_distance(g, dimensions=2)
    assert len(model.g.nodes) == 4
    for node in model.g.nodes:
        assert "d1" in model.g.nodes[node]
        assert "d2" in model.g.nodes[node]
    val = model.rank_fn(0, 1, model.g)
    assert isinstance(val, float)

def test_sort_core_distance_custom_distance(monkeypatch, mock_rank_model):
    def manhattan(u, v):
        return float(np.sum(np.abs(np.array(u) - np.array(v))))
    n = 3
    model = sort_core_distance(n, dimensions=2, distance=manhattan)
    val = model.rank_fn(0, 1, model.g)
    assert isinstance(val, float)

def test_sort_core_distance_node_order(monkeypatch, mock_rank_model):
    n = 6
    model = sort_core_distance(n, dimensions=1)
    order = model.node_order_function(model.g)
    # Should be sorted by "d1"
    d1s = [model.g.nodes[n]["d1"] for n in order]
    assert d1s == sorted(d1s)
