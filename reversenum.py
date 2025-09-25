def reversenum(num):
    reversedd=0
    while(num>0):
            digit=num%10
            reversedd=reversedd*10+digit
            num//=10
    return reversedd 
num=(int(input('enter num:')))
print(reversenum(num))