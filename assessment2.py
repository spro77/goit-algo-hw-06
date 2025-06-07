import networkx as nx

# Побудова графа (як у assessment1.py)
G = nx.Graph()
G.add_edges_from([
    ("Київ", "Львів"),
    ("Київ", "Харків"),
    ("Київ", "Одеса"),
    ("Київ", "Дніпро"),
    ("Львів", "Харків"),
    ("Львів", "Одеса"),
    ("Львів", "Дніпро"),
    ("Харків", "Одеса"),
    ("Харків", "Дніпро"),
    ("Одеса", "Дніпро")
])

# Алгоритм DFS
dfs_tree = nx.dfs_tree(G, source="Київ")
dfs_path = nx.shortest_path(dfs_tree, source="Київ", target="Одеса")
print(f"DFS шлях від Київ до Одеса: {dfs_path}")

# Алгоритм BFS
bfs_path = list(nx.shortest_path(G, source="Київ", target="Одеса"))
print(f"BFS шлях від Київ до Одеса: {bfs_path}")