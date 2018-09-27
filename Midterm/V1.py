month = input(("Month: "))
day = input(("Day: "))
month = month.lower()
month = month.capitalize()
day = int(day)
if month == "January" and day == 1:
    print("New year's day")
elif month == "June" and day == 17:
    print("National holiday")
elif month == "December" and day == 25:
    print("Christmas day")
else:
    print("Not a holiday")

