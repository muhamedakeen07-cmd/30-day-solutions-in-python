#QUESTION 21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?


hours = int(input("Enter the hours taken: "))
rate_per_hour = float(input("Enter the rate per Hour? "))

weekly_earn = hours * rate_per_hour

print(f"Your weekly earning is",weekly_earn)