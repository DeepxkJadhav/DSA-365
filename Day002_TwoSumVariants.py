
Day 2 – Two Sum (3 Ways)

## Problem Statement
Given an array of integers and a target value, return indices of the two numbers that sum up to the target.  
 The twist: Solve it using 3 different approaches.

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

📌 Lesson Learned:** Always squeeze more juice out of a simple problem — it’s free training.

## Key Python Tricks 
- Dictionary lookups for O(1) search.
- `sorted((value, index) for index, value in enumerate(nums))` for preserving original indices.
- `bisect.bisect_left` for binary search on sorted tuples.
