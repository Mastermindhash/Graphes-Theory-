# Graph Theory - Dijkstra's algorithm 
import heapq

class Graphe(object):
    """
    A class representing an undirected weighted graph and providing 
    tools for shortest path calculations using Dijkstra's algorithm.
    """

    def __init__(self):
        """
        Initializes an empty graph with an adjacency list representation.
        """
        self.adjacence = {}

    def add_edge(self, u, v, weight):
        """
        Adds an undirected weighted edge between two vertices.

        Args:
            u: The starting vertex.
            v: The ending vertex.
            weight (int, float): The weight/distance of the edge.
        """
        self.adjacence.setdefault(u, []).append((v, weight))
        self.adjacence.setdefault(v, []).append((u, weight))

    def dijkstra(self, start):
        """
        Computes the shortest paths from a starting vertex to all other 
        reachable vertices in the graph.

        Args:
            start: The source vertex for the calculation.

        Returns:
            tuple: A pair of dictionaries (distances, previous).
                   - distances: Maps each node to its minimum distance from 'start'.
                   - previous: Maps each node to its immediate predecessor in the shortest path.
        """
        distances = {n: float('inf') for n in self.adjacence}
        previous  = {n: None        for n in self.adjacence}
        distances[start] = 0
        priority_q = [(0, start)]

        while priority_q:
            min_dist, u = heapq.heappop(priority_q)
            
            # Optimization: skip if a shorter path to u has already been processed
            if min_dist > distances[u]:
                continue
                
            for v, weight in self.adjacence[u]:
                if min_dist + weight < distances[v]:
                    distances[v] = min_dist + weight
                    previous[v]  = u
                    heapq.heappush(priority_q, (distances[v], v))

        return distances, previous

    def get_path(self, distances, previous, target):
        """
        Reconstructs the shortest path from the source to a target vertex.

        Args:
            distances (dict): Dictionary of distances calculated by dijkstra().
            previous (dict): Dictionary of predecessors calculated by dijkstra().
            target: The destination vertex.

        Returns:
            list: An ordered list of vertices representing the path from source to target.
        
        Raises:
            KeyError: If the target vertex does not exist in the graph.
        """
        if target not in previous:
            raise KeyError(f"The vertex '{target}' does not exist in the graph.")
        if distances[target] == float('inf'):
            return []
            
        path    = []
        current = target
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        return path

    def display(self, path):
        """
        Formats a list of vertices into a readable string representation.

        Args:
            path (list): A list of vertices representing a path.

        Returns:
            str: A string showing the path joined by arrows (e.g., 'A -> B -> C').
        """
        if not path:
            return "No path found."
        return " -> ".join(str(s) for s in path)

# END OF FILE
