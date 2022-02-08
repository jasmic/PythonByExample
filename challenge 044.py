#challenge 044

guests=int(input("how many guests do you want to invite to the party? "))

if guests < 10:
    for i in range(0,guests):
        name=input("Enter the name of your guest")
        print(name,"has been invited.")

else:
    print("Sorry, too many guests.")
