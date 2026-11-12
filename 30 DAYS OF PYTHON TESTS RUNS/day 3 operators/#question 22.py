#question 22
#  Write a script that prompts the user to enter number of years.
#  Calculate the number of seconds a person can live. Assume a person can live hundred years



lived = int(input("Enter the years you were alived: "))

a_year_in_sec = 60*60*24*365

lived_in_sec = lived*a_year_in_sec
print(lived_in_sec)

