import networkx as nx


def dijkstra(graph: nx.Graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    previous_nodes = {node: None for node in graph.nodes}
    distances[start] = 0
    unvisited = list(graph.nodes)
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex

        visited.append(current_vertex)
        unvisited.remove(current_vertex)

    return distances, previous_nodes


def get_shortest_path(previous_nodes, start, target):
    path = []
    node = target

    while node is not None:
        path.append(node)
        node = previous_nodes[node]

    path = path[::-1]
    if path[0] == start:
        return path
    else:
        return None


def main():
    # Створення графа
    G = nx.Graph()
    cities = [
        "Kyiv", "Warshaw", "Budapesht", "Sofia", "Athena",
        "Belgrad", "Praha", "Berdychiv", "Berlin", "Vien",
        "Vilnus", "Tirana", "London", "Roma", "Paris", "Bonn"

    ]
    G.add_nodes_from(cities)
    connections = [
        ("Kyiv", "Warshaw", 1200), ("Kyiv", "Sofia", 1600), ("Kyiv", "Athena", 2800),
        ("Kyiv", "Belgrad", 3000), ("Kyiv", "Berdychiv", 300), ("Kyiv", "Roma", 3500),
        ("Kyiv", "Berlin", 3500), ("Kyiv", "London", 6000), ("Kyiv", "Vilnus", 1600),
        ("Kyiv", "Athena", 2800), ("Belgrad", "Roma", 500), ("Belgrad", "Paris", 1200),
        ("Berdychiv", "Tirana", 3200), ("Berdychiv", "Vien", 2800), ("London", "Paris", 1000),
        ("Berdychiv", "Paris", 5000), ("Sofia", "Roma", 1700), ("Sofia", "Bonn", 2200),
        ("Athena", "Vien", 1700), ("Athena", "Bonn", 1900), ("Berdychiv", "Roma", 3200),
        ("Berdychiv", "Vilnus", 2350), ("Berdychiv", "Athena", 3000), ("London", "Vilnus", 4700),
        ("Praha", "Bonn", 1200), ("Berlin", "Tirana", 900),
        ("Praha", "Tirana", 400), ("Berlin", "Vien", 700),
        ("Budapesht", "Roma", 750), ("Budapesht", "Athena", 600),
        ("Budapesht", "Athena", 600)
    ]
    for conn in connections:
        G.add_edge(conn[0], conn[1], weight=conn[2])

    start_node = "Berdychiv"
    distances, previous_nodes = dijkstra(G, start_node)

    for target_node in cities:
        if distances[target_node] == 0:
            continue
        path = get_shortest_path(previous_nodes, start_node, target_node)
        print(f"The shortest path from {start_node} to {target_node}: {path} is {distances[target_node]} long")


if __name__ == "__main__":
    main()
