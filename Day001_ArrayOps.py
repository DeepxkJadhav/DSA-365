"""
Day 1 : Reverse, Rotate, Remove Duplicates

Challenge:
Given an array, perform:
1. Reverse the array
2. Rotate it k steps to the right
3. Remove duplicates (keep order stable)
"""

# 1️ Reverse Array
def reverse_array(arr):
    return arr[::-1]

# 2️ Rotate Array Right by k steps
def rotate_array(arr, k):
    k %= len(arr)  # In case k > len(arr)
    return arr[-k:] + arr[:-k]

# 3️ Remove Duplicates (order preserved)
def remove_duplicates(arr):
    seen = set()
    return [x for x in arr if not (x in seen or seen.add(x))]

#  Testing All-in-One
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 2, 3]
    print("Original:       ", data)
    step1 = reverse_array(data)
    print("Reversed:       ", step1)
    step2 = rotate_array(step1, 2)
    print("Rotated by 2:   ", step2)
    step3 = remove_duplicates(step2)
    print("No Duplicates:  ", step3)
