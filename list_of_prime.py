num=[1,2,4,5,55,65]
for n in num:
    if n>1:
        for i in range(2,n):
            if n % i ==0:
                print(f'{n} not prime')
                break
        else:
            print(f'{n} is prime')
    else:
        print(f'{n} is not prime')