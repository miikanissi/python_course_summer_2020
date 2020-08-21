def myMax(l):
    number = l[0]

    # Goes through the list and compares it to the previous largest number,
    # If the number is higher than previous largest number,
    # It becomes the new largest number.
    for x in l:
        if x > number:
            number = x

    return number


print("Find the biggest number")

l = list()
for x in range(0, 3):
    while True:
        number = input("Enter a number: ")
        try:
            a = float(number)
        except ValueError:
            print("Try entering again...")
        else:
            l.append(a)
            break
l.sort()
print("Using sort: Largest number is :", l[-1])
print("Using max: Largest number is :", max(l))
print("Using comparison: Largest number is :", myMax(l))
