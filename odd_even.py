def odd_even(num):
    if num%2==0:
        return f'{num} is Even Number'
    else:
        return f'{num} is Odd Number'


num=int(input('enter number : '))
print(odd_even(num))