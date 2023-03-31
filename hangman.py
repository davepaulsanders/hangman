import random
import os

listOfWords = ["penny", "guitar", "world", "space", "python", "megan", "sanders", "love"]

class Hangman:

    def __init__(self, answer):
        self.playing = True
        self.answer = [*answer.lower()]
        self.board = ["___"] * len(answer)
        self.strikes = 15
        self.guesses = []

    def printCurrentBoard(self):

        print(f'''
Strikes left: {self.strikes}
Previous guesses: {self.guesses}


{self.board}
''')
    
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
            
    def guess(self):
        guess = input("Guess a letter:  ")
        if guess in self.guesses:
            print(f'''
            
You already guessed "{guess}"!
''')
        else:
            if guess in self.answer:
                indexes = []
                for i, char in enumerate(self.answer):
                    if char == guess:
                        indexes.append(i)
                for i in indexes:
                    self.board[i] = guess
            else:
                self.guesses.append(guess)
                print(f'''

Sorry, "{guess}" is not in the word!  Try again!       
''')
            self.strikes -= 1

    def checkGameStatus(self):
        if self.strikes == 0:
            self.playing = False
            print("Sorry, you lost!")
            self.playAgain()

        if "___" not in self.board:
            self.playing = False
            print(f'''

{self.board}

CONGRATS, YOU WON!  THE WORD WAS "{"".join(self.answer)}"

''') 
            self.playAgain()
            
    def playAgain(self):
        
        playAgain = input("Play again?  ")
        while (playAgain != "y" or playAgain != "n"):
            if playAgain == "y":
                newGame()
            if playAgain == "n":
                raise SystemExit

def newGame():
    newWord = random.choice(listOfWords)
    game = Hangman(newWord)
    game.start()

newGame()


