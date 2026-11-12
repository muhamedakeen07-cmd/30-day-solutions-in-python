#Day 7 (sets) LEVEL 3 


#question1 
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

age_in_set = set(age)
print(len(age_in_set))
print(len(age))



#question 3 

sentece = "I am a teacher and I love to inspire and teach people."
words = sentece.split()
unique_words = set(words)
print(unique_words)