import networkx as nx

G_weighted = nx.Graph()

# Додавання зважених ребер
weighted_edges = [
    ("Київ", "Львів", 3),
    ("Київ", "Харків", 2),
    ("Київ", "Одеса", 5),
    ("Київ", "Дніпро", 4),
    ("Львів", "Харків", 4),
    ("Львів", "Одеса", 6),
    ("Львів", "Дніпро", 7),
    ("Харків", "Одеса", 3),
    ("Харків", "Дніпро", 1),
    ("Одеса", "Дніпро", 2),
]

G_weighted.add_weighted_edges_from(weighted_edges)

print("\n--- Алгоритм Дейкстри: найкоротші шляхи від Київ ---")
for city in G_weighted.nodes:
    if city != "Київ":
        path = nx.dijkstra_path(G_weighted, source="Київ", target=city)
        length = nx.dijkstra_path_length(G_weighted, source="Київ", target=city)
        print(f"Київ → {city}: шлях = {path}, вага = {length}")