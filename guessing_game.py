import random
# add __init__ attribute with a number given as input
# define a method called guess that takes a number and compares it with self.input. It should return "low" if the guessed number is lower, "high" if it's higher or "correct" if it's equal. 
# it also needs to store the last result of the guessing game
# and last another method called solved that returns True if the last if the last guess was correct or False if it wasn't

class GuessingGame:
    def __init__(self,num,solvedinit=False):
        self.number = int(num)
        self.issolved = solvedinit

    def guess(self,guess_num):
        guess_num = int(guess_num)
        if guess_num > self.number:
            self.issolved = False
            return "high"
        elif guess_num < self.number:
            self.issolved = False
            return "low"
        else:
            self.issolved = True
            return "correct"

    def solved(self):
        
        return self.issolved


game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None


while game.solved() == False:
  if last_guess != None: 
    print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    print("")

  last_guess  = input("Enter your guess: ")
  last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")