#challenge 043

num=0
direction=int(input("""1: count up
2: count down"""))

if direction==1:
    top=int(input("What number do you want to count up to? "))
    for i in range(0,top):
        num=num+1
        print(num)
elif direction==2:
    top=int(input("Please enter a number below 20: "))
    if top < 20:
        for i in range(top,0,-1):
            print(i)
    else:
        print("Invalid selection")
else:
    print("Invalid selection")
