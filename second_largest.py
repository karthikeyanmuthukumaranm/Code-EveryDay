n=int(input('length of arr:'))
arr_elements=input('enter elements by space').split()
arr_elements=[int(i) for i in arr_elements]

unique_elements=list(set(arr_elements))

if len(unique_elements)<2:
    print('No second largest elements found')
else:
    unique_elements.sort(reverse=True)
    second_largest=unique_elements[1]
    print(second_largest)