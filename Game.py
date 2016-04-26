from tpge import *

GAME_START = False
GAME_MODE = 0


def game_title():
    """
    Returns the name of the game which is "Tic Tac Toe".
    """
    return "Tic Tac Toe"

def initial_state():
    """
    Returns the initial state of the game.
    S['x'] denotes the cells that
    player x ownes.
    S['o'] denotes the cells that player o ownes.
    S['MODE'] denotes the type of game the player will be playing.
    0 is a two player game, 1 is single player vs a Easy AI, 2 is single player
    vs a medium AI, and 3 is single player vs a Hard AI.
    S['STATE'] denotes the current state of the game. 0 means that the player
    is still selecting the mode of the game. 1 means that the game is currently
    in progress, and 2 means that the game is over.
    S['MISS'] denotes whether the previous click was an invalid input or not.
    """
    return {'x':set(),'o':set(), 'MODE':0, 'STATE':0, 'MISS': False}

def images(S):
    """
    Returns the image list that will be drawn on the screen of the game
    """
    return background() + contents(S)

def background():
    """
    Cell 0 X = (50,300, 75,275),(50,275,75,300)
    Cell 0 O = (62,287,13)
    Cell 1 X = (125,300, 150,275),(125,275,150,300)
    Cell 1 O = (137,287,13)
    Cell 2 X = (200,300, 225,275),(200,275,225,300)
    Cell 2 O = (213,287,13)
    Cell 3 X = (50,225,75,200),(50,200,75,225)
    Cell 3 O = (62,213,13)
    Cell 4 X = (125,225,150,200),(125,200,150,225)
    Cell 4 O = (137,213,13)
    Cell 5 X = (200,225,225,200),(200,200,225,225)
    Cell 5 O = (213,213,13)
    Cell 6 X = (50,150,75,125),(50,125,75,150)
    Cell 6 O = (62,138,13)
    Cell 7 X = (125,150,150,125),(125,125,150,150)
    Cell 7 O = (137,138,13)
    Cell 8 X = (200,150,225,125),(200,125,225,150)
    Cell 8 O = (213,138,13)
    """
    LEFT_VERTICAL = (100,100,100,325)
    RIGHT_VERTICAL = (175,100,175,325)
    TOP_HORIZONTAL = (25,250,250,250)
    BOTTOM_HORIZONTAL = (25,175,250,175)
    return [LEFT_VERTICAL, RIGHT_VERTICAL, TOP_HORIZONTAL, BOTTOM_HORIZONTAL]

def contents(S):
    """
    What gets drawn based on the state of the game
    """
    if S['STATE'] == False:
        A = [('Press to start the game',240,460,20),(200,440,280,410,YELLOW),\
             ('START', 240, 425, 15), ('Select the game mode:', 440, 345,20)]
        if S['MODE'] == 0:
            return A + [(380,315,500,285,GREEN),('Two Player',440,300,13),\
                     (380,275,500,245,RED), ('VS. Easy AI', 440,260,13),\
                     (380,235,500,205,RED), ('VS. Medium AI', 440,220,13),\
                     (380,195,500,165,RED), ('VS. Hard AI', 440,180,13)]
        if S['MODE'] == 1:
            return A + [(380,315,500,285,RED),('Two Player',440,300,13),\
                     (380,275,500,245,GREEN), ('VS. Easy AI', 440,260,13),\
                     (380,235,500,205,RED), ('VS. Medium AI', 440,220,13),\
                     (380,195,500,165,RED), ('VS. Hard AI', 440,180,13)]
        if S['MODE'] == 2:
            return A + [(380,315,500,285,RED),('Two Player',440,300,13),\
                     (380,275,500,245,RED), ('VS. Easy AI', 440,260,13),\
                     (380,235,500,205,GREEN), ('VS. Medium AI', 440,220,13),\
                     (380,195,500,165,RED), ('VS. Hard AI', 440,180,13)]
        if S['MODE'] == 3:
            return A + [(380,315,500,285,RED),('Two Player',440,300,13),\
                     (380,275,500,245,RED), ('VS. Easy AI', 440,260,13),\
                     (380,235,500,205,RED), ('VS. Medium AI', 440,220,13),\
                     (380,195,500,165,GREEN), ('VS. Hard AI', 440,180,13)]

        
    else:
        return []

def successor_state(S,P):
    if(S['STATE'] == 0):
       if(in_2Player(P)):
           S['MODE'] = 0
       if(in_Easy(P)):
            S['MODE'] = 1
       if(in_Med(P)):
            S['MODE'] = 2
       if(in_Hard(P)):
            S['MODE'] = 3
       if(in_Start(P)):
           S['STATE'] = 1
    else:
        print('hello')
    return S

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
def tie(S):
    return 9 == len(S['x'] | S['o'])

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
def in_Start(P):
    (x,y) = P
    return 200 <= x <= 280 and 410 <= y <= 440

run_game(game_title, initial_state, successor_state, game_over, images)
