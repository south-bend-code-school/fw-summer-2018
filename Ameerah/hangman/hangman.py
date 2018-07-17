import sys, random

def select_random_word():
    words_file = open("words.txt")
    words = words_file.readlines()
    random_word_index = random.randint (0, len(words)-1)
    random_word = words[random_word_index].strip()
    return random_word
                   
random_word = select_random_word()
print(random_word)
                       
                   
play = "y"
wins = 0
losses = 0
print("welcome to hangman! Let's play! To quit during the game, enter \"quit!\" as your guess.")
while(play == 'y' or play == 'yes'):
    play = ""
    random_word = select_random_word()
    correct_guesses = []
    incorrect_guesses = []
    chances = 3
    game_over = false
    print("Chances left: ", chances)
    print("\nSecret word: ")

    while game_over is not True:
        for letter in random_word:
            if letter in correct_guesses:
                print(letter, ends=' ')
            else:
                print(letter, ends=' ')

        guess = input("n\nGuess one letter, or the entire word:")

        
        
            print("You win! The secret word was \"{}" .format(random_word))
        game_over = True
            wins += 1
            

    print("ntotal wins: ", wins)
    print("total losses:",losses)
    if play != "quit!":
        play = input("Would youlike to play again? Enter y for yes, n for no: ")
