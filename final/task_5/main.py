import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph: nx.DiGraph, node: Node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap_root: Node):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def create_heap_from_list(elements):
    if not elements:
        return None

    # Використання heapq для створення мін-купа
    heapq.heapify(elements)
    
    # Перебудова купи у бінарне дерево
    nodes = [Node(key) for key in elements]
    n = len(nodes)

    # Побудова бінарного дерева з масиву
    for i in range(n):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < n:
            nodes[i].left = nodes[left_index]
        if right_index < n:
            nodes[i].right = nodes[right_index]

    return nodes[0]

def depth_first_search(root):
    stack = [root]
    visited = set()
    order = []

    while stack:
        node = stack.pop()
        if node and node not in visited:
            visited.add(node)
            order.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
    return order

def breadth_first_search(root):
    queue = deque([root])
    visited = set()
    order = []

    while queue:
        node = queue.popleft()
        if node and node not in visited:
            visited.add(node)
            order.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return order

def assign_colors(nodes, start_color="#444444", end_color="#eeeeee"):
    def interpolate_color(start, end, factor):
        start = [int(start[i:i+2], 16) for i in (1, 3, 5)]
        end = [int(end[i:i+2], 16) for i in (1, 3, 5)]
        return f"#{int(start[0] + (end[0] - start[0]) * factor):02X}{int(start[1] + (end[1] - start[1]) * factor):02X}{int(start[2] + (end[2] - start[2]) * factor):02X}"

    n = len(nodes)
    for i, node in enumerate(nodes):
        color = interpolate_color(start_color, end_color, i / (n - 1))
        node.color = color

def main():
    # Тестування

    # Список елементів для бінарної купи
    elements = [2, 4, 1, 12, 9, 8, 6, 5]

    # Створення купи з елементів
    heap_root = create_heap_from_list(elements)

    # Візуалізація обходу DFS
    dfs_order = depth_first_search(heap_root)
    assign_colors(dfs_order, "#05b4f8", "#d7f0f9")
    print("DFS Order:")
    draw_heap(heap_root)

    # Візуалізація обходу BFS
    bfs_order = breadth_first_search(heap_root)
    assign_colors(bfs_order, "#ba01ff", "#f4e2fb")
    print("BFS Order:")
    draw_heap(heap_root)

if __name__ == "__main__":
    main()
