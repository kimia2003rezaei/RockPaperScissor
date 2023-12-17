import random
import sys
import time
import os


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


rock = '''
      ROCK!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     PAPER!
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    SCISSORS!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
logo = '''

    ____             __   ____                        _____      _                          
   / __ \____  _____/ /__/ __ \____ _____  ___  _____/ ___/_____(_)_____________  __________
  / /_/ / __ \/ ___/ //_/ /_/ / __ `/ __ \/ _ \/ ___/\__ \/ ___/ / ___/ ___/ __ \/ ___/ ___/
 / _, _/ /_/ / /__/ ,< / ____/ /_/ / /_/ /  __/ /   ___/ / /__/ (__  |__  ) /_/ / /  (__  ) 
/_/ |_|\____/\___/_/|_/_/    \__,_/ .___/\___/_/   /____/\___/_/____/____/\____/_/  /____/  
                                 /_/                                                        

'''

moves = [rock, paper, scissors]
clear = lambda: os.system('cls')
print(logo)
print_slow("Hello, welcome to RockPaperScissors!\n")
while True:
    try:
        players_move = int(input("\nWhat do you choose? Type 0 for rock, 1 for paper and 2 for scissors.\n"))
        oh = moves[players_move]
        clear()
        print(logo)
    except ValueError:
        print_slow("Please only enter 0, 1 or 2\n")
        continue
    except IndexError:
        print_slow("Please only enter 0, 1 or 2\n")
        continue
    print_slow("ROCK, PAPER, SCISSORS!\n.\n.\n.\n")
    print_slow("You chose: ")
    print(moves[players_move])
    computers_move = random.randint(0, 2)
    print_slow("Computer chose: ")
    print(moves[computers_move])
    if players_move == 0 and computers_move == 2:
        print_slow("You win!\n")
    elif players_move == 2 and computers_move == 0:
        print_slow("You lose.\n")
    elif players_move > computers_move:
        print_slow("You win!\n")
    elif players_move < computers_move:
        print_slow("You lose.\n")
    else:
        print_slow("It's a draw.\n")