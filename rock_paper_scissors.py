#a rock paper scissors game with a computer 

import random

def play():
    user = input("what's your choice 'r'--rock, 'p'--paper, 's'--scissors: ")
    computer= random.choice(['r', 'p', 's'])
    
    if user == computer :
        return "it's a tie"
    
    if u_win(user,computer):
        return 'You won! :)'
    return 'You lost... :('
    
    #r>s, s>p, p>r
def u_win(player , opponent):
    #r>s, s>p, p>r (this is the order of the game rock > scissors and so on...)
    #returns true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player =='p' and opponent =='r'):
        return True
    
print(play())