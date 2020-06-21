import numpy as np

# I was very confused at first how to solve this problem
# After googling for ideas I found this numpy library
# https://numpy.org/doc/stable/reference/generated/numpy.roots.html
# which solves quadratic equations using the coefficients

coeff = [3, -4, 9, 5]
print(np.roots(coeff))
