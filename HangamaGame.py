import random
incorrect=0
max_atempt=6
list_word=["apple","banna"]
gues_letter=[]
word=random.choices(list_word)
print("Welcome the Hangama Game")
while incorrect<max_atempt:
    display=""
    for letter in word: 
        if letter in gues_letter:
            display+=letter
        else:
            display+="_"
    print("word:",display)
    if "_" not in display:
        print("Congratulation You Win the game")
        break
    gues=input("Enter a word").lower()
    if gues in gues_letter:
        print("you already guess it try again")
        continue
    gues_letter.append(gues)
    
    if gues not in word:
        incorrect+=1
        print(f" Wrong guess and left atempts is : {max_atempt - incorrect}")
    else:
        print("good guess")
if incorrect==max_atempt:
    print(F"you loss the game the word is {word}")
    
        
        
"""import random

words = ["orange", "apple"]
incorrect = 0
wrong_attempt = 6
word = random.choice(words)
guess_l = []

print("Welcome to the hangman game!")

while incorrect < wrong_attempt:
    display_letter = ""
    
    # Word display banaye
    for letter in word:
        if letter in guess_l:
            display_letter += letter
        else:
            display_letter += "_"
    
    print("Word:", display_letter)
    
    # Win check yahan pe
    if "_" not in display_letter:
        print("You win the game!")
        break
    
    guess = input("Guess a letter: ").lower()
    
    # Check kare pehle guess ho chuka hai ya nahi
    if guess in guess_l:
        print("Already guessed that letter!")
        continue
    
    guess_l.append(guess)
    
    # Check kare guess sahi hai ya galat
    if guess not in word:
        incorrect += 1
        print(f"Wrong guess! Attempts left: {wrong_attempt - incorrect}")
    else:
        print("Good guess!")
    
    print()  # Blank line for readability

# Agar saare attempts khatam ho gaye
if incorrect == wrong_attempt:
    print(f"You lose! The word was: {word}")
    

list_word=["amna","jannat","ayesha"]
incorect=0
max_wrong=6
word=random.choice(list_word)
guess_letter=[]
while incorect<=max_wrong:
    display=""
    for letter in word:
        if letter in guess_l:
            display+=letter
        else:
            display+="_"
    print("word:",display)
    if "_" not in display:
        print("you r win")
        break
    gues=input("enter word").lower()
    if guess in  guess_letter:
        print("alrady gues")
    guess_letter.append(gues)
    if gues not in word:
        incorect+=1
        print("worng")
    else:
        print("Good")
    print()
if incorect==wrong_attempt:
    print(f"you loss:{word}")"""