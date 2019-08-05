import random
i1 = 0
i2 = 0
c = 0
n1 = 1
n2 = 4

realValue = random.randrange(n1, n2)
while c < 100:
    check = random.randrange(n1, n2-1)
    if check == realValue:
        i1 += 1
    elif check == random.randrange(n1, n2):
        i2 += 1
    c += 1        

n3 = i1 - i2

print(f"Chance is higher on {n3}%")