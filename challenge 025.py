#challenge 025

name=input("please enter your first name: ")
nameLen=len(name)
if nameLen <5:
    surname=input("Please enter your surname: ")
    fullName=name+surname
    fullName=fullName.upper()
    print(fullName)
else:
    name=name.lower()
    print(name)
