balance = 0

while True:
    print("Account Manager")
    print("1 - Deposit")
    print("2 - Withdraw")
    print("3 - Balance")
    print("0 - Exit")
    option = input()
    try:
        x = int(option)
        if x < 0 or x > 3: raise ValueError("Enter correct number.")
    except ValueError:
        print("Try entering again...")
    else:
        if x == 0:
            break
        elif x == 1:
            while True:
                deposit = input("How much would you like to deposit? ")
                try:
                    y = float(deposit)
                    if x < 0: raise ValueError("Amount can not be negative.")
                except ValueError:
                    print("Try entering amount again...")
                else:
                    balance += y
                    input("Press any key to continue...")
                    break
        elif x == 2:
            while True:
                withdraw = input("How much would you like to withdraw? ")
                try:
                    z = float(withdraw)
                    if z < 0 or z > balance: raise ValueError("Can not withdraw that amount")
                except ValueError:
                    print("Try entering amount again...")
                else:
                    balance -= z
                    input("Press any key to continue...")
                    break
        elif x == 3:
            print("Your balance is " + str(balance))
            input("Press any key to continue...")
