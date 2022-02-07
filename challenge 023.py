#challenge 023

nursery=input("Please enter a line of text from a nursery rhyme: ")
lenNurse=len(nursery)
print("This phrase has ",lenNurse,"letters and spaces in it.")
num1=int(input("Give me a starting point number: "))
num2=int(input("Give me an end point number: "))
print(nursery[num1:num2])

