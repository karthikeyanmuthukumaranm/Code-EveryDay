import random
def guess_number():
    print('welcome to play guessing game')
    guess_num=random.randint(1,100)
    attempt=0
    while True:
        inputt=int(input('enter number : '))
        attempt+=1
        if guess_num>inputt:
            print('too low')
        elif guess_num<inputt:
            print('too high')
        else:
            print(f'congrats you guessed at {attempt}')
            break
guess_number()