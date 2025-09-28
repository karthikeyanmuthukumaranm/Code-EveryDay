def is_a(number):
    digits=str(number)
    power=len(digits)
    total=sum(int(i) ** power for i in digits)
    return total == number

number=153

if is_a(number):
    print(f'{number} is an Armstrong number')
else:
    print(f'{number} is not an Armstrong number')