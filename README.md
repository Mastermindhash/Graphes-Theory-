# Graphs Theory — Dijkstra Algorithm

A Python implementation of **Dijkstra's shortest path algorithm** 
using an adjacency table representation.

## Files

| File | Description |
|------|-------------|
| `graphe.py` | `Graphe` class — core module |
| `interactive_test.py` | Interactive menu to test the implementation |
| `test_graph-real_case.py` | Real use case of the implementation |

## Class `Graphe` — Methods

- `add_edge(u, v, weight)` — adds an undirected weighted edge to the graph
- `dijkstra(start)` — computes shortest distances from `start` to all vertices; returns `(distances, previous)`
- `get_path(distances, previous, target)` — reconstructs the shortest path to `target`; returns a list
- `display(path)` — formats the path as a string with arrows `" -> "`
- `display_adjacence()` — prints the adjacency table of the graph

## Usage

```python
from graphe import Graphe 

g = Graphe()
g.add_edge('R', 'A', 9)                    # adding edges 
g.add_edge('R', 'U', 12)
g.add_edge('A', 'C', 5)
g.add_edge('A', 'U', 7)
g.add_edge('C', 'U', 9)
g.add_edge('C', 'H', 8)
g.add_edge('C', 'M', 14)

distances, previous = g.dijkstra('R')       # getting 2 dictionaries from dijkstra 
path = g.get_path(distances, previous, 'M') # finding the path 
print(g.display(path))                      # displaying path 
print(distances)                            # displaying distances between R and each vertex of g

```
