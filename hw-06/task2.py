import networkx as nx
from collections import deque


def dfs(graph: nx.Graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            visited = dfs(graph, neighbor, visited)
    return visited


def bfs(graph: nx.Graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.pop()
        if node not in visited:
            visited.append(node)
            neighbors = list(graph.neighbors(node))
            for neighbor in neighbors:
                queue.append(neighbor)
    return visited


def main():
    G = nx.Graph()
    cities = [
        "Kyiv", "Warshaw", "Budapesht", "Sofia", "Athena",
        "Belgrad", "Praha", "Berdychiv", "Berlin", "Vien",
        "Vilnus", "Tirana", "London", "Roma", "Paris", "Bonn"

    ]
    G.add_nodes_from(cities)
    connections = [
        ("Kyiv", "Warshaw"), ("Kyiv", "Sofia"), ("Kyiv", "Athena"),
        ("Kyiv", "Belgrad"), ("Kyiv", "Berdychiv"), ("Kyiv", "Roma"),
        ("Kyiv", "Berlin"), ("Kyiv", "London"), ("Kyiv", "Vilnus"),
        ("Kyiv", "Athena"), ("Belgrad", "Roma"), ("Belgrad", "Paris"),
        ("Berdychiv", "Tirana"), ("Berdychiv", "Vien"), ("London", "Paris"),
        ("Berdychiv", "Paris"), ("Sofia", "Roma"), ("Sofia", "Bonn"),
        ("Athena", "Vien"), ("Athena", "Bonn"), ("Berdychiv", "Roma"),
        ("Berdychiv", "Vilnus"), ("Berdychiv", "Athena"), ("London", "Vilnus"),
        ("Praha", "Bonn"), ("Berlin", "Tirana"),
        ("Praha", "Tirana"), ("Berlin", "Vien"),
        ("Budapesht", "Roma"), ("Budapesht", "Athena"),
        ("Budapesht", "Athena")
    ]
    G.add_edges_from(connections)

    start_node = "Berdychiv"
    dfs_path = dfs(G, start_node)
    bfs_path = bfs(G, start_node)
    print("Comparison of the paths DFS та BFS:")
    print("DFS path: ", dfs_path)
    print("BFS path: ", bfs_path)
    difference = set(dfs_path) ^ set(bfs_path)
    print(f"difference: {difference}")


if __name__ == "__main__":
    main()
