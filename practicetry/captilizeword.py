def captilizeword(s):
    result=[]
    for char in s.split():
        result.append(char.capitalize())
    return ' '.join(result) 

print(captilizeword("hello world python"))