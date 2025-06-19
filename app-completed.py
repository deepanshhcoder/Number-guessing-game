## Guess the number

# imported the libraries
from art import logo # comment this out
# import art 
# from file name import function/variable
from random import randint


# logo = r"""
#    ______                                         _     __                                                    __                         
#  .' ___  |                                       / |_  [  |                                                  [  |                        
# / .'   \_|   __   _    .---.   .--.    .--.     `| |-'  | |--.    .---.     _ .--.    __   _    _ .--..--.    | |.--.    .---.   _ .--.  
# | |   ____  [  | | |  / /__\\ ( (`\]  ( (`\]     | |    | .-. |  / /__\\   [ `.-. |  [  | | |  [ `.-. .-. |   | '/'`\ \ / /__\\ [ `/'`\] 
# \ `.___]  |  | \_/ |, | \__.,  `'.'.   `'.'.     | |,   | | | |  | \__.,    | | | |   | \_/ |,  | | | | | |   |  \__/ | | \__.,  | |     
#  `._____.'   '.__.'_/  '.__.' [\__) ) [\__) )    \__/  [___]|__]  '.__.'   [___||__]  '.__.'_/ [___||__||__] [__;.__.'   '.__.' [___]    
                                                                                                                                         

# """


# set the level of the game
EASY_LEVEL=10
HARD_LEVEL=5

# function to check answer
def check_answer(guess,answer,no_of_attempts): # 45, 73 , 10 
   if guess>answer: # 90>73
      print("The number you've guessed is too high!")
      return no_of_attempts-1 # 9
   elif guess<answer: # 45<73
      print("The number you've guessed is too low!")
      return no_of_attempts-1
   else: #73==73
      print("Hurray! you've guessed  it right . You won the game!!!!!!!!! ")


# set the difficulty
def set_difficulty():
   level=input("Choose the level of the game: Type 'easy' or 'hard': ") # EASY, Easy. EaSY
   if level=="easy":
      return EASY_LEVEL # 10
   else:
      return HARD_LEVEL # 5



    
## game
def game():
   print(logo) 
   print("Welcome to the number guessing game!")
   # system willl think of a number
   print("I'm thinking if a number between 1 and 100")
   answer=randint(1, 100) # 73 python app.py # actual answer 
   no_of_attempts=set_difficulty() # 10
   guess=0 
   while guess!=answer: # guess=45, answer=73 # true, 
      print(f"You have {no_of_attempts} no of attempts remaining to guess the right number.") # 9 
      guess=int(input("Guess a number: "))  # 45 
      no_of_attempts=check_answer(guess, answer, no_of_attempts) # 9 ......0 
      if no_of_attempts==0:
         print("You've lost the GAME!!!!!!!")
         print(f"Just in case you want to know the right answer it is {answer}!!")
         return
      elif guess!=answer: 
         print("Guess again!!!")

# print(check_answer())

game()





