import heapq

import networkx as nx
import matplotlib.pyplot as plt


# Створення власного вагового графа 
G = nx.Graph()
G.add_edge("A", "B", weight=10)
G.add_edge("B", "C", weight=3)
G.add_edge("C", "D", weight=5)
G.add_edge("С", "H", weight=1)
G.add_edge("С", "T", weight=2)
G.add_edge("С", "N", weight=1)
G.add_edge("С", "E", weight=9)
G.add_edge("N", "D", weight=8)
G.add_edge("M", "B", weight=15)
G.add_edge("D", "T", weight=8)
G.add_edge("A", "M", weight=6)

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > shortest_paths[current_vertex]:
            continue
        for neighbor, edge_data in graph[current_vertex].items():
            weight = edge_data['weight']
            distance = current_distance + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return shortest_paths


# Використання алгоритму Дейкстри
shortest_paths = dijkstra(G, "A")
print(shortest_paths)

# Візуалізація графа
pos = nx.spring_layout(G)  # Positions for all nodes
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=2)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

plt.axis("off")
plt.show()
