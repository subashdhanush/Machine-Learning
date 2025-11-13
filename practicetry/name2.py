s = input("Enter a string: ")
unique_count = 0

for char in s:
    if s.count(char) == 1:
        unique_count += 1

if unique_count == 0:
    print(-1)
else:
    print(unique_count)
