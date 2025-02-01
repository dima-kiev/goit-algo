from tree import AVLNode, create_tree


def find_max(node: AVLNode) -> int:
    current = node
    while current.right is not None:
        current = current.right
    return current.key


def main() -> None:
    keys = [9, 5, 10, 14, 0, 6, 11, 18, -1, 1, -4, 2]

    root = create_tree(keys)

    print(root)

    print(find_max(root))


if __name__ == "__main__":
    main()
