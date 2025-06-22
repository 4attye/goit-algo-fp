import networkx as nx
import heapq


def dijkstra(G, start):
    # Ініціалізуємо відстані до всіх вузлів як нескінченність
    distances = {vertex: float('inf') for vertex in G.nodes()}
    distances[start] = 0

    # Ініціалізуємо бінарну купу (heap)
    heap = [(0, start)]

    while heap:
        # Дістаємо вершину з найменшою поточною відстанню
        current_distance, current_node = heapq.heappop(heap)

        # Якщо вже маємо кращий шлях, пропускаємо
        if current_distance > distances[current_node]:
            continue

        # Перебираємо всіх сусідів поточної вершини
        for neighbor in G.neighbors(current_node):
            weight = G[current_node][neighbor].get('weight', 1)
            distance = current_distance + weight

            # Якщо знайдено кращий шлях до сусіда, оновлюємо відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


if __name__ == "__main__":
    # Створюємо граф з вагами
    G = nx.Graph()
    G.add_weighted_edges_from([
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
        ('D', 'Z', 6),
        ('E', 'Z', 3)
    ])

    # Стартрва вершина
    start = 'A'
    shortest_paths = dijkstra(G, start)

    # Виводимо найкоротші шляхи до кожної вершини
    print(f"Найкоротші шляхи від вершини {start}:")
    for vertex, distance in shortest_paths.items():
        print(f"{start} -> {vertex}: {distance}")

print(dijkstra(G, 'A'))