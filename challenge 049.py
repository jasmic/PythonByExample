#challenge 049

compnum=50
count=1

guess = int(input("Try to guess what the number is! "))
while guess != compnum:
    count=count+1
    if guess<compnum:
        print("Too low... ")
    else:
        print("Too high... ")
    guess=int(input("Have another go... "))
print("Correct! That took you",count,"goes.")
