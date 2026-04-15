# Theorie des graphes - Algorithme de DIJKSTRA
import heapq 
class Graphe(object) :
    def __init__(self) :
        self.adjacence = {} 
    
    def add_edge(self, u, v, weight) :
        self.adjacence.setdefault(u, []).append((v, weight))
        self.adjacence.setdefault(v, []).append((u, weight))

    def dijkstra(self, start) :
        if start not in self.adjacence :
            raise KeyError(f"le sommet '{start}' n'appartient pas au graphe .")
        distances = {n :float('inf') for n in self.adjacence} # distances c'est la distance de start à un sommet 
                                                              # on considere qu'elle est infinie pour chaque sommet 
        previous = {m :None for m in self.adjacence}          # on cree une 'liste' de sommets parcourus                                           
        distances[start] = 0                                  # le distance du point de depart est nulle
        priority_q = [(0, start)] 

        while priority_q :
            min_dist, u = heapq.heappop(priority_q) # recupération de la distance min connue de start à un sommet u   

            if min_dist > distances[u] :
                continue 

            for v, weight in self.adjacence[u] :                  # pour chaque sommet adjacent à u 
                if ( min_dist + weight < distances[v] ) :         # si la distance de start à v (un sommet adjacent à u)
                                                            # est > min_dist + weight(poids de l'arete u-v) 
                    distances[v] = min_dist + weight  # on actualise la distance de start à v 
                    previous[v] = u 
                    heapq.heappush(priority_q, (distances[v], v))

        return distances, previous 
    
    
    def get_path(self,distances, previous, target) :
        """
         chargee de reconstituer le chemin 
         """

        if target not in previous :
            raise KeyError(f"le sommet '{target}' n'appartient pas au graphe .")
        if distances[target] == float('inf') :
            return [] 
        path = []
        current = target  
        
        while current is not None :
            path.append(current)
            current = previous[current] 
        path.reverse()

        return path
    
    def display(self, path) :
        if not path :
            return "no path found"
        
        return "->".join(str(s) for s in path)   

    def display_adjacence(self):
        """Affiche la table d'adjacence du graphe."""
        for sommet, voisins in self.adjacence.items():
            voisins_str = ", ".join(f"{v}(poids:{w})" for v, w in voisins)
            print(f"{sommet} : [{voisins_str}]")