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
    
        
        
