"""
$ time python examples/zoo_sort_distances.py

$ python3 -X importtime examples/zoo_sort_distances.py
"""

from structify_net.zoo import sort_distances

if __name__ == "__main__":
    # Voir PCI_article.ipynb

    # Returns a Rand_model
    rank = sort_distances(128)

    # sort_distances n'appelle pas _assign_nominal_attributes avec les bons
    # paramètres et on a encore de la reconstruction de graphe partout
