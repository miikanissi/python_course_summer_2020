arr = [1, 40, 50, 20, 30, 40, 55, 98, 234, -290, -33]
print("Original array: ", arr)

# Append to array
arr.append(46)
print("Array appended with 46: ", arr)

# Extend an array with another array
iters = [200, 32, -1]
iterator = iter(iters)
arr.extend(iterator)
print("Array after extending with another array: ", arr)

# Insert an item in array at given position
arr.insert(2, 90)
print("Array after inserting 90 at position 2: ", arr)

# Remove an item from array
arr.remove(40)
print("Array after removing the first 40: ", arr)

# Remove an item from array at given position
arr.pop(10)
print("Array after removing item at position 10: ", arr)

# Return index of value in array
print("Return index of value 40: ", arr.index(40))

# Counts how many times item is in array
print("Return how many times value 40 appears in array: ", arr.count(40))

# Sorts array in ascending order
arr.sort()
print("Array sorted: ", arr)

# Reverses order of array
arr.reverse()
print("Array reversed: ", arr)

# Copies array
copy = arr.copy()
print("Copy of array: ", copy)

# Clears the original array
arr.clear()
print("Array emptied: ", arr)
