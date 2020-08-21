def biggest(x,y,z):
    if (x > y) and (x > z):
        big = x
    elif (y > x) and (y > z):
        big = y
    else:
        big = z
    return big

print(biggest(20,4,10))
print(biggest(2,20,2))
print(biggest(9,8,30))
print(biggest(8,9,8))
    
