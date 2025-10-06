import random
def diceroll():
    while True:
        try:
            dice=(int(input('Enter No of Dice : ')))
            sides=(int(input('Enter Number of Sides : ')))
        except ValueError:
            print('Invalid ! please enter a valid Number')
            continue
        rolls= [random.randint(1,sides) for _ in range(dice)]
        print('you rolled',rolls)
        print('Total',sum(rolls))

        again=input('Roll Again? (y/n):').lower()
        if again !='y': 
            break

if __name__=='__main__':
    diceroll()