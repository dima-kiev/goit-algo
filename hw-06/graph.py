import networkx as nx
import matplotlib.pyplot as plt


def main():
    g = nx.Graph()

    cities = [
        "Kyiv", "Warshaw", "Budapesht", "Sofia", "Athena",
        "Belgrad", "Praha", "Berdychiv", "Berlin", "Vien",
        "Vilnus", "Tirana", "London", "Roma", "Paris", "Bonn"

    ]
    g.add_nodes_from(cities)

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
    g.add_edges_from(connections)

    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(g, seed=42)
    nx.draw(g, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold")
    plt.title("All the rads go to Berdychiv. Proofed")
    plt.show()

    num_nodes = g.number_of_nodes()
    num_edges = g.number_of_edges()
    degree_of_nodes = dict(g.degree())

    print(f"Vertexes: {num_nodes}")
    print(f"Edges: {num_edges}")
    print("Each edge pow:")
    for node, degree in degree_of_nodes.items():
        print(f"{node}: {degree}")


if __name__ == "__main__":
    main()
