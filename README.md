# Graphs Theory — Dijkstra Algorithm

A Python implementation of **Dijkstra's shortest path algorithm** 
using an adjacency table representation.

## Files

| File | Description |
|------|-------------|
| `graphe.py` | `Graphe` class — core module |
| `test-graphe.py` | Interactive menu to test the implementation |

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
g.add_edge('A', 'B', 2)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'D', 3)
g.add_edge('C', 'D', 1)

distances, previous = g.dijkstra('A')
path = g.get_path(distances, previous, 'D')

print(g.display(path))       # A -> B -> D
print("Distance :", distances['D'])  # Distance : 5
```
