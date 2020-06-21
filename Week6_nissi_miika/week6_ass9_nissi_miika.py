def sqrt(n):
    if n < 0:
        return
    else:
        return n**0.5

def mean(array):
    return float(sum(array) / len(array))

def variance(array):
    m = mean(array)
    return mean([(x-m) ** 2 for x in array])

def standarddev(array):
    return sqrt(variance(array))

arr = [10, 40, 20, 22, 60, 8.98]

print(standarddev(arr))
