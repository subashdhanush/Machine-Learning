S=input("enter a name")
list1=[]
list2=[]
count=0
countnew=0
result=0
for j in S:
    list1.append(j)
    a=list1.count(j)
    print(a)
    if a>1:
        countnew=a+countnew
        result=len(S)-countnew  
    elif a == 0:
        result=-1    
    # print(a,j)
    # print(countnew,"COUNTNEW")  
print(result,"result")          

 
