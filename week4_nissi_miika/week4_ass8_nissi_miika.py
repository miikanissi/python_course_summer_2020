print("N factorial calculator")
while True:
    n = input("Enter variable n: ")
    try:
        x = int(n)
        if x < 0: raise ValueError("Enter positive number")
    except ValueError:
        print("Try entering again.")
    else:
        factorial = 1
        for i in range(2, x + 1):
            factorial *= i
        print(factorial)
        break
