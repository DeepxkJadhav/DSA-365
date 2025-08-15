
Day 2 – Two Sum (3 Ways)



# Approach 1: Hash Map (O(n))

def two_sum_hash(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_map:
            return [num_map[diff], i]
        num_map[num] = i
    return []


# Approach 2: Two-Pointer (O(n log n))

def two_sum_two_pointer(nums, target):
    arr = sorted((num, i) for i, num in enumerate(nums))
    l, r = 0, len(arr) - 1
    while l < r:
        curr_sum = arr[l][0] + arr[r][0]
        if curr_sum == target:
            return [arr[l][1], arr[r][1]]
        elif curr_sum < target:
            l += 1
        else:
            r -= 1
    return []


# Approach 3: Binary Search (O(n log n))

import bisect

def two_sum_binary_search(nums, target):
    arr = sorted((num, i) for i, num in enumerate(nums))
    for idx, (num, original_idx) in enumerate(arr):
        complement = target - num
        pos = bisect.bisect_left(arr, (complement, -1), idx + 1)
        if pos < len(arr) and arr[pos][0] == complement:
            return [original_idx, arr[pos][1]]
    return []


# Test the functions

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print("Hash Map:", two_sum_hash(nums, target))
    print("Two Pointer:", two_sum_two_pointer(nums, target))
    print("Binary Search:", two_sum_binary_search(nums, target))
