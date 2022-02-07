#challenge 032

import math
radius=float(input("Enter the radius of a cylinder"))
depth=float(input("Enter the depth of the cylinder"))
area=math.pi*radius**2
volume=area*depth
print(round(volume,3))
