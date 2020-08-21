print("sum of 5, 10, 15, .. 100 using for loop")
count = 0
for i in range(5,101):
    if(i % 5 == 0):
        count += i
print(count)

print("sum of 5, 10, 15, .. 100 using while")
counter = 0
x = 5
while x < 101:
    if(x % 5 == 0):
        counter += x
    x += 1
print(counter)
