
def binary_search(arry, target):
    binary_search.counter = 0

    def _binary_search(arr, test):
        binary_search.counter += 1
        center = len(arr) // 2
        if arr[center] == test:
            return arr[center]
        elif arr[center] > test:
            chunk = arr[0:center]
        else:
            chunk = arr[center + 1: len(arr)]
        if len(chunk) == 1:
            return chunk[0]
        elif len(chunk) == 2:
            return chunk[1]
        else:
            return _binary_search(chunk, test)

    return _binary_search(arry, target), binary_search.counter


def main():
    sorted_array = [-7, -0.5, 0.0, 0.1, 0.3, 0.5, 1.1, 2.0, 2.3, 3.7, 4.4, 5.5]

    print(binary_search(sorted_array, -9))  #-7, 3
    print(binary_search(sorted_array, -3))  #-7, 3
    print(binary_search(sorted_array, 0))  #0.0, 3
    print(binary_search(sorted_array, 0.1))  #0.1, 2
    print(binary_search(sorted_array, 2.3))  #2.3, 2
    print(binary_search(sorted_array, 6))  #5.5, 2


if __name__ == "__main__":
    main()
