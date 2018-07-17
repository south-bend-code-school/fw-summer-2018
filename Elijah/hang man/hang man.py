import sys, random

def select_random_word():
    words_file = open("words.txt")
    words = words_file.readlines()
    random_word_index = random.randint (0, len (words) -1)
    random_word = words[random_word_index].strip()
    return random_word

    play = "y"
    wins = 0
    losses = 0
    print("wecom to hangman! let's play to quit during the game,ente \"quit!\" as your guss")
    while (play == 'y' or play == 'yes'):
        play = ""
        random_word = slect_random_word()
        correct_gesses = []
    incorrect_gesses = []
    chances = 10
    print("chances left: ", cances
    print("/insecret word: ")
    while game_over is not true:
        for letter in random_word:
            if letter in correct_gesses
                     print(letter, end=' ')
                     else:
                         print("_", end='')
        guess = input("n/ngusses one letter, or the entire word: ")
   if guess == "quit!":
      losses += 1
      game_over = true
      break
  elif guess == radom_word:
      print("you win the secrit word was \"{}" .format(random_word))
      game_over =treue
      win +=
  elif len(guess) >1;
       print("you incorreectly guessed the word\n")
        chances -=1
          print("chances left: ", chances
  elif guess in correct_guesses or guess in incorrect_guesses
       print("you'ev  alredy  guessed that that letter /n")
  elif guess in random_word:
       correct_guesses.append(guss)
       print("inccorect!")
       print("chances left: ", chances)
   else:
       inccorect_guess
        
          
