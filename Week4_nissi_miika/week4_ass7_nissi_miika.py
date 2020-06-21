print("Build a semipyramid!")
while True:
    height = input("Enter the height of the semipyramid (amount of rows): ")
    try:
        x = int(height)
        if x < 0: raise ValueError("Number can not be negative")
    except ValueError:
        print("Try entering again...")
    else:
        for i in range(x):
            print("m" * (i+1))
        break
