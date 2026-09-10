def max_items_two_types(items: list[int]) -> int:
    left = 0
    counts = {}
    best = 0

    for right, item in enumerate(items):
        counts[item] = counts.get(item, 0) + 1

        while len(counts) > 2:
            left_item = items[left]
            counts[left_item] -= 1
            if counts[left_item] == 0:
                del counts[left_item]
            left += 1

        best = max(best, right - left + 1)

    return best

items = [1, 2, 1]
print(max_items_two_types(items))