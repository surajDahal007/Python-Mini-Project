# ROCK-PAPER-SCISSOR GAME
# developed by surajDahal007
# Github : 
import random


def play():

    user = input("CHOOSE? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    print("Computer : "+computer)

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'


def is_win(player, opp):

    if (player == 'r' and opp == 's') or (player == 's' and opp == 'p') or (player == 'p' and opp == 'r'):
        return True


print(play())
