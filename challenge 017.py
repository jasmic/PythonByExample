#challenge 017

age = int(input("How old are you?\n"))


if age >= 18:
    print("You are old enough to vote.")
elif age == 17:
    print("You are old enough to learn how to drive.")
elif age == 16:
    print("You can buy a lottery ticket.")
else:
    print("You can go trick or treating!")
