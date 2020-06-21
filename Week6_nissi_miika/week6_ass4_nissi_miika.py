def factorial(x):
    try:
        if x < 1: raise ValueError
        elif x == 1:
            return 1
        else:
            return x *factorial(x-1)
    except ValueError:
        print("Factorial can not be negative.")

print(factorial(-20))
print(factorial(20))
print(factorial(4))
