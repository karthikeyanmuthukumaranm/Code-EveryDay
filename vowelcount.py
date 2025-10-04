sentence=input()
vowel='AEIOUaeiou'
vowel_count=0
const_count=0
for i in sentence:
    if i.isalpha():
        if i in vowel:
            print(f'{i}-vowel')
            vowel_count+=1
        else:
            print(f'{i}-const')
            const_count+=1
print(vowel_count)
print(const_count)

