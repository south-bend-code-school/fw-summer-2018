import sys, random

def select_random_word():
    words_file = open("words.txt")
    words = words_file.readlines()
    random_word_index = random.randint (0, len(words)-1)
    random_word = words[random_word_index].strip()
    return random_word

play = "y"
wins = 0
losses = 0
print  ("Welcome to Hangman! Let's Play! To quit during the game, enter \"quit!\" as your guess")
while (play == 'y' or play == 'yes'):
    play = ""
    random_word = select_random_word()
    correct_guesses = []
    incorrect_guesses = []
    chances = 8
    game_over = False
    print("Chances left: ", chances)
    print ("\nSecret word: ")

    while game_over is not True:
        for letter in random_word:
            if letter in correct_guesses:
                print (letter, end='')
            else:
                print("_", end=' ')
        guess = input("\n\nGuess one letter, or the entire word: ")

        if guess =="quit!":
            play = 'n'
            losses += 1
            game_over = True
            break
        elif guess == random_word:
            print("You win! The secret word was\"{}".format(random_word))
            game_over = True
            wins += 1
        elif len(guess) > 1:
            print("You incorrectly guessed the word!\n")
            chances -= 1
        elif guess in correct_guesses or guess in incorrect_guesses:
            print("You've already guessed that letter!\n")
        elif guess in random_word:
            correct_guesses.append(guess)
        else:
            incorrect_guesses.append(guess)
            chances -= 1
            if chances == 0:
                print("You lose! The word was \"{}".format(random_word))
                game_over = True
                losses += 1
            else:
                print("Incorrect!")
                print("Chances left ", chances
                if len(correct_guesses) == len(set(random_word))
                    print("You win! The secret word was\"{}".format(random_word))
            game_over = True
            wins += 1

    print("\nTotal wins: ",wins)
    print("Total losses:",losses)
    if play != "quit!":
        play = input("Would you like to play again? Enter y for yes, n for no")


            
