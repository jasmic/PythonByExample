#challenge 026

word=input("please enter a word: ")
word=word.lower()

first = word[0]
length=len(word)
rest=word[1:length]
if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
    pigWord = rest + first + "ay"
else:
    pigWord = word + "way"
print(pigWord)
