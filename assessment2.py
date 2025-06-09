from collections import deque


def dfs_path(graph, start, goal):
    visited = set()
    stack = [(start, [start])]

    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None


def bfs_path(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None


graph = {
    "Київ": ["Львів", "Харків", "Одеса", "Дніпро"],
    "Львів": ["Київ", "Харків", "Одеса", "Дніпро"],
    "Харків": ["Київ", "Львів", "Одеса", "Дніпро"],
    "Одеса": ["Київ", "Львів", "Харків", "Дніпро"],
    "Дніпро": ["Київ", "Львів", "Харків", "Одеса"]
}


weighted_graph = {
    "Київ": [("Львів", 1), ("Харків", 2), ("Одеса", 3), ("Дніпро", 4)],
    "Львів": [("Київ", 1), ("Харків", 1), ("Одеса", 2), ("Дніпро", 3)],
    "Харків": [("Київ", 2), ("Львів", 1), ("Одеса", 1), ("Дніпро", 1)],
    "Одеса": [("Київ", 3), ("Львів", 2), ("Харків", 1), ("Дніпро", 2)],
    "Дніпро": [("Київ", 4), ("Львів", 3), ("Харків", 1), ("Одеса", 2)]
}


dfs_result = dfs_path(graph, "Київ", "Одеса")
print(f"DFS шлях від Київ до Одеса: {dfs_result}")

bfs_result = bfs_path(graph, "Київ", "Одеса")
print(f"BFS шлях від Київ до Одеса: {bfs_result}")
