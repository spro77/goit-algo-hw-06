import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("Київ")
G.add_node("Львів")
G.add_node("Харків")
G.add_node("Одеса")
G.add_node("Дніпро")

G.add_edge("Київ", "Львів", weight=550)   # відстань у км
G.add_edge("Київ", "Харків", weight=480)
G.add_edge("Київ", "Одеса", weight=480)
G.add_edge("Київ", "Дніпро", weight=470)
G.add_edge("Львів", "Харків", weight=890)
G.add_edge("Львів", "Одеса", weight=980)
G.add_edge("Львів", "Дніпро", weight=750)
G.add_edge("Харків", "Одеса", weight=550)
G.add_edge("Харків", "Дніпро", weight=330)
G.add_edge("Одеса", "Дніпро", weight=470)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', font_size=10, font_weight='bold', node_size=500, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Транспортна мережа міста")
plt.show()

# Аналіз основних характеристик
print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")

degrees = dict(G.degree())
print(f"Ступінь вершин: {degrees}")