arr=[30,4,2,3]
for n in arr:
    if n>2:
        for i in range(2,n):
            if n%i==0:
                print(f'{n}not prime')
                break
            else:
                print('prime')

    elif n==2:
        print('primr')


    else:
        print('not')
