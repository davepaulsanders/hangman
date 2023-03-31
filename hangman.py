import random
import os
import time
listOfWords = ["penny", "guitar", "world", "space", "python", "megan", "sanders", "love"]

class Hangman:

    def __init__(self, answer):
        self.playing = True
        self.answer = [*answer.lower()]
        self.board = ["___"] * len(answer)
        self.strikes = 15
        self.guesses = []
    
    # Print the board each loop
    def printCurrentBoard(self):

        print(f'''
Strikes left: {self.strikes}
Previous guesses: {self.guesses}


{self.board}
''')
    
    # Game loop
    def start(self):
        while self.playing == True:
            os.system("clear")
            print('''

            

            
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

''')
            self.printCurrentBoard()
            self.guess()
            self.checkGameStatus()

    # take input for guess and determine result     
    def guess(self):
        while True:
            guess = input("Guess a letter:  ")
            if guess.isalpha():
                break
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

    # check if game is over each loop
    def checkGameStatus(self):
        
        # if the player runs out of chances
        if self.strikes == 0:
            self.playing = False
            print('''Sorry, you lost!

''')
            self.playAgain()
        
        # if the word is completed
        if "___" not in self.board:
            self.playing = False
            print(f'''

{self.board}

CONGRATS, YOU WON!  THE WORD WAS "{"".join(self.answer)}"

''') 
            self.playAgain()
            
    # check if user wants to play again if game ends
    def playAgain(self):
        playAgain = input("Play again?  ")

        if playAgain != "y" or playAgain != "n":
            print('''
            
Please type "y" or "n"!

''')
            self.playAgain()
        else:
            if playAgain == "y":
                newGame()
            if playAgain == "n":
                raise SystemExit

# creates a game instance with a new answers and starts it
def newGame():
    newWord = random.choice(listOfWords)
    game = Hangman(newWord)
    game.start()

newGame()


