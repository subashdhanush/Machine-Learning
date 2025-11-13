# N=(input("enter a number"))
# for i in N:
#     if N.count(i) > 1:
#         print("Yes")
#     else:
#         print("NO")    
n = input("Enter a number: ")
has_repeat = False

for digit in n:
    if n.count(digit) > 1:
        has_repeat = True
        break

if has_repeat:
    print("yes")
else:
    print("no")
