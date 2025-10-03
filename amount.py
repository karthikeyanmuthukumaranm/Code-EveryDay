amount=int(input('enter amount:'))
if amount%100 !=0:
    print('no')
else:
    note_500=amount//500
    amount%=500

    note_200=amount//200
    amount%=200

    note_100=amount//100
    amount%=100

print(note_500)
print(note_200)
print(note_100)