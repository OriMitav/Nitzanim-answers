#Jurnalist born
paragraph = input("Enter your paragraph:")
counter = 0
pointer = 0
for each in paragraph:
    if each == ".":
        print(paragraph[pointer:counter])
        print()
        pointer == counter
    counter+= 1
