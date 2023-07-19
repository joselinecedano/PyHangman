import random


# word class
class Word:
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
        self.dict = [{"letter": letter, "guessed": False} for letter in chosen_word]

    def update_dict(self, guess):
        #  all the guessed letter are false at first
        guessed = False
        for letter in self.dict:
            # this checks if the guessed letter (guess) is in our chosen word for the game
            if letter["letter"] == guess:
                #  if it is in our word then it will update the letters key = 'guesssed' to  True (meaning its been guessed) and return it back to game()
                letter["guessed"] = True
                guessed = True
        return guessed

    def print_word(self):
        for letter in self.dict:
            if letter["guessed"]:
                # this will update the words display so it shows all the correctly guessed letters in their spot
                print(letter["letter"], end = " ")
            else:
                # this will update the words display with '_' in the place of the letters not yet correctly guessed
                print(" _ ", end = " ")
        return "\n" 


# game function
def game():
    words = [
        "mop",
        "plastic",
        "cheetos",
        "octopus",
        "bonsai",
        "dinosaur",
        "guitar",
        "python",
    ]
    chosen_word = random.choice(words)

    # creating an instance of the Word class and passing randomized word(chosen_word) to it
    word = Word(chosen_word)

    remaining_guesses = 8
    letters_guessed = []

    # intro to game
    print(
        "\n\nWelcome to Hangman : Python Edition \n\n *** Instructions *** \n\n The rules are simple, try to guess the letters in the mystery word without using up all your lives. If your lives reach 0, GAME OVER. \n\nGood Luck !!\n\n"
    )

    while remaining_guesses > 0:
        word.print_word()
        user_guess = input("\n\nEnter letter here : ").lower()

        # add the users guessed letter to our letters_guessed list
        letters_guessed.append(user_guess)
        print(f"\n\nLetters Guessed : {letters_guessed}\n\n")

        # run the letter guessed through update_dict (if its in our game word it'll update 'guessed': True)
        guessed = word.update_dict(user_guess)
        if guessed:
            print("Yayyy! You guessed a letter!\n\n")

            # check if the user has guessed the full word 
            #  all() returns true if all values are true ... so this will execute if all letters in the word have been guessed and updated to True in update_dict
            if all([letter["guessed"] for letter in word.dict]):
                print("CONGRATS!! YOU GUESSED THE WORD!")

                print("\nWould you like to play again? Y or N")
                user_resp = input("Answer : ").lower()
                if user_resp == "y" or user_resp == "yes":
                    game()
                elif user_resp == "n" or user_resp == "no":
                    print("\n\nThanks for playing! Have a good day!")
                    break
        else:
            remaining_guesses -= 1
            print("No silly goose! Try Again!")
            print(f"Lives : {remaining_guesses}\n\n")

            if remaining_guesses == 0:
                print(f"Game Over! The word was {chosen_word}! \nWould you like to play again? Y or N")
                user_resp = input("Answer : ").lower()
                if user_resp == "y" or user_resp == "yes":
                    game()
                elif user_resp == "n" or user_resp == "no":
                    print("\n\nThanks for playing! Have a good day!")
                    break


game()
