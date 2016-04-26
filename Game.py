from tpge import *

GAME_START = False
GAME_MODE = 0


def game_title():
    """
    Returns the name of the game which is "Tic Tac Toe".
    """
    return "Tic Tac Toe"

def initial_state():


    return {'x':set(),'o':set(), 'MODE':GAME_MODE, 'START':GAME_START}

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
    if GAME_START == False:
        A = [('Press to start the game',240,460,20),(200,440,280,410,YELLOW),\
             ('START', 240, 425, 15), ('Select the game mode:', 440, 345,20)]
        if GAME_MODE == 0:
            return A + [(380,315,500,285,GREEN),('Two Player',440,300,13),\
                     (380,275,500,245,RED), ('VS. Easy AI', 440,260,13),\
                     (380,235,500,205,RED), ('VS. Medium AI', 440,220,13),\
                     (380,195,500,165,RED), ('VS. Hard AI', 440,180,13)]
        if GAME_MODE == 1:
            return A + [(380,315,500,285,RED),('Two Player',440,300,13),\
                     (380,275,500,245,GREEN), ('VS. Easy AI', 440,260,13),\
                     (380,235,500,205,RED), ('VS. Medium AI', 440,220,13),\
                     (380,195,500,165,RED), ('VS. Hard AI', 440,180,13)]
        if GAME_MODE == 2:
            return A + [(380,315,500,285,RED),('Two Player',440,300,13),\
                     (380,275,500,245,RED), ('VS. Easy AI', 440,260,13),\
                     (380,235,500,205,GREEN), ('VS. Medium AI', 440,220,13),\
                     (380,195,500,165,RED), ('VS. Hard AI', 440,180,13)]
        if GAME_MODE == 3:
            return A + [(380,315,500,285,RED),('Two Player',440,300,13),\
                     (380,275,500,245,RED), ('VS. Easy AI', 440,260,13),\
                     (380,235,500,205,RED), ('VS. Medium AI', 440,220,13),\
                     (380,195,500,165,GREEN), ('VS. Hard AI', 440,180,13)]

        
    else:
        return []

def successor_state(S,P):
    if(not GAME_START):
       if(in_2Player(P)):
           GAME_MODE = 0
       if(in_Easy(P)):
            GAME_MODE = 1
       if(in_Med(P)):
            GAME_MODE = 2
       if(in_Hard(P)):
            GAME_MODE = 3
       print(S)
    else:
        print('hello')
    return (S,P)

def game_over(S):
    return has_won('x',S) or has_won('o',S)

def has_won(P,S):
    """won_vertically(P,S) or won_horizontally(P,S) or won_diagonally(P,S)"""
    return False

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

def in_2Player(P):
    (x,y) = P
    return 380 <= x <= 500 and 285 <= y <= 315

def in_Easy(P):
    (x,y) = P
    return 380 <= x <= 500 and 245 <= y <= 275

def in_Med(P):
    (x,y) = P
    return 380 <= x <= 500 and 205 <= y <= 235

def in_Hard(P):
    (x,y) = P
    return 380 <= x <= 500 and 165 <= y <= 195


run_game(game_title, initial_state, successor_state, game_over, images)
