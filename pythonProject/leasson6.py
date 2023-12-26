#Jurnalist born
paragraph = input("Enter your paragraph:")
sentences = 0
counter = 0
pointer = 0
index = 0
tests_list = []
for each in paragraph:
    if each == ".":
        the_sentence = paragraph[pointer:counter]
        words = 1
        for value in the_sentence:
            if value ==" ":
                words += 1
        if words < 5:
            tests_list.append(f"The sentence in index {index} is too short")
        elif "," in the_sentence:
            if words > 30:
                tests_list.append(f"The sentence in index {index} is too long")
            print(f"The number of words is: {words}")
        elif words > 15:
            tests_list.append(f"The sentence in index {index} is too long")
        #print(f"the length of the sentence is: {len(paragraph[pointer:counter])}")
        pointer = counter
        index += 1
    counter+= 1
if index < 3:
    print("The size of paragraph is too short")
elif index <= 5:
    print("The size of paragraph is ok")
else:
    print("The size of paragraph is too long")
for each in tests_list:
    print(each)


