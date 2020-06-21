x = input("Enter a month number (1-12): ")

def f(x):
    return {
        "1":"January has 31 days.",
        "2":"February has 28 days or 29 during leap years.",
        "3":"March has 31 days.",
        "4":"April has 30 days.",
        "5":"May has 31 days.",
        "6":"June has 30 days.",
        "7":"July has 31 days.",
        "8":"August has 31 days.",
        "9":"Sebtember has 30 days.",
        "10":"October has 31 days.",
        "11":"November has 30 days.",
        "12":"December has 31 days."
        }.get(x, "Not a month number")

print(f(x))
