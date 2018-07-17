import sys, random

def select_random_word():
    words_file = open("words.txt")
    words = words_file.readlines()
    random_word_index = random.randint (0, len(words) -1)
    random_word = words[random_word_index].strip()
    return random_word

play ="y"
wins = 0
losses = 0
print ("Welcome to Hangman! Let's play!To quit during the game,enter\"quit!\" as you guess.")
while (play == 'y' or play == 'yes'):
    play =""
    random_word = select_random_word()
    correct_guesses =[]
    incorrect_guesses =[]
    chances = 6
    game_over =False
    print("Chances left:",chances)
    print(" word\nSecrect word:")

    while game_over is not True:
        for letter in random_word:
            if letter in correct_guesses:
                print (letter, end=' ')
            else:
                print("_", end=' ')

        guess = input("\n\nGuesses one letter, or the entire word:")

        if guess == "quit!":
            play ='n'
            break
        elif guess == random_word:
            print("You win! the secret word was\"{}" . format(random_word))
            game_over = True
            win += 1
        elif len(guess) > 1:
            print ("You've alredy guessed that letter!\n")
        elif guess in random_word:
            correct_guesses.append(guess)
            chances -= 1
        else:
            incorrect_guesses.append(guess)
            chances -=1
            if chances == 0:
                print("You lose! the word was\"{}" .format(random_word))
                game_over = True
                losses += 1
            else:
                print("Incorrect!")

        if chances == 6:
           print("_ _ _ _ ,")    
           print(" |")
           print(" |") 
           print(" |")
           print("_| _ _ _ _ _ _")     
        if chances == 5:
           print("_ _ _ _ ,")    
           print(" |       O")
           print(" |") 
           print(" |")
           print("_| _ _ _")
        if chances == 4: 
           print("_ _ _ _ ,")    
           print(" |       O")
           print(" |       T")
           print(" |")
           print("_| _ _ _ _ _ _")
        if chances == 3: 
           print("_ _ _ _ ,")    
           print(" |       O")
           print(" |      |T")
           print(" | ")
           print("_| _ _ _ _ _ _")
        if chances == 2: 
           print("_ _ _ _ ,")    
           print(" |       O")
           print(" |      |T|")
           print(" |")
           print("_| _ _ _ _ _ _")
        if chances == 1: 
           print("_ _ _ _ ,")    
           print(" |        O")
           print(" |       |T|")
           print(" |        |")
           print("_| _ _ _ _ _ _")
        if chances == 0: 
           print("_ _ _ _ ,")    
           print(" |        O")
           print(" |       |T|")
           print(" |       | |")
           print("_| _ _ _ _ _ _")



        if len(correct_guesses) == len(set(random_word)):
            print("You win! the secret word was\"{}" . format(random_word))
            game_over = True
            wins += 1

    print("\ntotal wins: ", wins)
    print("\ntotal losses : ", losses)
    if play != "quit":
        play = input ("Would you like to play agian? Enter y for yes n for no:")

    
