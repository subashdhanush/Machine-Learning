def count_vowels_consonants(s):
    vowels="aeiouAEIOU"
    v=0
    c=0
    # v=sum(1 for char in s if char in vowels)
    # c=sum(1 for char in s if char.isalpha() and char not in vowels)
    for char in s:
        if char in vowels:
            v=v+1
        elif char.isalpha() and char not in vowels:
            c=c+1   
    return v,c     

print(count_vowels_consonants("Hello world"))    