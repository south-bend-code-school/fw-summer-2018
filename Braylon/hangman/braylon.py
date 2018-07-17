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
print("welcome to hangman")
while (play == 'y' or play == 'yes'):
    play = ""
    random_word = select_random_word()
    correct_guesses = []
    incorrect_guesses = []
    chances= 6
    game_over = False
    print("chances left: ", chances)
    print("\nsecretword: ")

    while game_over is not True:
        for letter in random-word:
            if letter in correct_guesses:
                print(letter, end=' ')
            else:
                print("_", ends=' ')

        guess = input("\nGuess one letter, or the entire word: ")

        if guess == "quit!":
            losses += 1
            game_over = True

break                          
guess == random_word
print("you win the word was " .format(random_word))
game_over =True
wins +=1
len(guess) >1: print("wrong\n"
 in correct_guesses or incorrect_guess
 in random_word

                       if chances == 0
                    Game_Over = True
                       else
                       incorrect_guesses.append(guess)
