"""
**structify-net** is a Python library for generating networks with customizable
structures, node counts, and link numbers.

It provides a unified framework to model various network structures, 
including community/bloc structures, spatial structures, and more.

A structure is defined by:

- The number of nodes `n`
- A ranking of all node pairs, from most likely to least likely to be connected
"""

from structify_net.structureClasses import Rank_model, Graph_generator

__all__ = ["Rank_model", "Graph_generator"]
