#QUESTION 3 LEVEL 2 


fruits = ['banana', 'orange', 'mango', 'lemon']

bucket = input("Pick a fruit: ")

if bucket in fruits:
    print("That fruit already exists in the list")

else:
    fruits.append(bucket)
    print(fruits)