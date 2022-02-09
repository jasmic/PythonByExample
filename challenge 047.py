#challenge 047


num=int(input("Please enter a number: "))
total=num
again="y"
while again == "y":
    addNum=int(input("Please enter another number: "))
    total=total+addNum
    print("The current total is",total)
    again=input("Do you want to add another number? (y/n)")
    
    
print("The total is",total)
