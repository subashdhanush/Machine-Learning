num = 12345
rev = 0
for digit in str(num):
    rev = int(str(rev) + digit)
print("Reversed:", str(rev)[::-1])