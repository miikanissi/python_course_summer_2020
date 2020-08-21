print("Euros to bills converter")

while True:
    euros = input("Enter the amount of Euros: ")
    try:
        x = float(euros)
        if x < 0: raise ValueError("Euros must be positive.")
    except ValueError:
        print("Try entering again...")
    else:
        break


euros = x
bill500 = euros // 500
euros %= 500
bill200 = euros // 200
euros %= 200
bill100 = euros // 100
euros %= 100
bill50 = euros // 50
euros %= 50
bill20 = euros // 20
euros %= 20
bill10 = euros // 10
euros %= 10
bill5 = euros // 5
euros %= 5

billlist = []
if bill500 != 0:
    billlist.append(str(int(bill500)) + ", 500 euro bill(s). ")
if bill200 != 0:
    billlist.append(str(int(bill200)) + ", 200 euro bill(s). ")
if bill100 != 0:
    billlist.append(str(int(bill100)) + ", 100 euro bill(s). ")
if bill50 != 0:
    billlist.append(str(int(bill50)) + ", 50 euro bill(s). ")
if bill20 != 0:
    billlist.append(str(int(bill20)) + ", 20 euro bill(s). ")
if bill10 != 0:
    billlist.append(str(int(bill10)) + ", 10 euro bill(s). ")
if bill5 != 0:
    billlist.append(str(int(bill5)) + ", 5 euro bill(s). ")

print(str(int(x)) + " Euros gives you ")
for x in billlist:
    print(x)
