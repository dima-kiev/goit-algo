import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.nodes = set()

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))
        
        # Додаємо вершини до множини
        self.nodes.add(from_node)
        self.nodes.add(to_node)

    def dijkstra(self, start):
        # Ініціалізація відстаней до всіх вершин як нескінченність
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0

        # Ініціалізація черги
        priority_queue = [(0, start)]
        heapq.heapify(priority_queue)

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Якщо знайдена краща відстань, пропускаємо
            if current_distance > distances[current_node]:
                continue

            # Оновлюємо відстані до сусідніх вершин
            for neighbor, weight in self.edges.get(current_node, []):
                distance = current_distance + weight

                # Якщо знайдена краща відстань до сусіда, оновлюємо його
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

def main():
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    start_node = 'A'
    distances = g.dijkstra(start_node)
    print(f"Найкоротші відстані від вершини {start_node}:")
    for node, distance in distances.items():
        print(f"Відстань до {node}: {distance}")

if __name__ == "__main__":
    main()
