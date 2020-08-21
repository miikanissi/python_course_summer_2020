import random
randomArray1 = []
randomArray2 = []
for i in range(20):
    randomArray1.append(random.randint(1,100))
    randomArray2.append(random.randint(1,100))

print("Sum of two arrays: ", sum(randomArray1) + sum(randomArray2))
