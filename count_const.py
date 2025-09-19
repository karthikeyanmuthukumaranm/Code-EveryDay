sentence='program'
vowel='aeiouAEIOU'
count=0
for i in sentence:
    if i not in vowel:
        count+=1
print(f'constant count: {count}')