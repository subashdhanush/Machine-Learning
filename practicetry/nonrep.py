def first_non_repeating_char(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return None

print(first_non_repeating_char("aabbccdeff"))  # d



def all_non_repeating_chars(s):
    return [ch for ch in s if s.count(ch) == 1]

print(all_non_repeating_chars("aabbccdeff"))  # ['d', 'e']
