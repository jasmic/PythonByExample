#challenge 039

num=int(input("Please enter a number between 1 and 12: "))
table=0

for x in range(1,13):
    table=table+1
    answer=num*table
    print(table,"*",num,"=",answer)  
