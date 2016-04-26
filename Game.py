from tpge import *

GAME_START = False
GAME_MODE = 0


def game_title():
    """
    Returns the name of the game which is "Tic Tac Toe".
    """
    return "Tic Tac Toe"

def initial_state():


    return {'x':{0,3},'o':set(), 'MODE':GAME_MODE, 'START':GAME_START}

def images(S):
    """

    """
    return background() + contents(S)

def background():
    """

    """
    LEFT_VERTICAL = (100,100,100,325)
    RIGHT_VERTICAL = (175,100,175,325)
    TOP_HORIZONTAL = (25,250,250,250)
    BOTTOM_HORIZONTAL = (25,175,250,175)
    return [LEFT_VERTICAL, RIGHT_VERTICAL, TOP_HORIZONTAL, BOTTOM_HORIZONTAL]

def contents(S):
    """

    """
    if S['START'] == False:
        return [('Press to start the game',140,460,14),(180,440,100,410,GREEN),\
                ('START', 140, 425, 10)]
    else:
        return []

def successor_state(S,P):
    return (S,P)

def game_over(S):
    return has_won('x',S) or has_won('o',S)

def has_won(P,S):
    return won_vertically(P,S) or won_horizontally(P,S) or won_diagonally(P,S)

def won_vertically(P,S):
    return {0,3,6} <= S[P] or\
           {1,4,7} <= S[P] or\
           {2,5,8} <= S[P]

def won_horizontally(P,S):
    return {0,1,2} <= S[P] or\
           {3,4,5} <= S[P] or\
           {6,7,8} <= S[P]

def won_diagonally(P,S):
    return {0,4,8} <= S[P] or\
           {2,4,6} <= S[P]



run_game(game_title, initial_state, successor_state, game_over, images)
