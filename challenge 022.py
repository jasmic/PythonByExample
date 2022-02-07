#challenge 022

firstName=input("Please enter your first name in lower case: ")
firstName=str.lower(firstName) #added this line to force the entry to be lower case
surname=input("Please enter your surname in lower case: ")
surname=str.lower(surname)

fullName = firstName + " " + surname
fullName=str.title(fullName)
print(fullName)
