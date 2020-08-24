# Python testing example
#
# Week 11-12, Python testing, Miika Nissi

def fibonacci(n):
    x = 0
    y = 1
    if n < 0:
        print("N can't be less than 0")
    elif n == 0:
        return x
    elif n == 1:
        return y
    else:
        for i in range(2,n):
            z = x + y
            x = y
            y = z
        return y

print(fibonacci(5))
