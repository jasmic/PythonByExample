#challenge 042

total=0

for i in range(0,5):
    num=int(input("Please enter a number: "))
    include=input("Do you want to include that number in your total? ")
    include=str.lower(include)
    if include=="yes" or include=="y":
        total=total+num
        print("OK, number included...")
    else:
        print("OK, number not included...")
print("The total is",total)


  
