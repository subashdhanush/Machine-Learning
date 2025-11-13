num=4123
result1=[]
result=list(str(num))
print(len(result))
for i in range(len(result) - 1):
    print(result[i],result[i+1])
    if result[i] < result[i+1]: 
        print("inside",i)
        result1.append(i)
print(result1)        