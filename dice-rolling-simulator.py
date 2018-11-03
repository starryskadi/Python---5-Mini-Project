import random

question = input("Do you Wanna Roll the dice? (Y/N)")
while question == "Y": 
    number = random.randint(1,6)
    number2 = random.randint(1,6)
    print(number)
    print(number2)
    question = input("Do you Wanna Roll Again? (Y/N)")    
