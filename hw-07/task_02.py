from tree import AVLNode, create_tree


def find_min(node: AVLNode) -> int:
    current = node
    while current.left is not None:
        current = current.left
    return current.key


def main() -> None:
    keys = [9, 5, 10, 14, 0, 6, 11, 18, -1, 1, -4, 2]

    root = create_tree(keys)

    print(root)

    print(find_min(root))


if __name__ == "__main__":
    main()
