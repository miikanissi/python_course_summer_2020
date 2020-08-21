x = input("Enter the speed of the car (km/h): ")
while (x.isdigit() == False):
    x = input("Enter the speed of the car (km/h): ")

y = input("Enter the distance (km): ")
while (y.isdigit() == False):
    y= input("Enter the distance (km): ")

hours = float(y)/float(x)
inthours = int(hours)
minutes = (hours*60) % 60
print("To travel " + y + " km at " + x + " km/h, takes " + str('%.3f'%(hours)) + " hours or " + str(inthours) + " hours and " + str('%02d'%(minutes)) + " minutes.")
