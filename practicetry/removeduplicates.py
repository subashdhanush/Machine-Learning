def removeduplicate(sentence):
    result=""
    for char in sentence:
        if char not in result:
            result=result+char
    return result

print(removeduplicate("Programming"))            