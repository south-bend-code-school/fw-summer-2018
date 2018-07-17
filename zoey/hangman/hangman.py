import sys, random

def select_random_word():
    word_file = open("words.txt")
    words = words_file.readlines()
    random_word_index = random.randint (0, len(words) -1)
    random_word = words[random_word_index].strip()
    return random_word

play = "Y"
wins = 0
losses = 0
print("hello welcome to my game hangman!to quit during the game enter \"quit!\"as your answer")
while (play == 'y' or play == 'y'):
    play=""
    random_word = select_random_word()
    correct_guesses = []
    incorrect_guesses = []
    chances = 10
    print("chances left: ", chances)
    print("\nsecret word: ")
 
    while game_over is not True:
        for letter in random_word:
            if letter in correct_guesses:
                print (letter, end=' ')
            else:
                print("_", end=' ')

    guess = input("n\nguess one letter, or the intire word: ")

    if guess == "quit!":
        losses += 1
        game_over = true
        break
    elif guess == random_word:
         print("you win! the secret word was \"{}" .format(random_word))
         game_over =True
         wins +=1
    elif len(guess) >1:
           print("you incorrectly guessed the word\n")
           chances -= 1
           print("chances left:, chances)
        
    elif
            guess in correct_guesses or guess in correct_guesses:
           print("you already guessed that letter\n")
                 
    elif
            guess in random_word:
             correct_guesses.append(guess)
            print
             print("chances left: ", chances)
        else:
            incorrect_guesses.append(guess)
            chances -=1
            if chances == 0:
               print("you lose! the secret word was \"{}" .format(random_word))
               game_over = True
               wins +=1

    print("\ntoatal wins: ", wins)
    print("toatal losses: ", losses)
    if play !="quit!":
             play = input("would you like to play again? Enter y for yes, n for no: ")
                 
            
                 

            
                 
                 
    
      
