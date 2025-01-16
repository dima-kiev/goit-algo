import timeit
import random


def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr


def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])


def tim_sort(arr):
    min_run = 32
    n = len(arr)
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min(i + min_run - 1, (n - 1)))
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size
            end = min((start + size * 2 - 1), (n - 1))
            merged_array = merge(arr[start:midpoint], arr[midpoint:end + 1])
            arr[start:start + len(merged_array)] = merged_array
        size *= 2
    return arr


test_data = list(range(10))


def tim_sort_(x: list):
    random.shuffle(x)
    return tim_sort(x)


def insertion_sort_(x: list):
    random.shuffle(x)
    return insertion_sort(x)


def merge_(x):
    random.shuffle(x)
    len_1: int = len(x) % 2
    len_2: int = len(x) - len_1
    return merge(x[0:1], x[1:len(x)-1])


def sorted_(x: list):
    random.shuffle(x)
    return sorted(x)


def list_sort_(x: list):
    random.shuffle(x)
    x.sort()
    return x


def main():
    print('tim_sort(test_data) ' + str(timeit.timeit('tim_sort_(test_data)', globals=globals())))
    print(tim_sort_(test_data))

    print('insertion_sort(test_data) ' + str(timeit.timeit('insertion_sort_(test_data)', globals=globals())))
    print(insertion_sort_(test_data))

    print('merge(test_data) ' + str(timeit.timeit('merge_(test_data)', globals=globals())))
    print(merge_(test_data))

    print('python internal sorted() ' + str(timeit.timeit('sorted_(test_data)', globals=globals())))
    print(sorted_(test_data))

    print('python internal list.sort() ' + str(timeit.timeit('list_sort_(test_data)', globals=globals())))
    print(list_sort_(test_data))


if __name__ == '__main__':
    main()
