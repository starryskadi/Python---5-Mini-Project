import random

word_list = ["Hangman","apple","Balloon","Cat","Dog","Aeroplane","Addition","Xerophone"]
word = word_list[random.randint(0,4)]
word = word.lower()
temp_word = list("*" * len(word))

lives = 5
user_input = ''


print("Hang Man Game")
print("One Word Have Been Selected")
print("You have:" + str(lives) + "lives")


while list(temp_word) != list(word):
    if lives != 0:
        user_input = input("One character to get full words > ")
        if (len(user_input))  == 1:
            guess_word = user_input.lower()
            if guess_word in word:     
                # temp_word = list(temp_word)                
                # temp_word[word.index(guess_word)] = word[word.index(guess_word)]               
                indices = [i for i, x in enumerate(word) if x == guess_word]
                for each in indices:
                    temp_word = list(temp_word) 
                    temp_word[each] = word[each]                             
                temp_word = "".join(temp_word)     
                print(temp_word)              
                # temp_word = "".join(temp_word)   
            else:
                lives = lives - 1
                print(lives)
        else:
            print("Please Put Only One Charcter")
    else:
        print("You lose!")
        show_word = "".join(word)
        print("The word is : " + show_word)
        break
else:
    print("Congratz,You Win!")

    
