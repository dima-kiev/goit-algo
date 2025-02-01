import heapq


def min_cables_connection_cost(cables):
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        combined = first + second

        total_cost += combined

        heapq.heappush(cables, combined)

    return total_cost


def main() -> None:
    cables = [4, 3, 2, 6, 10]

    cost = min_cables_connection_cost(cables)

    print("Мінімальні витрати на об'єднання кабелів:", cost)


if __name__ == "__main__":
    main()
