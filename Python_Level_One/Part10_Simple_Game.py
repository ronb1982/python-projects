###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
# import random
# digits = list(range(10))
# random.shuffle(digits)
# print(digits[:3])
# 
# # Another hint:
# guess = input("What is your guess? ")
# print(guess)

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
def print_intro():
    print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")

def run_game():
    guess = input("What is your guess? ")
    correctGuesses = check_guess(guess, randomNumArr)
    matchType = get_match_type_by_result(correctGuesses)
    display_result(matchType)
    return matchType
        
def generate_random_number():
    nums = list(range(9))
    random.shuffle(nums)
    return nums[:3]
    
def check_guess(guess, randomNumArr):
    matchType = ''
    correctGuesses = 0
    
    if len(guess) < 3:
        print("Please enter a 3 digit number.")
    else:
        for i, numAsString in enumerate(guess):
            if int(numAsString) == randomNumArr[i]:
                correctGuesses += 1
            elif int(guess[i]) in randomNumArr:
                correctGuesses = 1
                break
                
    return correctGuesses

def get_match_type_by_result(correctGuesses):
    matchType = ''
    if correctGuesses == 3:
        matchType = 'Match'
    elif correctGuesses >= 1 and correctGuesses <= 2:
        matchType = 'Close'
    else:
        matchType = 'Nope'
    
    return matchType


def display_result(matchType):
    print("{}!".format(matchType))
    
def is_game_over(result):
    endGame = False
    if result.capitalize() == 'Match':
        print("You win!")
        endGame = True
    else:
        print("\n=====================\n")
    
    return endGame
    
import random
print_intro()
randomNumArr = generate_random_number()
print(randomNumArr)
gameOver = False
numCorrectGuesses = 0
print("Code has been generated, please guess a 3 digit number")
while not gameOver:
    result = run_game()
    gameOver = is_game_over(result)