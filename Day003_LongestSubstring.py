Day 3 – Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the **length** of the longest substring without repeating characters.

# Sliding Window Approach (O(n)) :

def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


# Test Cases ;
if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3 ("abc")
    print(length_of_longest_substring("bbbbb"))     # 1 ("b")
    print(length_of_longest_substring("pwwkew"))    # 3 ("wke")

#Key Python Tricks 🐍
- Using `set()` for O(1) duplicate checks.
- Moving `left` pointer dynamically without restarting from scratch.
- `max_len = max(max_len, right - left + 1)` to track window size on the fly.
    
Lesson Learned: Sliding window is the “Swiss Army knife” of string problems.
