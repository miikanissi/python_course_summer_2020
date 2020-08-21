x = input("Enter a week number (1 -7): ")

def f(x):
    return {
        "1":"Monday",
        "2":"Tuesday",
        "3":"Wednesday",
        "4":"Thursday",
        "5":"Friday",
        "6":"Saturday",
        "7":"Sunday"
        }.get(x, "Not a week number")

print(f(x))
