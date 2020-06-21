print("US Dollars to Euros converter")
print("Current XE conversion rate for 1 USD is 0.924214 Euros.")

while True:
    dollars = input("Enter the amount of dollars: ")
    try:
        x = float(dollars)
        if x < 0: raise ValueError("Dollars must be a positive number.")
    except ValueError:
        print("Try entering again...")
    else:
        break

rate = 0.924214
euros = x * rate
print(str(dollars) + " Dollars equals " + str('%.03f'%(euros)) + " Euros.")       
