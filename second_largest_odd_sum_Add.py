arr=list(map(int,input('enter element sepated by space:').split()))
if len(arr)==0 or len(arr)<=3:
    print(0)
else:
    odd_arr=[]
    even_arr=[]

for i in arr:
    if i%2==0:
        even_arr.append(i)
    else:
        odd_arr.append(i)
even_arr.sort()
odd_arr.sort()

second_largest_even=even_arr[-2]
second_smallest_odd=odd_arr[1]
result=second_largest_even+second_smallest_odd
print(result)