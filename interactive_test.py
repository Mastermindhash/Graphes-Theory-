from graphe import Graphe

g = Graphe()

while True:
    print("\n--- MENU ---")
    print("1. Ajouter une arête")
    print("2. Afficher le Graphe")
    print("3. Tester Dijkstra")
    print("4. Quitter")

    choix = input("Choix : ")

    if choix == "1":
        u = input("Sommet u : ")
        v = input("Sommet v : ")
        weight = float(input("Poids : ")) 
        g.add_edge(u, v, weight)
        print(f"Arête {u}-{v} ajoutée.")

    elif choix == "2":
        g.display_adjacence()

    elif choix == "3":
        start  = input("Sommet de départ : ")
        target = input("Sommet d'arrivée : ")
        distances, previous = g.dijkstra(start)
        path = g.get_path(distances, previous, target)
        print(g.display(path))
        print(f"Distance totale : {distances[target]}")

    elif choix == "4":
        print("A PLUS .")
        break

    else:
        print("CHOIX INVALIDE.")
