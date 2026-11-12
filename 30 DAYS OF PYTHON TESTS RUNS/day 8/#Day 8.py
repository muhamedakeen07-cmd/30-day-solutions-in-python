#Day 8 

#questio 1 and 2 

dog = {"name": "Scooby","color": "brown", "breed": "Labrador", "legs": 4 , "age": 3}

#question 3 

Student = {
    'first_name':'Akeen',
    'last_name':'Arshad',
    'age':17,
    "geder": "male",
    'country':'Sri lanka',
    'martial_status':"not_married",
    'skills':['Cotent creating', 'html', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'}}

#question 4 
#print(len(Student))


#QUESTION 5 

print(type(Student["skills"]))


#question 6 


(Student["skills"].append("marketing"))


#questio 7 

student_keys = Student.keys()
#print(student_keys)


#question 8 

student_values = Student.values()
print(student_values)


#question 9 
print(Student.items())



#question 10 
Student.pop("skills")


#question 11

del Student
print(Student)