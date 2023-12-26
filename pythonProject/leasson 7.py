#Stars question
for i in range(1, 11):
    for x in range(i):
        print('*', end='')
    print()

#Multiplication table
for i in range(1,11):
    for j in range(1,11):
        print(i * j ,end = ",")
    print()

# Prime numbers between 10 and 60
print("Prime numbers between 10 and 60 are:")
for number in range(10, 61):
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime and number > 1:
        print(number)

############################################### Practice ########################################
#secret_number
secret_number = 80
sum_numbers = 0
answer = input("Would you like to play?")

while answer == "yes":
    user_number = int(input("Enter number: "))
    sum_numbers += user_number
    if sum_numbers > secret_number:
        print("GAME OVER")
        break
    elif sum_numbers == secret_number:
        print("you win")
        break
    print("We didn't reached the secret value")
    answer = input("Would you like to play?")