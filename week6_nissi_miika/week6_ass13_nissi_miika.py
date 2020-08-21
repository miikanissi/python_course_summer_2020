import math as m

def cos(x, terms):
    return sum(((-1)**i) * (x ** (2*i)) / (m.factorial(2*i)) for i in range(terms))

def sin(x, terms):
    sini = 0
    for i in range(terms):
        sign = (-1)**i
        sini = sini + ((x**2.0*i+1))/m.factorial(2*i+1)*sign
    return sini

print(cos(1.2, 30))
print(sin(1.6, 20))
