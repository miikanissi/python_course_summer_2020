import random
randomArray = []

for i in range(30):
    randomArray.append(random.randint(1,100))

def Average(lst):
    return sum(lst)/len(lst)
print("Sum of 30 random numbers between 1-100: ", sum(randomArray))
print("Average of 30 random numbers between 1-100: ", round(Average(randomArray), 2))
print("Largest number in array: ", max(randomArray))

while True:
    finder = input("Enter a number (1-100), to find it in array, 0 to exit: ")
    try:
        x = int(finder)
        if x < 0 or x > 100: raise ValueError("Number not between 1-100")
        if x == 0: break
        try:
            print(x, " was found in array at index: ", randomArray.index(x))
        except ValueError:
            print(x, " was not found in array.")
    except ValueError:
        print("Try entering again")
