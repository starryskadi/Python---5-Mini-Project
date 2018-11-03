import random
number = random.randint(1,10)

print("A  Number have been randomly generated")
question = int(input("Guess the number between 1 to 10 > "))

while question != number:    
    if question < number:
        print("The Number is too Low")
        question = int(input("Please Guess the number between 1 to 10 Again > "))
    else:
        print("The Number is too High")
        question = int(input("Please Guess the number between 1 to 10 Again > "))
else:
    print("You got the correct number")
    
