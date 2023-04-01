'Hangman Game'

import random
import os
import time

listOfWords = ["penny", "guitar", "world",
               "space", "python", "megan", "sanders", "love"]


class Hangman:
    'class for hangman game'

    def __init__(self, answer):
        self.playing = True
        self.answer = [*answer.lower()]
        self.board = ["___"] * len(answer)
        self.strikes = 15
        self.guesses = []
        # Print the board each loop

    def print_current_board(self):
        'Print the board each loop'

        print(f'''
Strikes left: {self.strikes}
Previous guesses: {self.guesses}


{self.board}
''')

    def start(self):
        "Game loop"
        while self.playing:
            os.system("clear")
            print('''

            

            
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

''')
            self.print_current_board()
            self.guess()
            self.check_game_status()

    def guess(self):
        'take input for guess and determine result'
        while True:
            guess = input("Guess a letter:  ")
            if guess.isalpha():
                break
            else:
                print("You have to guess a letter!")
            # if guess has been previously guessed
        if guess in self.guesses or guess in self.board:
            print(f'''
            
You already guessed "{guess}"!
''')
            time.sleep(1)
        else:
            # if the new guess is in the word
            if guess in self.answer:
                indexes = []
                for i, char in enumerate(self.answer):
                    if char == guess:
                        indexes.append(i)
                for i in indexes:
                    self.board[i] = guess
            # if it's not in the answer
            else:
                self.guesses.append(guess)
                print(f'''

Sorry, "{guess}" is not in the word!  Try again!       
''')
                time.sleep(1)
                self.strikes -= 1

    def check_game_status(self):
        'check if game is over each loop'
        # if the player runs out of chances
        if self.strikes == 0:
            self.playing = False
            print('''Sorry, you lost!

''')
            self.play_again()

        # if the word is completed
        if "___" not in self.board:
            self.playing = False
            print(f'''

{self.board}

CONGRATS, YOU WON!  THE WORD WAS "{"".join(self.answer)}"

''')
            self.play_again()

    def play_again(self):
        'check if user wants to play again if game ends'
        while True:
            play_again = input("Play again?  ")
            if play_again in ["y", "n"]:
                break
            else:
                print('Please choose "y" or "n"')

        if play_again == "y":
            new_game()
        if play_again == "n":
            raise SystemExit


def new_game():
    'creates a game instance with a new answers and starts it'
    new_word = random.choice(listOfWords)
    game = Hangman(new_word)
    game.start()


new_game()
