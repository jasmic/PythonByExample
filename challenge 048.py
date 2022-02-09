#challenge 048

#My version - it works, but is more complicated than the answer given in the book
##count=0
##invite=input("Enter the name of someone you want to invite to the party.")
##print(invite,"has been invited.")
##invite=input("Do you want to invite someone else to the party? (y/n)")
##newInvite=invite
##while newInvite == "y":
##    invite=input("Enter the name of the person you want to invite to the party.")
##    print(invite,"has been invited.")
##    count=count+1
##    newInvite=input("Do you want to invite someone else to the party? (y/n)")
##print(count,"people have been invited to the party.")

#solution from the book
count=0
again="y"
while again == "y":
    name=input("Enter the name of someone you want to invite to the party.")
    print(name,"has been invited.")
    count=count+1
    again=input("Do you want to invite someone else to the party? (y/n)")
print(count,"people have been invited to the party.")
