from linked_list import LinkedList, Node

def reverse_linked_list(list: LinkedList):
    """
    Реверсування однозв'язного списку
    """
    prev = None
    current = list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    list.head = prev
    

def __get_middle(head: Node | None) -> Node | None:
    if head is None:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def __sorted_merge(left: Node | None, right: Node | None) -> Node:
    if left is None:
        return right
    if right is None:
        return left

    dummy_node = Node()
    tail = dummy_node

    while left and right:
        if left.data <= right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    if left:
        tail.next = left
    else:
        tail.next = right

    return dummy_node.next
    
def merge_sort_linked_list(list: LinkedList) -> LinkedList:
    copy = LinkedList()
    cur = list.head
    while cur:
        copy.insert_at_end(cur.data)
        cur = cur.next
        
    if copy.head is None or copy.head.next is None:
        return copy
    
    middle = __get_middle(copy.head)
    next_to_middle = middle.next

    middle.next = None

    left = LinkedList()
    right = LinkedList()
    left.head = copy.head
    right.head = next_to_middle

    left = merge_sort_linked_list(left)
    right = merge_sort_linked_list(right)

    sorted_list = LinkedList()
    sorted_list.head = __sorted_merge(left.head, right.head)

    return sorted_list

def merge_sorted_lists(list1: LinkedList, list2: LinkedList):
    result = LinkedList()
    result.head = __sorted_merge(list1.head, list2.head)
    return result

def main():
    # Створення списків
    list1 = LinkedList()
    list1.insert_at_end(3)
    list1.insert_at_end(1)
    list1.insert_at_end(5)

    list2 = LinkedList()
    list2.insert_at_end(4)
    list2.insert_at_end(2)
    list2.insert_at_end(6)
 
    print("Cписок 1:", list1)
    print("Cписок 2:", list2)

    # Реверсування списку
    reverse_linked_list(list1)
    print("Реверсований список:", list1)

    # Сортування спискid
    sorted_list_1 = merge_sort_linked_list(list1)
    print("Відсортований список 1:", sorted_list_1)
    sorted_list_2 = merge_sort_linked_list(list2)
    print("Відсортований список 2:", sorted_list_2)

    # Об'єднання двох списків
    merged_list = merge_sorted_lists(sorted_list_1, sorted_list_2)
    print("Об'єднання двох списків:", merged_list)
 
    print("Cписок 1:", list1)
    print("Cписок 2:", list2)
    


if __name__ == "__main__":
    main()