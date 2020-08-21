print("sum of even values between 2-40 using for loop")
count = 0
for i in range(2,41,1):
    if(i % 2 == 0):
        count += i
print(count)

print("sum of even values between 2-40 using while loop")
counter = 0
x = 2
while x < 41:
    if(x % 2 == 0):
        counter += x
    x += 1
print(counter)
