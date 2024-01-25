import random

"""
I gave the player the right to enter 4 words.
For the words I left embedded in my system, I left clues as to what they were. And I opened some letters of these words. 
In order for the game to loop constantly and not for the user to constantly open the letters, I first gave the user three rights.
Then, if the word was shorter than three letters and the user noticed this and did not constantly open the clue letters,
I ended the game if the clue was opened as long as the word. (So if keli has two letters and if he tries to open the second clue letter after the first clue letter, the game is already over.)
The reason why I did this was that if an 8-letter word was chosen in the game and we had 9 rights, not every word could be opened. At the 8th letter, the game would end without the player winning.
"""

# Variables
secret_words=["apple","banana","rabbit"]
guess_number=0
x=0
hint_number=0

# Request word from user
while x < 4:
    x+=1
    user_words=input(f"Please enter {x}. word? ({5-x} more) ")
    secret_words.append(user_words.lower())
print(secret_words)


# Choose a word
choosen_word=random.choice(secret_words)

"""
If you want know choosen word you can just show yourself with that code and you can try positive and negative situations

print(choosen_word)

"""



# Loop for ask choosen word
while True:
    print("\nDo not forget you have 6 chance for try!\n")
    
    # retur words in list(secret_words)
    for i in secret_words:
        
        print("")
        c=0
 
        # return letter
        for x in i:
            c+=1
            number=random.choice(range(0,10))
            if c == number:
                print(x,end="")
                continue            

            elif x ==" ":
                a=" "
                print(" ", end="")
                continue
                
            else:
                b="_"
                print("_", end="")
                continue
            
        # hint for words     
        if i == secret_words[0]:
            print(" (This is a fruit and this fruit may be red and round)")
            continue
        elif i == secret_words[1]:
            print(" (This is a fruit and monkeys love this fruit very much.)")
            continue
        elif i == secret_words[2]:
            print(" (This is an animal and this animal is defeated by the turtle in this story.)")
            continue
        else:
            print(" (You know what is that)")
        print("")
        
    # Chosen word's hint    
    for i in choosen_word:
            if i == " ":
                print(" ",end="")
                
            else:
                print("_", end="")
    
    # Loop for request from user and check it            
    while True:
        # Increase guess number 
        guess_number+=1
        
        # Take last letter index
        last_letter_index=len(choosen_word)-1       
        print("")
        # Ask to user what is the his answer 
        guess_word=input("\nPlease guess which of the words you gave me I chose: ").lower()
        
        # Check for len is it same with the answer
        if len(guess_word) == len(choosen_word):
            print("\nThere is a hint for you!\n")
            index_choosenword=0
            hint_number+=1
            
            
            # Show hints
            for i in choosen_word:
                index_choosenword+=1
                if index_choosenword <= hint_number:
                        print(i,end="")
                    
                elif i == " ":
                    print(" ",end="")
                    
                else:
                    print("_",end="")
            
            
            # check for is it 2. hint?
            if hint_number==2:
                print("")
                print(f"You get your {hint_number}. hint! But do not forget you cannot try forever!")
                continue
            
            
            # Check for is it last letter of word and done game
            elif last_letter_index + 1 == hint_number:
                print("")
                print("\nThere are no more letters left to give clues! Game over!\n")
                break
            
            
                
                     
  
                 
        # Warning for finish game
        if guess_word == choosen_word:
            print("\nYes that is right word!\n")
            break
        
        # Warning for last chance
        elif guess_number == 3-1:
            print("\nThis is your last chance!\n")
            continue
        
        # Warning for done choose chance
        elif guess_number == 3:
            print("\nThis was the wrong choice I guess you can try more\n")
            break
        
        # Warning for you can try more
        else:
            print("\nThis was the wrong choice I guess you can try more\n")
            continue
        

    # Show number of guess 
    print(f"Your number of guess is {guess_number}")
    
    break