print("Convert seconds to hours:minutes:seconds")

while True:
    seconds = input("Enter seconds: ")
    try:
        x = int(seconds)
        if x < 0: raise ValueError("Seconds must be positive.")
    except ValueError:
        print("Try entering again.")
    else:
        break

seconds = x % (24 * 3600)
print(seconds)
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print("%d:%02d:%02d" % (hours, minutes, seconds))
