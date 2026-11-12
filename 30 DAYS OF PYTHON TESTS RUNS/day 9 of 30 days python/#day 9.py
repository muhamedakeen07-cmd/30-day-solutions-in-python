#day 9
#question 2


your_age = int(input("Enter your age: "))
my_age = int(input("Enter my age: "))

if your_age < my_age:
    age_difference = my_age - your_age
    if age_difference == 1:
        print(f"You are {age_difference} year older than me.")
    else:
        print(f"You are {age_difference} years older than me.")

elif your_age > my_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print(f"I am {age_difference} year older than you.")
    else:
        print(f"I am {age_difference} years older than you.")

else:
    print("We do have the same age.")
