while True:
    value = input("Enter a number: ")
    try:
        x = float(value)
    except ValueError:
        print("Try entering again...")
    else:
        break

if x > 100:
    print(str(x) + " is over 100.")
else:
    print(str(x) + " is less than 100.")
