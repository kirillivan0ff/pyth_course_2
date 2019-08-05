import random

n1 = random.randrange(1,10)
n2 = random.randrange(1,10)
answer = input(f'{n1}x{n2}?:')

test = answer.replace('.', '', 1)

if answer.isdigit():
    if int(answer) == n1*n2:
        print('Correct!')
    else:
        print('Wrong!')
else:
    print('Enter number!')