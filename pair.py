numbers=[2,8,9,1,4,5]
target=9
pairs=[]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] == target :
            pairs.append((numbers[i],numbers[j]))
print(f'pairs of is {pairs}')
