print("Exponential calculator")
while True:
    base = input("Enter base number (real number): ")
    try:
        x = float(base)
    except ValueError:
        print("Try entering again...")
    else:
        while True:
            exp = input("Enter exponent (whole number): ")
            try:
                y = int(exp)
            except ValueError:
                print("Try entering again...")
            else:
                if y == 0:
                    result = 0
                else:
                    result = x
                    for i in range(1, y):
                        result *= x
                print(result)
                break
        break
    
