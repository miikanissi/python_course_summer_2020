mathArr = [10, 8, 6, 7, 8, 7, 9, 9, 7, 8]
engArr = [10, 6, 7, 8, 9, 6, 7, 8, 9, 10]

def mean(arr):
    n = len(arr)
    return sum(arr)/n

def squaredev(arr):
    y = mean(arr)
    sd = sum((x-y)**2 for x in arr)
    return sd

def standdev(arr):
    n = len(arr)
    sd = squaredev(arr)
    pvar = sd/n
    return pvar**0.5

def cov(x,y):
    n = len(x)
    xy = [x[i]*y[i] for i in range(n)]

    return (sum(xy) - n * mean(x) * mean(y)) / float(n)
# Correlation formula Pxy=Cov(rx,ry)/(sdx*sdy)

print("Covariance: ", cov(mathArr, engArr))
print("Correlation: ", cov(mathArr, engArr)/(standdev(mathArr)*standdev(engArr)))
