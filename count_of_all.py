import re
stringg="python is 1"

digitcount=re.sub("[^0-9]","",stringg)
lettercount=re.sub("[^a-zA-Z]","",stringg)

print(len(digitcount))
print(stringg.count(" "))
print(len(lettercount))