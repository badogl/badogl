import time

# I created a story over three levels, for convenience in making choices, you can make choices not only by typing the option, but also by numbers.
# I had the user choose the boot color and jersey number (2-99) and used it in the story. And at the end of the game, I returned it to the user which paths he chose.
# I care about invalid user input
# The game was very enjoyable. "It became very enjoyable with creative dialogues."
# There is scenario more than one in choose crampon color


user_name=input("Please enter your name:")
chosen_sections=[]
jersey_number=""

while True:
        print(f"{user_name.title()} you are a very good football player and you had your first training with the team after a long injury break. \
After a good training session, your coach asks you: 'The next match is very important, are you ready to play in the starting eleven?' he asks, and you;")
        section=input("1)Yes! \n\
2)No!\n(1/2 or Yes/No):")
        # Save answers to chosen_section
        chosen_sections.append(section)
        
        # Check answer for Yes or No
        if section.lower() == "yes" or section=="1":
            print("\nYou confidently said 'yes I'm ready for this and I've always been waiting for this moment'\n")
            time.sleep(1)
            
            while True:
                # Asking jersey number
                print(f"And your coach says to you 'that's great {user_name}, I'm glad to hear that, what number jersey do you want to wear?' he asked,")
                section=input("and you said: ")
                jersey_number=section
                
                # Save answers to chosen_section
                chosen_sections.append(section)
            
                # Genarate valid jersey numbers
                valid_jersey_numbers = [str(i) for i in range(1,100)]
                
                # Choose valid jersey number
                if section in valid_jersey_numbers and section != "1":
                    # Which number you are wearing
                    print(f"\nNow you're wearing {jersey_number} like a star")
                    
                    while True:
                        # Matchday Talk 
                        print(f"\nDays passed and the match day came. Your coach started to give a speech for the match. And he turned to you and said,\
    'Come and make a speech as the team captain, now the floor is with the team captain {user_name}.")
                        
                        section=input("\nAnd you are thinking about how to give a speech,\n 1)Encourage, 2)Praise; (1/2 or Encourage/Paraise)")
                        
                        # Save answers to chosen_section
                        chosen_sections.append(section)
                        
                        # Encourage option
                        if section.lower()=="encourage" or section=="1":
                            # Talk
                            print("We have achieved a lot with you so far, you can do this! And now it's time to prepare after that go and show them\n")
                            
                            # Choose your crampon
                            crampon_color=input(f"You're starting to get ready, which color cleats do you want to wear?(Red,Blue,Purple,Yellow):")
                            
                            # Check for crampon color
                            if crampon_color.lower() in ("yellow","red","blue","purple"):
                                print(f"\nThe match has started and you are on the field with your {crampon_color.lower()} colored boots, the first sixty minutes are over.\
You tried so hard but you couldn't do anything, what's that! Your team won a corner. And you;")
                                
                                # Corner
                                section=input("You looked around and saw that you had two options;\n 1)You could cross the ball into the penalty area and assist your teammate.\n \
2)You can pass the ball to your friend coming towards you and take possession of the ball more clearly?\n (1/2 or Crossing ball/Possessing the ball)")   
                                
                                # Save answers to chosen_section
                                chosen_sections.append(section)
                                
                                # Possessing the ball
                                if section.lower() == "possessing the ball" or section == "2":
                                    print("\nYou passed the ball to your friend nearby and he threw the ball back to you, creating free space in front of you, and you took advantage of this free space, crossed inside, \
and then sent the ball with a stylish shot towards the corner of the goal, scoring a perfect goal.")
                                    section=input("You have to do something to be happy after the perfect goal you scored, and you;\n \
1) You wanted to go to your coach and thank him. \n \
2) You wanted to hug your girlfriend  \n \
3) Gathered together with your team and celebrated (1/2/3 or Coach/Girlfriend/Teammates)\n")
                                    
                                    # Go to Coach
                                    if section.lower()=="coach" or section == "1":
                                        print(f"your {section.lower()} was very happy about this. And the match ended with this score, journalists came to you for an interview.")
                                        section=input("Journalists ask you how you felt after you scored, and you say;\n\
1) You say you are absolutely happy that you scored in this important match. \n \
2) Since this was a very normal thing for you, you did not feel anything extra. (1/2 or I am happy/It is quite normal)\n")
                                        
                                        
                                        # How did you feel
                                        if section.lower() == "i am happy" or section=="1":
                                            print("You are very happy to score this goal. When you look at the scoreboard, you say you see peace there.\n")
                                            print(f"Thank you {user_name.title()} for playing my game and congratulations you have written your own story.")
                                            break
                                        elif section.lower()=="it is quite normal" or section=="2":
                                            print("It was a perfectly normal match for you and you did your duty.\n")
                                            print(f"Thank you {user_name.title()} for playing my game and congratulations you have written your own story.")    
                                            break
                                        else:
                                            print("Please enter valid options!")
                                            continue
                                    
                                    # Go to Girlfriend
                                    if section.lower()=="girlfriend" or section == "2":
                                        print(f"your {section.lower()} was very happy about this. And the match ended with this score, journalists came to you for an interview.")
                                        section=input("Journalists ask you how you felt after you scored, and you say;\n\
1) You say you are absolutely happy that you scored in this important match. \n \
2) Since this was a very normal thing for you, you did not feel anything extra. (1/2 or I am happy/It is quite normal)\n")
                                        
                                        # How did you feel
                                        if section.lower() == "i am happy" or section=="1":
                                            print("You are so happy that you scored this goal on this important match and you gift it to your girlfriend.\n")
                                            print(f"Thank you {user_name.title()} for playing my game and congratulations you have written your own story.")
                                            break
                                        elif section.lower()=="it is quite normal" or section=="2":
                                            print("It was a normal match for you and that's why you said you were going to get out of here and go out with your girlfriend.\n")
                                            print(f"Thank you {user_name.title()} for playing my game and congratulations you have written your own story.")    
                                            break
                                        else:
                                            print("Please enter valid options!")
                                            continue
                                    
                                    # Go to Teammates
                                    if section.lower()=="team mates" or section == "3":
                                        print(f"your {section.lower()} was very happy about this. And the match ended with this score, journalists came to you for an interview.")
                                        section=input("Journalists ask you how you felt after you scored, and you say;\n\
1) You say you are absolutely happy that you scored in this important match. \n \
2) Since this was a very normal thing for you, you did not feel anything extra. (1/2 or I am happy/It is quite normal)\n")
                                        
                                        # How did you feel
                                        if section.lower() == "i am happy" or section=="1":
                                            print("You're absolutely excited, you wouldn't have scored this goal without your teammates.\n")
                                            print(f"Thank you {user_name.title()} for playing my game and congratulations you have written your own story.")
                                            break
                                        elif section.lower()=="it is quite normal" or section=="2":
                                            print("You don't feel excited because if it wasn't you, someone else would have done it anyway.\n")
                                            print(f"Thank you {user_name.title()} for playing my game and congratulations you have written your own story.")    
                                            break
                                        else:
                                            print("Please enter valid options!")
                                            continue  
                                          
                                # Crossing ball   
                                elif section.lower() == "crossing ball" or section == "1":
                                    print("You opened a very good cross into the penalty area, allowing your teammates to head it, and your teammate made this cross a goal, and you ran towards him to celebrate.")
                                    print("And the match ended with this score, journalists came to him for an interview.\n")
                                    section=input("Journalists ask you how you felt after you asist, and you say;\n\
1) You say you are absolutely happy that you asist in this important match. \n \
2) Since this was a very normal thing for you, you did not feel anything extra. (1/2 or I am happy/It is quite normal)\n")
                                    
                                    # Save answers to chosen_section
                                    chosen_sections.append(section)
                                        
                                        # How did you feel
                                    if section.lower() == "i am happy" or section=="1":
                                        print("\nIt was certainly a pleasure for you to assist and you think you deserve a congratulations\n")
                                        print(f"Thank you {user_name.title()} for playing my game and congratulations you have written your own story.")
                                        break
                                    elif section.lower()=="it is quite normal" or section=="2":
                                        print("Even though you made a great assist, you say that the assist is not important, the goal is important, so you are not very excited.\n")
                                        print(f"Thank you {user_name.title()} for playing my game and congratulations you have written your own story.")    
                                        break
                                    else:
                                        print("Please enter valid options!")
                                        continue  
                                else:
                                    print("Please enter a valid option")
                                    continue
                        
                        
                        # Paraise option
                        elif section.lower()=="paraise" or section=="2":
                            print("You guys are talented enough to do this, each of you has velvet wrists. There is no other team that is this talented! And now it's time to prepare after that go and show them\n")
                            
                            # Choose your crampon
                            crampon_color=input(f"You're starting to get ready, which color cleats do you want to wear?(Red,Blue,Purple,Yellow):")
                            
                            # Check for crampon color
                            if crampon_color.lower() in ("yellow","red","blue","purple"):
                                print(f"\nThe match has started and you are on the field with your {crampon_color.lower()} colored boots, the first sixty minutes are over.\
You tried so hard but you couldn't do anything, what's that! Your team won a corner. And you;")
                                
                                # Corner
                                section=input("You looked around and saw that you had two options;\n 1) You could cross the ball into the penalty area and assist your teammate.\n \
2)You can pass the ball to your friend coming towards you and take possession of the ball more clearly?\n (1/2 or Crossing ball/Possessing the ball)")   
                                
                                # Save answers to chosen_section
                                chosen_sections.append(section)
                                
                                # Possessing the ball
                                if section.lower() == "possessing the ball" or section == "2":
                                    print("\nYou passed the ball to your friend nearby and he threw the ball back to you, creating free space in front of you, and you took advantage of this free space, crossed inside, \
and then sent the ball with a stylish shot towards the corner of the goal, scoring a perfect goal.")
                                    section=input("You have to do something to be happy after the perfect goal you scored, and you;\n \
1) You showed your joy by going to the coach who gave you this chance  \n\
2) You wanted to go to your girlfriend and share your joy with her  \n\
3) You wanted to go to your teammates and share your joy (1/2/3 or Coach/Girlfriend/Teammates)\n")
                                    
                                    # Save answers to chosen_section
                                    chosen_sections.append(section)
                                    
                                    # Go to Coach
                                    if section.lower()=="coach" or section == "1":
                                        print(f"your {section.lower()} was very happy about this. And the match ended with this score, journalists came to you for an interview.")
                                        section=input("Journalists ask you how you felt after you scored, and you say;\n\
1) You say you are absolutely happy that you scored in this important match. \n \
2) Since this was a very normal thing for you, you did not feel anything extra. (1/2 or I am happy/It is quite normal)\n")
                                        
                                        # Save answers to chosen_section
                                        chosen_sections.append(section)
                                        
                                        # How did you feel
                                        if section.lower() == "i am happy" or section=="1":
                                            print("'It was a good match, I am very lucky to score this goal, I thank everyone but most of all my coach.' you said\n")
                                            print(f"Thank you {user_name.title()} for playing my game and congratulations you have written your own story.")
                                            break
                                        elif section.lower()=="it is quite normal" or section=="2":
                                            print("It was a good match for you but you said you didn't get much excitement\n")
                                            print(f"Thank you {user_name.title()} for playing my game and congratulations you have written your own story.")    
                                            break
                                        else:
                                            print("Please enter valid options!")
                                            continue
                                    
                                    # Go to Girlfriend
                                    if section.lower()=="girlfriend" or section == "2":
                                        print(f"your {section.lower()} was very happy about this. And the match ended with this score, journalists came to you for an interview.")
                                        section=input("Journalists ask you how you felt after you scored, and you say;\n\
1) You say you are absolutely happy that you scored in this important match.\n \
2) Since this was a very normal thing for you, you did not feel anything extra. (1/2 or I am happy/It is quite normal)\n")
                                        
                                        # Save answers to chosen_section
                                        chosen_sections.append(section)
                                        
                                        # How did you feel
                                        if section.lower() == "i am happy" or section=="1":
                                            print("You said you were very excited and promised your girlfriend about this goal.\n")
                                            print(f"Thank you {user_name.title()} for playing my game and congratulations you have written your own story.")
                                            break
                                        elif section.lower()=="it is quite normal" or section=="2":
                                            print("It was a good match, the goal you scored was legendary, but you said it didn't give you much pleasure.\n")
                                            print(f"Thank you {user_name.title()} for playing my game and congratulations you have written your own story.")    
                                            break
                                        else:
                                            print("Please enter valid options!")
                                            continue
                                    
                                    # Go to Teammates
                                    if section.lower()=="team mates" or section == "3":
                                        print(f"your {section.lower()} was very happy about this. And the match ended with this score, journalists came to you for an interview.")
                                        section=input("Journalists ask you how you felt after you scored, and you say;\n\
1) You say you are absolutely happy that you scored in this important match. \n \
2) Since this was a very normal thing for you, you did not feel anything extra. (1/2 or I am happy/It is quite normal)\n")
                                        
                                        # Save answers to chosen_section
                                        chosen_sections.append(section)
                                        
                                        # How did you feel
                                        if section.lower() == "i am happy" or section=="1":
                                            print("You said that the biggest contribution was from your teammates and that their skills were top-notch and that's why you scored goals.\n")
                                            print(f"Thank you {user_name.title()} for playing my game and congratulations you have written your own story.")
                                            break
                                        elif section.lower()=="it is quite normal" or section=="2":
                                            print("You praised your own skills but said you didn't feel anything special about scoring a goal and said you wanted to go home and rest.\n")
                                            print(f"Thank you {user_name.title()} for playing my game and congratulations you have written your own story.")    
                                            break
                                        else:
                                            print("Please enter valid options!")
                                            continue  
                                          
                                # Crossing ball   
                                elif section.lower() == "crossing ball" or section == "1":
                                    print("You opened a very good cross into the penalty area, allowing your teammates to head it, and your teammate made this cross a goal, and you ran towards him to celebrate.")
                                    print("And the match ended with this score, journalists came to him for an interview.\n")
                                    section=input("Journalists ask you how you felt after you asist, and you say;\n\
1) You say you are absolutely happy that you asist in this important match. \n \
2) Since this was a very normal thing for you, you did not feel anything extra. (1/2 or I am happy/It is quite normal)\n")
                                    
                                    # Save answers to chosen_section
                                    chosen_sections.append(section)
                                        
                                        # How did you feel
                                    if section.lower() == "i am happy" or section=="1":
                                        print("You said that you were happy to make a nice assist and that you would like to go celebrate with your teammates if they let you.\n")
                                        print(f"Thank you {user_name.title()} for playing my game and congratulations you have written your own story.")
                                        break
                                    elif section.lower()=="it is quite normal" or section=="2":
                                        print("You said that it wasn't a very tiring match and that it was static.\n")
                                        print(f"Thank you {user_name.title()} for playing my game and congratulations you have written your own story.")    
                                        break
                                    else:
                                        print("Please enter valid options!")
                                        continue  
                                else:
                                    print("Please enter a valid option")
                                    continue
                        
                        # Other option
                        else:
                            print("Please enter a valid option")
                            continue
                
                # Goalkeepers number    
                elif section == "1":
                    print(f"{user_name.title()} you can not take this number because this is goalkeepers number\n")
                    continue
                
                # Other numbers
                else:
                    print("Please enter a valid number!\n")
                    continue
                break    
            
            
            
        # Check answer for Yes or No
        elif section.lower() == "no" or section=="2":
            print("You said sadly 'I can't wait to play this match, but I don't feel ready enough to play in the starting eleven.'")
            time.sleep(1)
            
            while True:
                # Asking jersey number
                print(f"Your coach asked you, 'No problem {user_name}, I know you will contribute to the team as a substitute, which number would you like to wear in the match?',")
                section=input("and you said: ")
                jersey_number=section
                
                # Save answers to chosen_section
                chosen_sections.append(section)
            
                # Genarate valid jersey numbers
                valid_jersey_numbers = [str(i) for i in range(1,100)]
                
                # Choose valid jersey number
                if section in valid_jersey_numbers and section != "1":
                    
                    # Which number you are wearing
                    print(f"\nNow you're wearing {jersey_number} like a star")
                    
                    # Choose crampon_color
                    print("\nMatch day came and the coach made a speech in the locker room.What color cleats are you preparing to wear,")
                    crampon_color=input("and you:(Red, Blue, Purple, Yellow)")
                    
                    #crampon_color
                    if crampon_color.lower() in ("red","blue","purple","yellow"):
                        
                        # Story
                        print(f"At the 80th minute of the match, you entered the game with your {crampon_color} colored boots. The score is 0-0, and the ball comes to your feet on the right and you:\
1) You took a very elegant shot by pulling the ball to the left side and the goalkeeper could not reach the ball, you scored a perfect goal.\
2) You saw your friend running towards the back and made a perfect assist by giving a very nice through pass.")
                        section=input("(1/2 or Shoot/Pass)")
                        
                        #choosen section
                        chosen_sections.append(section)
                        
                        # Shoot option
                        if section.lower()== "shoot" or section=="1":
                            print("\nAnd the match ended with a score of 1-0, we can say that you became the star of the match even though you came from the bench.\n")
                            print("You scored a great goal and the journalists want to interview you.")
                            section=input("They ask you if you are specially prepared for this, and you say: (1/2 or Yes/No)")
                            
                            #choosen section
                            chosen_sections.append(section)
                            
                            if section.lower()=="yes" or section=="1":
                                print("\nYou said, 'Yeah I always prepare for it and we never know what's going to happen'\n")
                                print("\nAnd you proved to us that you are a star by finishing this game")
                                break
                            elif section.lower()=="no" or section=="2":
                                print("\nYou said, 'No, I don't need to prepare for this, I'm already a star and I'm always ready'")
                                print("\nAnd you proved to us that you are a star by finishing this game")
                                break
                            else:
                                print("Please enter a valid option!")
                                continue
                            
                        
                        
                        # Pass option
                        elif section.lower()== "pass" or section=="2":
                            print("And the match ended with a score of 1-0, we can say that you became the star of the match even though you came from the bench.\n")
                            print("Even if you make a great assist, sometimes journalists may not want to interview you. Don't worry, maybe next time. Get out of here and choose what you want to do.")
                            section=input("1)You want go to home\n2)You want go to training (1/2 or home/training)")
                            
                            #choosen section
                            chosen_sections.append(section)
                            
                            if section.lower()=="home" or section=="1":
                                print("\nEver you did an excellent job today and you definitely deserve to go home")
                                break
                            elif section.lower()=="training" or section=="2":
                                print("\nBy choosing to go to training you definitely prove that you are a star")
                                break
                            else:
                                print("\nPlease enter a valid option!\n")
                                continue
                        
                        
                        
                        
                        else:
                            print("Please enter a valid option!")
                    
                    else:
                        print("Please enter a valid option!") 
                        continue
                    
                
                #Goalkeeper number
                elif section == "1":
                    print(f"{user_name.title()} you can not take this number because this is goalkeepers number\n")
                    continue
                
                # Other Numbers
                else:
                    print("Please enter a valid number!\n")
                    continue
                break     
                   
        #Yes or No else blog
        else:
            print("Please enter valid option!")
            continue
        print(f"\n{chosen_sections}")
        print(f"Your number on the story {jersey_number}")
        break