arr=[1,2,4,5,6]
tar=6
for i  in range(len(arr)):
    for j in range(i,len(arr)):
        if arr[i]+arr[j]==tar:
            print(arr[i],arr[j])