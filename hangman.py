import random
def hangman():
    list_word=['education','hangman','laptop']
    word=random.choice(list_word)
    turns=10
    guessmade=' '
    valid_enter=set('abcdefghijklmnopqrstuvwxyz')
    while len(word)>0:
        main_word=" "
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_  "
        if main_word==word:
            print(main_word)
            print("your win")
            break
        print("guess the word",main_word)
        guess=input("")
        if guess in valid_enter:
            guessmade+=guess
        else:
            print("enter valid character")
            guess=input("")
        if guess not in word:
            turns=turns-1
            if turns==9:
                print("9 turns left !!!")
                print("----------")
                print("     _    ")
                print("     |     ")
            if turns==8:
                print("8 turns left !!!")
                print("----------")
                print("     _     ")
                print("     |     ")
                print("     O     ")
            if turns==7:
                print("7 turns left !!!")
                print("----------")
                print("     _     ")
                print("     |     ")
                print("     O     ")
                print("     |     ") 
            if turns==6:
                print("6 turns left !!!")
                print("----------")
                print("     _     ")
                print("     |     ")
                print("     O     ")
                print("     |     ")
                print("     /     ")
            if turns==5:
                print("5 turns left !!!")
                print("----------")
                print("     _     ")
                print("     |     ")
                print("     O     ")
                print("     |     ")
                print("     /\    ")    
            if turns==4:
                print("4 turns left !!!")
                print("----------")
                print("     _     ")
                print("     |     ")
                print("    \O     ")
                print("     |     ")
                print("     /\    ")    
            if turns==3:
                print("3 turns left !!!")
                print("----------")
                print("     _     ")
                print("     |     ")
                print("    \O/    ")
                print("     |     ")
                print("     /\    ") 
            if turns==3:
                print("3 turns left !!!")
                print("----------")
                print("     _     ")
                print("     |     ")
                print("    \O/    ")
                print("     |     ")
                print("     /\    ") 
            if turns==3:
                print("3 turns left !!!")
                print("----------")
                print("     _     ")
                print("     |     ")
                print("    \O/    ")
                print("     |     ")
                print("     /\    ")  
            if turns==2:
                print("2 turns left !!!")
                print("----------")
                print("     _     ")
                print("     |     ")
                print("    \O/|   ")
                print("     |     ")
                print("     /\    ")   
            if turns==1:
                print("only 1 turns left !!! hangman on his last breath")
                print("----------")
                print("     _     ")
                print("     |     ")
                print("    \O/_|  ")
                print("     |     ")
                print("     /\    ")  
            if turns==0:
                print(" you loose")
                print("0 you let a good  man die")
                print("----------")
                print("     _     ")
                print("     |     ")
                print("     O _|  ")
                print("    /|\    ")
                print("     /\    ")
                break
name=input("enter ur name  ")
print("welcome", name,"!") 
print("-------------") 
print("try to guess the word in less than 10 attempts")
hangman()  
           
import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")
          
       
       
       

