num = input("Enter a number: ")
sorted_digits = sorted(num, reverse=True)
max_number = ''.join(sorted_digits)
print(max_number)
