'''
### הכנה 0 - התנסות ##
print('Hello world')

### הכנה 1 - אתגר המעלית##
elevator1 = int(input("Enter the location of elevator 1: "))
elevator2 = int(input("Enter the location of elevator 2: "))
alice = int(input("Enter the location of Alice"))
if abs(elevator1 - alice) <= abs(elevator2 - alice):
    print("A")
else:
    print("B")
'''

### תנאים אי שוויון המשולש##


'''
#Multiplication table
num = int(input("Enter number:"))
if num > 0:
    for i in range(1,num+1):
        for j in range(1, num+1):
            print(f"{i}x{j}={i*j}")
else:
    print("Error")
'''

### Wordle ###
word = input("Enter secrete word: ").lower() #I want to have it as lower case
user_guess = input(f"guess word with {len(word)} letters: ")

#Game testing
for i in range(1,4):
    print(f"Round number {i}:")
    # lists
    grey_list = []
    green_list = []
    orange_list = []
    j = 0
    while j < len(word):
        if user_guess[j] == word[j]:
            green_list.append(user_guess[j])
        elif user_guess[j] in word:
            orange_list.append(user_guess[j])
        else:
            grey_list.append(user_guess[j])
        j += 1
    #Results
    print(f"The green list: {green_list}")
    print(f"The orange list: {orange_list}")
    print(f"The grey list: {grey_list}")
    if user_guess == word:
        print("You won!")
        break
    user_guess = input(f"guess word with {len(word)} letters: ")

 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#עיתונאי נולד
    '''
    # לקלוט מהמשתמש פסקה ולהחליט אם הפסקה טובה בהתאם להתניות
    # הפסקה צריכה להיות בין 3 ל5 משפטים.
    # המשפטים להיות טובים בהתאם להתניות
    # אם אין פסיקים המשפט יהיה בין 5 ל15 מילים
    # אם יש פסיקים המשפט יהיה עד 30 מילים

    # קלוט פסקה
    # בדוק כמה משפטים יש בפסקה#
    # ספור את כמות הנקודות בפסקה
    # בדוק כמה מילים יש בכל משפט#
    # בדוק כמה רווחים יש ותגדיל ב1
    '''

    paragraph = input("Enter your paragraph: ")
    index = 0  # Counting the number of sentences
    pointer = 0  # pointing the start of sentence
    counter = 0  # pointing the end of sentence
    tests_list = []
    for each in paragraph:
        if each == ".":
            the_sentence = paragraph[pointer:counter + 1]
            words = 1
            for value in the_sentence:
                if value == " ":
                    words += 1
            if words < 5:
                tests_list.append(f"The senetce in the index {index} is too short")
            elif "," in the_sentence:
                if words > 30:
                    tests_list.append(f"The senetce in the index {index} is too long")
            elif words > 15:
                tests_list.append(f"The senetce in the index {index} is too long")
            pointer = counter + 1
            index += 1
        counter += 1
    if index < 3:
        print("The size of the paragraph is too short")
    elif index <= 5:
        print("The size of the paragraph is ok")
    else:
        print("The size of the paragraph is too long")

    for each in tests_list:
        print(each)


