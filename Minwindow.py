from collections import Counter

def minWindow(source, target):
    need = Counter(target)
    window = {}

    left = 0
    have = 0
    need_count = len(need)

    best = ""
    best_len = float("inf")

    for right in range(len(source)):
        char = source[right]

        window[char] = window.get(char, 0) + 1

        if char in need and window[char] == need[char]:
            have += 1

        while have == need_count:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best = source[left:right + 1]

            left_char = source[left]
            window[left_char] -= 1

            if left_char in need and window[left_char] < need[left_char]:
                have -= 1

            left += 1

    return best


print(minWindow("ADOBECODEBANC", "ABC"))