#day 6 questions 

#question 1 

emp_tuple = ()

#question 2 
brothers = ("John", "Mike", "David")
sisters = ("Anna", "Emily", "Sophia")


#quetion 3 

siblings = brothers + sisters
#question 4 

#print(len(siblings))

#question 5 

family_members = (siblings) + ("Mom", "Dad")
#print(family_members)


#exercise level 2
#question 1 level 2 


# Unpacking siblings and parents

siblings = family_members[0:6]

father, mother = family_members[6:8]

#print(siblings)
#print(father)
#print(mother)


#question 2 lvel 2 

fruits = ("apple", "banana", "cherry", "date", "elderberry")
vegetables = ("asparagus", "broccoli", "carrot", "daikon", "eggplant")
animals_product = ("chicken","meat", "fish", "goat", "beef")

food_stuff_tpl = fruits + vegetables + animals_product

#question 3 level 2 

food_stuff_list = list(food_stuff_tpl)

#question 4 level 2 

middle_items = food_stuff_list[7:8]


#questio 5 
first_three = food_stuff_list[0:3]
last_three = food_stuff_list[-3:]

print("First three items:", first_three)
print("Last three items:", last_three)

#question 6 level 2 

del food_stuff_tpl


#question 7 level 2 

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in nordic_countries)  
print("Iceland" in nordic_countries)  
