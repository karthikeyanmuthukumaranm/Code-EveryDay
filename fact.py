def fact(n):
    for i in range(n):
        if i==0:
            return 0
        elif i==1:
            return 1
        else:
            return fact(n(n-1))

a=int(input("enter number:"))
fact(3)
