#challenge 020 error

##num = input("Enter a number: ")   #this creates an error message
##total = num + 10                  #type error - cannot convert int object to str
##print(total)

#either...

#num = int(input("Enter a number: ")
#OR...
#num = input("Enter a number: ")
#num = int(num)

num = input("Enter a number: ")
num = int(num)
total = num + 10
print(total)

