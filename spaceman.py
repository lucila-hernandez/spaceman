import random

def load_word():
    '''
    Open the file titled words.txt. Read all the content from the file and save it in a list called word list. Close the file words.txt
    Choose a random word from the words list. Return the random word that was selected from the list.

    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') 
    secret_word = random.choice(words_list)
    return secret_word



def is_word_guessed(secret_word, letters_guessed):
    '''
    Get a random word the player is trying to guess.
    For each letter that is in the secret word chosen.If a letter has not been guessed it will let the player know. If the letter has been guessed it will let the player know.
    '''

    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
  

def get_guessed_word(secret_word, letters_guessed):
    '''
    The random word the player is trying to guess. 
    If the player guessed a letter correctly it will show the letter where it appears in the word. If the letter has not been guessed it will show an underscore _ where a letter would be. 
    Show  the result of the letters guessed within the word and the letters still missing. 
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    guessed_word = ""

    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else: 
            guessed_word += "_"

    return guessed_word



def is_guess_in_word(guess, secret_word):
    '''
    Taking the players guessed letter and checking if the letter guessed is found in the secret word.
    If it is in the secret word it will be true if it’s not it won’t be true. 

    '''
    #TODO: check if the letter guess is in the secret word

    return guess in secret_word




def spaceman(secret_word):
    '''
    Starting the spaceman game with an introduction and a secret word that the player needs to guess. It will show _  for the empty letters guessed so far. And It will show the number of guesses that were incorrect and it will also give the player 7 chances to guess. 
    As long as the game is not over it will show the word with the letters that have been guessed and _ for the letters that need to be guessed. The player will be asked to guess a letter. 
    Checking to see if the guessed letter is in the secret word. If the letter is in the word the letter will be added to the list of guessed letters and the player will know they guessed correctly. If the letter guessed is not in the word, the number of incorrect guesses will increase by 1 and the player will know they guessed incorrectly. 
    If the player guessed all the letters correctly they win. If the player reached the max amount of guesses they will loose. 
    The game will end and show the results to the player. They will know if they won or lost. 

    '''
    game_state = {
        "letters_guessed": [],
        "incorrect_guesses": 0,
        "max_incorrect_guesses":  7
    }

    #TODO: show the player information about the game according to the project spec
    print("👋 Hi! Welcome to Spaceman, the guessing game!" ) 
    print("🔍 You get 7 chances to discover what the mystery word is.")
    print("🚀 Let's get started!")
    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
