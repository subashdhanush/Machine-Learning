def reverse_word(sentence):
    result = []
    for word in sentence.split():
       result.append(word[::-1])
    return ' '.join(result)
   

print(reverse_word("hello world"))