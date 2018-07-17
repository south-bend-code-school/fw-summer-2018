import sys, random

def select_random_word():
    words_file = open("words.txt")
    words = words_file.readlines()
    random_word_index = random.randint(0,len(words)-1)
    random_word = words[random_word_index].strip()
    return random_word

play = "y"
wins = 0
losses = 0
print("Hey, play my hangman game. Do it. To quit, enter \"quit\" as your guess.")
while(play == 'y' or play == 'yes'):
    play = ""
    random_word = select_random_word()
    correct_guesses = []
    incorrect_guesses = []
    chances = 6
    game_over = False
    print("Chances left:",chances)
    print("\nSecret word:")

    while game_over is not True:
        for letter in random_word:
                if letter in correct_guesses:
                    print(letter, end='')
                else:
                    print("_", end=' ')

        guess = input("\nuess one letter or, the entire word.")

        if guess == "quit!":
            losses += 1
            game_over = True
            break
        elif guess == random_word:
            print("YOU WIN!!!THE SECRET WORD WAS \"{}" .format(random_word))
            game_over = True
            wins += 1
        elif len(guess) >1:
            print("you are wrong\n")
            chances -= 1
            print("Chanses left:  ", chanses)
        elif guess in correct_guess or guess in incorrect_guesses:
            print("You already said that.\n")
        elif guess in random_word:
            print("Yay you did it")
            print("Chanses left: " ,chances)
        else:
            incorrect_guesses.append(guess)
            chances -= 1
            if chances == 0:
                print("HAHA! YOU LOST! The secret word was\"{}" .format(random_word))
                game_over = True
                losses += 1
            else:
                print("Incorrect!")
                print("Chances left: ", losses)

        if len(correct_guesses) == len(set(random_word)):
            print("You won. Yay. The correct word was: \"{}" .format(random_word))
            game_over = True
            wins += 1
               
    print("\nTotal wins: ", wins)
    print("yoyal losses: ", losses)
    if play == "quit!":
               play = input("Do you wanna play again? Enter y for yes and n for no: ")
