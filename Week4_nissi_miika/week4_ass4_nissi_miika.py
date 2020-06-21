from random import randint

counter = [0] * 7

for i in range(0,100):
    value = randint(1,6)
    counter[value] += 1

for i in range(1,7):
    print( str(i) + " was hit " + str(counter[i]) + " times.")

