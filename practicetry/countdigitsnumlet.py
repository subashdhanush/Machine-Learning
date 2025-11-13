import re
name="Python is 1"

digitcount=re.sub("[^0-9]","",name)
lettercount=re.sub("[^a-zA-z]","",name)
spacecount=re.sub("[ \s]","",name)

print(len(digitcount))
print(len(lettercount))
print(len(spacecount))