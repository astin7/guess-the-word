import random
import sys

# function to play the game
def guess_the_word():
    # initializes the variables
    letter_guesses = [] # list to store guessed letters
    word = choose_word() # randomly chooses a word
    attempts = 5 # sets the attempts per game to 5

    print("Welcome to guess the word!") # welcome statement to the game
    
    # while the user still has attempts, it will go on with the game
    while attempts > 0: 
        # displays current game status
        print(f"Attempts left:", attempts)
        current_display = display_word(word, letter_guesses)
        print(f"Current word: {current_display}")

        # checks if the word has been completely guessed
        if "_" not in current_display:
            print("Congratulations you guessed the word!")
            break

        # prompts user to guess a single letter
        guess = input("Enter a single letter: ")
        # makes sure the input is valid
        if len(guess) == 1 and guess.isalpha():
            # checks if the letter was already guessed
            if guess in letter_guesses:
                print("You already guessed that letter. Try again.")
            # checks if the letter is correct
            elif guess in word:
                print("Correct guess!")
            else:
                print("Incorrect guess!")
                attempts -= 1 # decreases attempts if incorrect

            letter_guesses.append(guess) # adds the guess to the letter_guesses list
        else:
            print("Invalid input. Please enter a single letter.")
    
    # checkes to see if you run out of attempts
    if attempts == 0:
        print(f"You ran out of attempts! The word was {word}")

    # prompts user to play again if they finish the game
    ask_user_to_play_again()

def choose_word():
    # randomly chooses a word of the list
    WORD_CHOICES = ["programming", "python", "algorithm", "arrays", "arithmetic", "operators"]
    return random.choice(WORD_CHOICES)

# this function displays the word
def display_word(chosen_word, player_guesses):
    display = ""

    for letter in chosen_word:
        # if the letter is the word is in player_guesses, it will add the word to the display, otherwise displays _
        if letter in player_guesses:
            display += letter
        else:
            display += "_"
    return display

# prompts the user to play again
def ask_user_to_play_again():
    try:
        user_choice = input("Do you want to play again? (y or n) ")
        # if the user inputs y, the game will rerun
        if user_choice.lower() == "y":
            guess_the_word()
        # if the user inputs n, the game will exit
        elif user_choice.lower() == "n":
            sys.exit()
        # if the user inputs something valid, it will display an error message and asks them again
        else:
            print("Please select a valid answer (y or n) ")
            ask_user_to_play_again()
    # if the user inputs something valid, it will display an error message and asks them again
    except ValueError:
        print("Please select a valid answer (y or n) ")
        ask_user_to_play_again()

# entry point of the gaem
if __name__ == "__main__":
    guess_the_word() # starts game when it is executed
