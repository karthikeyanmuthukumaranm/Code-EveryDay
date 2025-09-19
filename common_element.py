def common_in_lists(list1,list2):
    common_elements=[]
    for i in list1:
        if i in list2:
            common_elements.append(i)
    return common_elements

list1=[1,2,4,5]
list2=[3,4,6,2]
print(common_in_lists(list1,list2))