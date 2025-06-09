
import heapq

# Custom graph representation
graph = {
    "Київ": [("Львів", 3), ("Харків", 2), ("Одеса", 5), ("Дніпро", 4)],
    "Львів": [("Київ", 3), ("Харків", 4), ("Одеса", 6), ("Дніпро", 7)],
    "Харків": [("Київ", 2), ("Львів", 4), ("Одеса", 3), ("Дніпро", 1)],
    "Одеса": [("Київ", 5), ("Львів", 6), ("Харків", 3), ("Дніпро", 2)],
    "Дніпро": [("Київ", 4), ("Львів", 7), ("Харків", 1), ("Одеса", 2)],
}

# Custom Dijkstra's algorithm
def dijkstra_path(graph, start, goal):
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))
    return None, float('inf')

print("\n--- Алгоритм Дейкстри: найкоротші шляхи від Київ ---")
for city in graph:
    if city != "Київ":
        path, length = dijkstra_path(graph, "Київ", city)
        print(f"Київ → {city}: шлях = {path}, вага = {length}")