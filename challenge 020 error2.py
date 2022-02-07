#challenge 020 error 2

#This code generates an error message
#Can only concatentate str to str, not int
##name = input("Enter a name: ")
##num = int(input("Enter a number: "))
##ID = name + num
##print(ID)

#fix 1 - don't define the number as an int
name = input("Enter a name: ")
num = input("Enter a number: ")
ID = name + num
print(ID)

#fix 2 - convert the int to a str
name = input("Enter a name: ")
num = int(input("Enter a number: "))
num = str(num)
ID = name + num
print(ID)

