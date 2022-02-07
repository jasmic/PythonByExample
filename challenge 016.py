#challenge 016

raining = input("Is it raining?\n")
raining = str.lower(raining)

if raining == "yes":
    windy = input("Is it windy?\n")
    windy = str.lower(windy)
    if windy == "yes":
        print("It is too windy for an umbrella.")
    else:
        print("Take an umbrella.")
else:
    print("Have a nice day!")
