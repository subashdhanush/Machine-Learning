from collections import Counter

def first_non_repeating(s):
    count = Counter(s)
    print(count)
    for char in s:
        if count[char] == 1:
            return char
    return None

print(first_non_repeating("aabbcddeff"))  # 'c'
