#My first Personal Project
#6/30/20,07/01/20, completed on 07/03/20

# The purpose of this project is to start implementing what I've learned.

"""
Build a RPS game that allows the player to play against the computer.
Best would be to learn how to use python GUI to make more interesting.

Would Build functions to seperate my code.
1. Build AI function that selects R, P or S at random
2. Build Score function that keep count of score
3. Build function of game play and its rules (P beats R e.t.c)
4. Ask user for input of their selection and implement error handling
5. See if users selection beats AI selection and save count of who wins.
6. Game last as best of three games
7. Ask User if they would play again
Added on 07/03/20 after getting game to run
8. implement termcolor and color rama
9. implement GUI

Game Rules
R beats S 		P beats R 		S beats P

"""

from random import randint, choice
from colorama import init
from termcolor import colored
from pyfiglet import figlet_format

init()
play_options = ('rock', 'paper', 'scissors')

''' for some reason, its not letting me add doc to my functions so I would write them outside function '''

'''The comp_choice function selects a choice of r,p,s for the computer '''
def comp_choice():

    computer = choice(play_options)
    return computer

'''The user_choice function allows the user to select from the r/p/s options. 
	It also handles error that may arise from user input.'''
def user_choice():
	
    while True:
        try:
            user = input('Choose from rock, paper or scissors'
            	'\nWhat would YOU play: ')
            if user.lower() in play_options:
                return user.lower()
                break
            else:
                print(f'Your entry of {user} is not valid.')
                raise
        except BaseException:
            print(f"Please choose one of {play_options}\n")

'''The game_play function is where the actual game is executed. 
	The function keeps count of and returns the value of the score for both user and computer.'''
def game_play(user, ai):
    user_score = 0
    ai_score = 0
    if (user == 'rock' and ai == 'scissors'
        ) or (user == 'scissors' and ai == 'paper'
              ) or (user == 'paper' and ai == 'rock'):
        user_score = user_score + 1
        ai_score = 0
        print(f'User wins!!!!!!!!!! User chose {user} and Computer chose {ai}')
        return (user_score, ai_score)
    elif (user == ai):
        print(f"It's a tie.. USER chose {user} and COMPUTER chose {ai}\n")
        user_score = 0
        ai_score = 0
        return (user_score, ai_score)
    else:
        print(f'Computer wins!!!!!!! User chose {user} computer chose {ai}')
        user_score = 0
        ai_score = ai_score + 1
        return (user_score, ai_score)

'''The replay function checks to see if the player wants to play again after the game ends.
	figlet_format is used to create the art in the terminal'''
def replay(p1, p2):
    yes = ('yes', 'yea', 'y', 'affirmative', 'yeah','ok','k')
    no = ('no', 'nope', 'n', 'never')
    if p1 > p2:
        print(f'GAME OVER \nFinal score is User: {p1}, Computer: {p2}')
        print(figlet_format('\nUSER WINS!!', font = 'letters'))
    elif p1 == p2:
        print(f'GAME OVER \nFinal score is User: {p1}, Computer: {p2}')
        print(figlet_format("\nIT'S A TIE", font = 'letters'))
    else:
        print(f'GAME OVER \nFinal score is User: {p1} Computer: {p2}')
        print(figlet_format('\nCOMPUTER WINS', font = 'letters'))

    to_replay = input('Would you like to play again: ').lower()
    if to_replay in yes:
        print('\n***NEW GAME***' * 2)
        rounds()

'''The rounds function is the main function. It is the confluence of all other functions
	It uses figlet_format for the ASCII art (Welcome to...) and termcolor to create visaual.
	The for loop allows for the game to have three turns and also counts the number of turns.
	The game_play function returns 2 values which are collected as the user and computer score.
	These are then unpacked from their tuple into the users score and ai score to keep count.
	Finally replay function is called to see if game is to be played again.
	'''
def rounds():
    number_of_turns = (1, 2, 3)
    users_score = 0
    ai_score = 0
    game_start = figlet_format(' WELCOME TO ROCK / PAPER / SCISSORS', font = 'slant')
    print(colored(game_start, color = 'cyan'))
    for i in number_of_turns:
        user_score_count, ai_score_count = game_play(user_choice(), comp_choice())
        user, ai = user_score_count, ai_score_count
        users_score += user
        ai_score += ai
        print(f'user score is {users_score}')
        print(f'comp score is {ai_score}')
        print(f'End of round {i}\n')

    replay(users_score, ai_score)
    return '\nThanks for playing! GOODBYE\n'

print(rounds())
