x = input("Enter voltage: ")
while (x.isdigit() == False):
    x = input("Enter voltage: ")

y = input("Enter current: ")
while (y.isdigit() == False):
    y = input("Enter current: ")

z = float(x) / float(y)

print("The resistance is " + str(z) + " Ohm's.")
