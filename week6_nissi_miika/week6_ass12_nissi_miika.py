def factorial(x):
    try:
        if x < 0: raise ValueError
        elif x == 1 or x == 0:
            return 1
        else:
            return x *factorial(x-1)
    except ValueError:
        print("Factorial can not be negative.")

def e(n):
    return sum(1 / float(factorial(i)) for i in range(n))

print(e(10))
