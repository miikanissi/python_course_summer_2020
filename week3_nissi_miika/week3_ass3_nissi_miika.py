print("BMI Calculator")
unit = input("Choose the unit of measure: 1 for Metric, 2 for Imperial: ")

while (unit != "1" and unit != "2"):
    unit = input("Choose the unit of measure: 1 for Metric, 2 for Imperial: ")

if (unit == "1"):
    while True:
        weight = input("Enter weight in kg: ")
        try:
            x = float(weight)
            if x < 0: raise ValueError("Weight must be positive.")
        except ValueError:
            print("Try entering again...")
        else:
            break

    while True:
        height = input("Enter height in m: ")
        try:
            y = float(height)
            if y < 0: raise ValueError("Height must be positive.")
        except ValueError:
            print("Try entering again...")
        else:
            break

    bmi = x / (pow(y, 2))
else:
    while True:
        weight = input("Enter weight in lbs: ")
        try:
            x = float(weight)
            if x < 0: raise ValueError("Weight must be positive.")
        except ValueError:
            print("Try entering again...")
        else:
            break
        
    while True:
        height = input("Enter height in inches: ")
        try:
            y = float(height)
            if y < 0: raise ValueError("Height must be positive.")
        except ValueError:
            print("Try entering again...")
        else:
            break

    bmi = 703 * x / (pow(y, 2))
    
if (bmi < 18.5):
    print("Your BMI is " + '%.01f'%(bmi))
    print("According to BMI you are Underweight.")
elif (bmi >= 18.5 and bmi < 24.5):
    print("Your BMI is " + '%.01f'%(bmi))
    print("According to BMI you are Normal weight.")
elif (bmi >= 24.5 and bmi < 30):
    print("Your BMI is " + '%.01f'%(bmi))
    print("According to BMI you are Overweight.")
else:
    print("Your BMI is " + '%.01f'%(bmi))
    print("According to BMI you are Obese.")
