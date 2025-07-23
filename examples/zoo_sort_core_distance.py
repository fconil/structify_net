"""
$ time python examples/zoo_sort_core_distance.py

$ python3 -X importtime examples/zoo_sort_core_distance.py
"""

from structify_net.zoo import sort_core_distance

if __name__ == "__main__":
    # Returns a Rand_model
    r_model = sort_core_distance(10)

    print (r_model.node_properties.number_of_nodes())
    
