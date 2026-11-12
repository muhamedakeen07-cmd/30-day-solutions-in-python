    #question 20 
    # Use index to determine the position of the first occurrence of C in Coding For All.



tagline = "Coding For All"

    #print(tagline.index("C"))


    #question 21 Use index to determine the position of the first occurrence of F in Coding For All. 


    #print(tagline.index("F"))


    #question 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.

tagline = "Coding For All People"

    #print(tagline.rfind("l"))


    #QUESTION 23 Use index or find to find the position of the first occurrence of the word 'because'
    #  in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence = "You cannot end a sentence with because because because is a conjunction"

    #print(sentence.index("because"))


    #question 24 Use rindex to find the position of the last occurrence of the word because 
    # in the following sentence: 'You cannot end a sentence with because because because is a conjunction' 

    #print(sentence.rindex("because"))

    #question 25 Slice out the phrase 'because because because' in the
    #  following sentence: 'You cannot end a sentence with because because because is a conjunction'

    #start = sentence.find("because")

    #print(sentence[start:start+23])


    #QUESTION 26 Find the position of the first occurrence of the word 'because' in the 
    # following sentence: 'You cannot end a sentence with because because because is a conjunction'

#first_position = sentence.index("because")
#print(first_position)

#question 27 Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'


#slice_start = sentence.find("because")
#slice_end = slice_start + len("because because because")

#print(sentence[slice_start:slice_end])


#question 28 Does 'Coding For All' start with a substring Coding?


tagline = "Coding For All"

#print(tagline.startswith("Coding"))


#question 29 Does 'Coding For All' end with a substring coding?

#print(tagline.endswith("coding"))


#question 30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.

tagline = "   Coding For All      "

#print(tagline.strip())

#question Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python

#print("thirty_days_of_python".isidentifier())

