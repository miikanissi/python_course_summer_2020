import random

arr = []

for i in range(20):
    arr.append(random.randint(1,50))

def mean(arr):
    n = len(arr)
    return sum(arr)/n

def squaredev(arr):
    y = mean(arr)
    sd = sum((x-y)**2 for x in arr)
    return sd

def standdev(arr):
    n = len(arr)
    sd = squaredev(arr)
    pvar = sd/n
    return pvar**0.5

print("Program calculates the population standard deviation of 20 random numbers between 1-50")
print(standdev(arr))
