import sys, random

def select_random_word():
    words_file = open("words.txt")
    words = words_file.readlines()
    random_word_index = random.randint (0, len(words) -1)
    random_word = words[random_word_index].strip()
    return random_word

play = "y"
wins = 0
losses = 0
print("Welcome to Hangman!To Quit press \"Quit!\" on your keyboard")
while (play == 'y' or play == 'yes'):
    play = ""
    random_word = select_random_word()
    correct_guesses = []
    incorrect_guesses = []
    chances = 5
    game_over = False
    print("Chances left: ", chances)
    print("\nSecret word: ")

    while game_over is not True:
        for letter in random_word:
            if letter in correct_guesses:
                print(letter, end=' ')
            else:
                print("_", end=' ')


        guess = input("n\n\Guess one letter, orthe entire word: ")

        if guess == "Quit!":
            losses += 1
            game_over = True
            break
        elif guess == random_word:
            print(" you won! the secret word was \"{}" .format(random_word))
            game_over = True
            wins += 1
        elif len(guess) >1:
            print("you incorectly guessed the word\n")
            chances -= 1
            print("Chances Left: ", chances)
        elif guess in correct_guesses or guess in incorrect_guesses:
            print("You've already guessed that letter\n")
        elif guess in random_word:
            correct_guesses.append(guess)
            print("correct")
            print("Chances Left: ", chances)
        else:
            incorrect_guesses.append(guess)
            chances -= 1
            if chances == 0:
                print("you lose! the word was \"{}" .format(random_word))
                game_over = True
                losses += 1
            else:
                print("incorrect")
                print("Chances Left: ", chances)

        if len(correct_guesses) == len(set(random_word)):
            print("You win! the secret word was \"{}" .format(random_word))
            game_over = True
            wins += 1

    print("\nTotal wins: ", wins)
    print("Total losses: ", losses)
    if play != "Quit!":
        play = input("wouldyou like to play again? Enter y for yes, n for no")
    
