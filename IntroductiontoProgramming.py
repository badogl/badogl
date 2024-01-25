# Adj
adjective1= input("Please enter a adjective name:").lower()
adjective2= input("Please enter how was it:").lower()

# Verbs
verb1= input("Please what was it doing ?:").lower()
verb2= "scream"
verb3= "humiliate"

# Other
exclamation= "Wooow"
animal= input("Please enter a animal name:")
very="very"
apple="apple"
carrot="carrot"

output=""

# Articles
art="a" 


# Story 
x = f"The other day, I was really in trouble. It all started when I saw {art} {very} {adjective1} {animal} {verb1} down the hallway. When I saw this {adjective1} {animal},\n{exclamation}! I yelled. Yes that was {art} {animal} But all I could think to do was to {verb2} over and over. Miraculously,that caused it to stop,\nbut not before it tried to {verb3} right in front of my family.It was {art} {very} {adjective2} memory for me. And although I was humiliated, I wanted to give him {art} {apple}. What I forgot was that he was {art} {animal} and I should have given him {art} {carrot}."

# Split words because we give a number to each word so if art is in the 100th index, the 101st index is the next word.
words=x.split()
    
#List for save next_words
next_words=[]

# We created a variable to keep track of the number of repetitions and use it in the if condition
c=0

# We create a loop to test conditions and constantly check multiple conditions.
for i in range(len(words)):
    
    # We update the after variable so that we can meet our if condition
    art="a"
    
    # We check whether the word i index number in the words we divided is the same as art.
    if words[i] == art:
        
        # We increase c so that we know which cycle we are in and can use it in the conditions.
        c+=1
        
        # Here we check whether art is the last word of the sentence or not.
        if i<len(words) - 1:
            
            # Here we get the next word. words were split words, we knew the index of these words with i and we got the next word with i + 1
            next_word=words[ i + 1 ]           
            
            # We check which letter the next word starts with and make a selection according to the spelling rule. In vowels, an becomes a in consonants.
            if next_word.startswith(("a","e","o","i","u")):
                art="an"
            else:
                art="a"
            
            # Here I parsed each art myself, but a better way can be followed. I can't say that the path I followed is very logical.
            # But this way I was able to adjust the outputs and add easily.
            if c == 1:
                output +=f"The other day, I was really in trouble. It all started when I saw {art} {very} {adjective1} {animal} {verb1} down the hallway. When I saw this {adjective1} {animal},{exclamation}! I yelled."
            elif c == 2:
                output +=f" Yes that was {art} {animal} But all I could think to do was to {verb2} over and over."
            elif c == 3:
                output +=f" Miraculously,that caused it to stop,but not before it tried to {verb3} right in front of my family.It was {art} {very} {adjective2} memory for me."
            elif c== 4:
                output +=f" And although I was humiliated, I wanted to give him {art} {apple}. " 
            elif c== 5:
                output +=f" What I forgot was that he was {art} {animal} and I should have given him "
            elif c== 6:
                output +=f"{art} {carrot}."
            
# In my operations, I combined the sentences I assigned to a variable into that variable and I get an output in the form of print.
print(output)