#challenge 050 - I could not get this one to work!
#Seeing the answer makes sense though

num1=int(input("Enter a number between 10 and 20: "))

while num1<10 or num1>20:
    if num1<10:
         print("Too low! Please Try again")
    else:
        print("Too high! Please Try again")
    num1=int(input("Have another go: "))
print("Thank you")
