"""
https://stepik.org/lesson/13238/step/10?unit=3424
"""
def max_items_cost(n: int, backpack_weight: int, items) -> float:
    # сортировка предметов по удельной стоимости
    sorted_items = sorted(items, key=lambda item: item[0] / item[1], reverse=True)
    i, cost, weight = 0, 0, 0
    while i < n and weight < backpack_weight:
        item = sorted_items[i]
        item_suitable_kgs = item[1]
        while weight + item_suitable_kgs > backpack_weight:
            item_suitable_kgs -= 1
        cost += item[0] / item[1] * item_suitable_kgs
        weight += item_suitable_kgs
        i += 1
    return round(cost, 3)


if __name__ == "__main__":
    n, backpack_weight = map(int, input().split())
    items = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    cost = max_items_cost(n, backpack_weight, items)
    print(cost)