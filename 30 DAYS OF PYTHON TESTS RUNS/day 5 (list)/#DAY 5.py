#DAY 5 

#question 1 
list = []
#question 2 
tec_company = ["meta", "google", "microsoft", "apple", "ibm","oracle", "amazon"]

#question 3 
companies = len(tec_company)

#question 4 
#high_tech_com = tec_company[0], tec_company[3], tec_company[6]

#print(high_tech_com)

#question 5 
mixed_data_types = ["Akeen", 17, 5.8, "Sri Lanka", True]

#question 6 
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#question 7 
#print(it_companies)
#question 8 

#print(len(it_companies))
#question 9

#print(it_companies[0], it_companies[3], it_companies[6])

#question 10 
it_companies[0] = "Meta"
#print(it_companies)

#question 11 
it_companies.append("Tesla")
#print(it_companies)

#question 12 
it_companies.insert(5,"netflix")
#print(it_companies)


#question 13 

#print(it_companies[4].upper())

#question 14 
#print(" # ".join(it_companies))


#question 15 

does_exist = "Amazon" in it_companies
#print(does_exist)

#question 16 


it_companies.sort()
#print(it_companies)


#question 17 

it_companies.reverse()
#print(it_companies)


#question 18 
first_three = it_companies[0:3]
#print(first_three)


#question 19 
last_three = it_companies[-3:]
#print(last_three)


#question 20 

avg_company = it_companies[5]
#print(avg_company)


#question 21 

it_companies.remove(it_companies[0])
#print(it_companies)


#question 22 


it_companies.remove(it_companies[4])
it_companies.remove(it_companies[3])
#print(it_companies)



#QUESTIO 23 
it_companies.remove(it_companies[-1])
#print(it_companies)


#questio 24 

it_companies.clear()
#print(it_companies)

#question 25
del it_companies


#question 26 
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

web_dev = front_end + back_end


#question 27

full_stack = web_dev.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")

print(full_stack)