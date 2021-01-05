import random
def hangman():
    list_of_words = ["india" , "hangman" ,"newyear" , "mandrem" , "beach"]
    word = random.choice(list_of_words)
    turns = 5
    guessmade =''
    a = set("abcdefghijklmnopqrstuvwxyz")
    
    while len(word)>0:
        main_word = ""
        
        for letter in word:
            if letter in guessmade:
                main_word = main_word+letter
            else:
                main_word = main_word+"_ "
            
        if main_word==word:
            print(main_word)
            print("YOU WON")
            break
        
        
        print("guess the word" , main_word)
        guess =input()
        
        if guess in a:
            guessmade = guessmade+guess
        
        else:
            print("enter valid character")
            guess = input() 

        if guess not in word:
            turns = turns-1


            
            if turns ==4:
                print("4 turns left")
                print("--------------")
                print("       O      ")
                print("       |       ")
                
            if turns ==3:
                print("3 turns left")
                print("--------------")
                print("       O      ")
                print("       |       ")
                print("      / \      ")
                
            if turns ==2:
                print("2 turns left")
                print("--------------")
                print("      \O/      ")
                print("       |       ")
                print("      / \      ")
                
            if turns ==1:
                print("this is your final chance or else you DIE")
                print("--------------")
                print("      \O/_|    ")
                print("       |       ")
                print("      / \      ")
                
            if turns ==0:
                print("You loose")
                print("You let a innocent man DIE")
                print("--------------")
                print("       O_|    ")
                print("      /|\       ")
                print("      / \      ")
                
            
name = input("enter your name ")
print("WELCOME" , name, "!")
print("--------------------------------")
print("try to guess the word in less than 5  attempts")
hangman()
