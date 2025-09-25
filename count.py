# text=input("enter text :")
# word=input("enter which word count need:")
# counts=text.count(word)
# print(f"{word} is {counts}")

# textt=input('enter word:')
# splitt=len(textt.split())
# print(splitt)

tetx=input('enter letters to count:')
lettercount=0
for i in tetx:
    if i.isalpha():
        lettercount+=1
print(lettercount)