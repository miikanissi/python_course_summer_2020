arr = [300,20,3,60,-500,-3,56]

i = 0
while i < len(arr):
    minim = min(arr[i:])
    index_minim = arr.index(minim)
    arr[i],arr[index_minim] = arr[index_minim],arr[i]
    i+=1

print(arr)
