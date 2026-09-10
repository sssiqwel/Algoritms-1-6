def count_subarrays_with_sum(nums: list[int], k: int) -> int:
    prefix_sum = 0
    count = 0
    seen = {0: 1}

    for num in nums:
        prefix_sum += num
        count += seen.get(prefix_sum - k, 0)
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

    return count


nums = [1, -1, 0]
k = 0

print(count_subarrays_with_sum(nums, k))