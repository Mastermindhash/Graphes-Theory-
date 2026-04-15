# test_graphe.py
from graphe import Graphe

def test_dijkstra_real_case():
    """
    Scenario: Finding the shortest driving route between European cities.
    Distances are approximated in kilometers.
    """
    geo_graph = Graphe()

    # Cities and distances (edges)
    # Paris as the central hub
    geo_graph.add_edge('Paris', 'Brussels', 312)
    geo_graph.add_edge('Paris', 'Lyon', 460)
    geo_graph.add_edge('Paris', 'London', 456)
    
    # Other connections
    geo_graph.add_edge('Brussels', 'Amsterdam', 210)
    geo_graph.add_edge('Brussels', 'London', 320)
    geo_graph.add_edge('Lyon', 'Milan', 440)
    geo_graph.add_edge('Milan', 'Rome', 570)
    geo_graph.add_edge('Amsterdam', 'Berlin', 655)
    geo_graph.add_edge('Milan', 'Berlin', 1035)

    print("--- Dijkstra Algorithm Test: European Road Network ---")
    
    # 1. Calculate distances from London
    start_city = 'London'
    destination = 'Rome'
    
    distances, previous = geo_graph.dijkstra(start_city)
    
    # 2. Get the specific path to Rome
    path = geo_graph.get_path(distances, previous, destination)
    
    # 3. Display Results
    print(f"Origin: {start_city}")
    print(f"Destination: {destination}")
    print(f"Path: {geo_graph.display(path)}")
    print(f"Total Distance: {distances[destination]} km")
    
    print("\n--- Full Distance Table from London ---")
    for city, dist in sorted(distances.items(), key=lambda x: x[1]):
        print(f"{city:10} : {dist} km")

if __name__ == "__main__":
    test_dijkstra_real_case()
