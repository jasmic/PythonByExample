#challenge 034

import math
choice=int(input("""1) Square
2) Triangle

Enter a number: """))

if choice == 1:
    side=float(input("what is the length of one of the sides?"))
    area=side*side
    print(round(area,3))
elif choice == 2:
    base=float(input("What is the length of the base of the triangle?"))
    height=float(input("What is the height of the triangle?"))
    area=(base*height)/2
    print(round(area,3))
else:
    print("Invalid Choice.")
