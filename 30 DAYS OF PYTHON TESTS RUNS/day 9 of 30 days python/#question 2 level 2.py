#question 2 level 2 

month = input("Enter the month: ").lower()


if month == "december" or month == "january" or  month== "february":
    print("Winter")
elif month == "march" or month == "april" or  month== "may":
    print("spring")
elif month == "june" or month == "july" or  month== "august":
    print("summer")
elif month == "september" or month == "october" or  month== "november":
    print("Autumn")
else:
    print("Enter a valid month")

