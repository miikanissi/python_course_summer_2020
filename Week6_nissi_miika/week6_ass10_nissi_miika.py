def search(array, n):
    for i in array:
        if i == n:
            return True
    return False

arr = [23,4,89,19,0,700,30]
print("Number 19 found: ", search(arr, 19))
print("Number 20 found: ", search(arr, 20))
