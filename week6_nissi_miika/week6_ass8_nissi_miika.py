def product(iterable):
    prod = 1
    for n in iterable:
        prod *= n
    return prod

def factorial(x):
    try:
        if x < 1: raise ValueError
        elif x == 1:
            return 1
        else:
            return x *factorial(x-1)
    except ValueError:
        print("Factorial can not be negative.")

def npr(n, r):
    assert 0 <= r <= n
    return product(range(n - r + 1, n + 1))

def ncr(n, r):
    assert 0 <= r <= n
    if r > n // 2:
        r = n - r
    return npr(n, r) // factorial(r)

print(ncr(4,2))
print(ncr(10,5))
