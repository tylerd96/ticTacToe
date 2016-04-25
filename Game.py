from tpge import *

X = {-1}
O = {-2}


def game_title():
    """
    Returns the name of the game which is "Tic Tac Toe".
    """
    return "Tic Tac Toe"

def initial_state():


    return (X,O)

def images(S):
    """

    """
    return background()

def background():
    """

    """
    LEFT_VERTICAL = (100,100,100,325)
    RIGHT_VERTICAL = (175,100,175,325)
    TOP_HORIZONTAL = (25,250,250,250)
    BOTTOM_HORIZONTAL = (25,175,250,175)
    return [LEFT_VERTICAL, RIGHT_VERTICAL, TOP_HORIZONTAL, BOTTOM_HORIZONTAL]

def successor_state(S,P):

    return (S,P)

def game_over(S):
    return has_won('x',S) or has_won('o',S)

def has_won(P,S):
    return won_vertically(P,S) or won_horizontally(P,S) or won_diagonally(P,S)

def won_vertically(P,S):
    c = 0 if P == 'x' else 1
    return {0,3,6} <= S[c] or\
           {1,4,7} <= S[c] or\
           {2,5,8} <= S[c]

def won_horizontally(P,S):
    c = 0 if P == 'x' else 1
    return {0,1,2} <= S[c] or\
           {3,4,5} <= S[c] or\
           {6,7,8} <= S[c]

def won_diagonally(P,S):
    c = 0 if P == 'x' else 1
    return {0,4,8} <= S[c] or\
           {2,4,6} <= S[c]



run_game(game_title, initial_state, successor_state, game_over, images)
