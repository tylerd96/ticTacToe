from tpge import *
from random import randint
from copy import deepcopy

# By: Tyler Davis and Nikhil Sutliff
# CSE 102 Final Lecture Project

def game_title():
    """
    game_Title : String
    Returns the name of the game which is "Tic Tac Toe".
    """
    return "Tic Tac Toe"

def initial_state():
    """
    initial_state: State
    Returns the initial state of the game.
    S['x'] denotes the cells that
    player x ownes.
    S['o'] denotes the cells that player o ownes.
    S['MODE'] denotes the type of game the player will be playing.
    0 is a two player game, 1 is single player vs a Easy AI, 2 is single player
    vs a medium AI, and 3 is single player vs a Hard AI.
    S['STATE'] denotes the current state of the game. 0 means that the player
    is still selecting the mode of the game. 1 means that the game is currently
    in progress, and 2 means that the game is over and the user is selecting
    whether or not they want to play another game.  3 means that the game is
    over and the program will automatically exit.
    S['MISS'] denotes whether the previous click was an invalid input or not.
    """
    return {'x':set(), 'o':set(), 'MODE':0, 'STATE':0, 'MISS': False}

def images(S):
    """
    images : State -> Image List
    Returns the image list that will be drawn on the screen of the game
    """
    return background() + contents(S)

def background():
    """
    background : Image List
    """
    LEFT_VERTICAL = (100,100,100,325)
    RIGHT_VERTICAL = (175,100,175,325)
    TOP_HORIZONTAL = (25,250,250,250)
    BOTTOM_HORIZONTAL = (25,175,250,175)
    return [LEFT_VERTICAL, RIGHT_VERTICAL, TOP_HORIZONTAL, BOTTOM_HORIZONTAL]

def contents(S):
    """
    contents : State -> Image List
    What gets drawn based on the state of the game
    """
    if S['STATE'] == 0:
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
    if S['STATE'] >= 1:
        c = []
        if(S['x'] >= {0}):
            c.append((50,300, 75,275))
            c.append((50,275,75,300))
        if(S['x'] >= {1}):
            c.append((125,300, 150,275))
            c.append((125,275,150,300))
        if(S['x'] >= {2}):
            c.append((200,300, 225,275))
            c.append((200,275,225,300))
        if(S['x'] >= {3}):
            c.append((50,225,75,200))
            c.append((50,200,75,225))
        if(S['x'] >= {4}):
            c.append((125,225,150,200))
            c.append((125,200,150,225))
        if(S['x'] >= {5}):
            c.append((200,225,225,200))
            c.append((200,200,225,225))
        if(S['x'] >= {6}):
            c.append((50,150,75,125))
            c.append((50,125,75,150))
        if(S['x'] >= {7}):
            c.append((125,150,150,125))
            c.append((125,125,150,150))
        if(S['x'] >= {8}):
            c.append((200,150,225,125))
            c.append((200,125,225,150))
        if(S['o'] >= {0}):
            c.append((62,287,13))
        if(S['o'] >= {1}):
            c.append((137,287,13))
        if(S['o'] >= {2}):
            c.append((213,287,13))
        if(S['o'] >= {3}):
            c.append((62,213,13))
        if(S['o'] >= {4}):
            c.append((137,213,13))
        if(S['o'] >= {5}):
            c.append((213,213,13))
        if(S['o'] >= {6}):
            c.append((62,138,13))
        if(S['o'] >= {7}):
            c.append((137,138,13))
        if(S['o'] >= {8}):
            c.append((213,138,13))
    if(S['STATE'] == 1):
        if(S['MODE'] == 0):
            if(len(S['x'] | S['o'])%2 == 0 and len(S['x'] | S['o'])!=9):
                c.append(('Player X\'s turn',430,320,20))
            else:
                c.append(('Player O\'s turn',430,320,20))
            if(S['MISS']):
                c.append(('Not a valid move',240,460,20))
                S['MISS'] = False
            return c
        if(S['MODE'] > 0):
            if(len(S['x'] | S['o'])%2 ==0 and len(S['x'] | S['o'])!=9):
               c.append(('Player X\'s turn',430,320,20))
            else:
               c.append(('Click anywhere for the computer to make his move',320,430,19))
            if(S['MISS']):
               c.append(('Not a valid move',240,460,20))
               S['MISS'] = False
            return c
        
    if(S['STATE'] == 2):
        c.append(('Play again?',430,250,20))
        c.append((320,230,420,200,GREEN))
        c.append((440,230,540,200,RED))
        c.append(('Yes',370,215,15))
        c.append(('No',490,215,15))
    

        
        if(has_won('x',S)):
            c.append(('Player X has won',430,320,20))
            return c
        if(has_won('o',S)):
            c.append(('Player O has won',430,320,20))
            return c
        else:
            c.append(('The game is a tie',430,320,20))
            return c
        
    else:
        return []

def successor_state(S,P):
    """
    successor_state : State x Point -> State
    """
    # Initial State of the game (Selection Phase)
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
           
    # Game is now under way
    if(S['STATE'] == 1):
        
        # Two player Game
        if(S['MODE'] == 0):
            if(not in_board(P)):
               S['MISS'] = True
            else:
                Cell = get_cell(P)
                if(is_open(Cell,S)):
                    make_move(Cell,S)
                else:
                    S['MISS'] = True
            if(has_won('x',S) or has_won('o',S) or tie(S)):
               S['STATE'] = 2
               
        # Easy AI mode
        if(S['MODE'] == 1):
            if(len(S['x'] | S['o'])%2 == 0):
                if(not in_board(P)):
                   S['MISS'] = True
                else:
                   Cell = get_cell(P)
                   if(is_open(Cell,S)):
                     make_move(Cell,S)
                   else:
                     S['MISS'] = True
            else:
                  Cell = -1
                  while Cell == -1 or not is_open(Cell,S):
                      Cell = randint(0,8)
                         
                  make_move(Cell,S)
            if(has_won('x',S) or has_won('o',S) or tie(S)):
                S['STATE'] = 2
                
        # Medium AI mode
        if(S['MODE'] == 2):
            if(len(S['x'] | S['o'])%2 == 0):
                if(not in_board(P)):
                    S['MISS'] = True
                else:
                    Cell = get_cell(P)
                    if(is_open(Cell,S)):
                       make_move(Cell,S)
                    else:
                        S['MISS'] = True
            else:
                if(about_to_win('x',S)):
                   Cell = get_block('x',S)
                   if(Cell != -1):
                       make_move(Cell,S)
                else:
                    Cell = -1
                    while Cell == -1 or not is_open(Cell,S):
                        Cell = randint(0,8)
                    make_move(Cell,S)
            if(has_won('x',S) or has_won('o',S) or tie(S)):
                S['STATE'] = 2
                
        # Hard AI mode
        if(S['MODE'] ==3):
            if(len(S['x'] | S['o'])%2 ==0):
                if(not in_board(P)):
                    S['MISS'] = True
                else:
                    Cell = get_cell(P)
                    if(is_open(Cell,S)):
                        make_move(Cell,S)
                    else:
                        S['MISS'] = True
            else:
                print(minimax(S))
                print(S)
                make_move(minimax(S),S)
                
            if(has_won('x',S) or has_won('o',S) or tie(S)):
                S['STATE'] = 2
                
    # Game is over asking if you want to play again
    if(S['STATE'] == 2):
        if(in_ngNo(P)):
            S['STATE'] = 3
        if(in_ngYes(P)):
            S['STATE'] = 3
            run_game(game_title, initial_state, successor_state, game_over, images)
        
    return S

def game_over(S):
    """
    game_over : State -> Boolean
    """
    return S['STATE'] >= 3

def has_won(P,S):
    """
    has_won : Player x State -> Boolean
    """
    return won_vertically(P,S) or won_horizontally(P,S) or won_diagonally(P,S)

def won_vertically(P,S):
    """
    won_vertically : Player x State -> Boolean
    """
    return {0,3,6} <= S[P] or\
           {1,4,7} <= S[P] or\
           {2,5,8} <= S[P]

def won_horizontally(P,S):
    """
    won_horizontally : Player x State -> Boolean
    """
    return {0,1,2} <= S[P] or\
           {3,4,5} <= S[P] or\
           {6,7,8} <= S[P]

def won_diagonally(P,S):
    """
    won_diagonally : Player x State -> Boolean
    """
    return {0,4,8} <= S[P] or\
           {2,4,6} <= S[P]
def tie(S):
    """
    tie : State -> Boolean
    """
    return 9 == len(S['x'] | S['o'])

def in_2Player(P):
    """
    in_2Player : Point -> Boolean
    """
    (x,y) = P
    return 380 <= x <= 500 and 285 <= y <= 315

def in_Easy(P):
    """
    in_Easy : Point -> Boolean
    """
    (x,y) = P
    return 380 <= x <= 500 and 245 <= y <= 275

def in_Med(P):
    """
    in_Med : Point -> Boolean
    """
    (x,y) = P
    return 380 <= x <= 500 and 205 <= y <= 235

def in_Hard(P):
    """
    in_Hard : Point -> Boolean
    """
    (x,y) = P
    return 380 <= x <= 500 and 165 <= y <= 195

def in_Start(P):
    """
    in_Start : Point -> Boolean
    """
    (x,y) = P
    return 200 <= x <= 280 and 410 <= y <= 440

def in_board(P):
    """
    in_board : Point -> Boolean
    """
    (x,y) = P
    return 25 <= x <= 250 and 100 <= y <= 325

def get_cell(P):
    """
    get_cell : Point -> Cell
    """
    (x,y) = P
    if(25 <= x <= 100 and 250 <= y <= 325):
        return 0
    if(100 <= x <= 175 and 250 <= y <= 325):
        return 1
    if(175 <= x <= 250 and 250 <= y <= 325):
        return 2
    if(25 <= x <= 100 and 175 <= y <= 250):
        return 3
    if(100 <= x <= 175 and 175 <= y <= 250):
        return 4
    if(175 <= x <= 250 and 175 <= y <= 250):
        return 5
    if(25 <= x <= 100 and 100 <= y <= 175):
        return 6
    if(100 <= x <= 175 and 100 <= y <= 175):
        return 7
    if(175 <= x <= 250 and 100 <= y <= 175):
        return 8
    
def is_open(C,S):
    """
    is_open : Cell x State -> Boolean
    """
    return not {C} <= S['x'] | S['o']

def make_move(C,S):
    """
    make_move : Cell x State
    """
    if(len(S['x'] | S['o'])%2 == 0):
        S['x'].add(C)
    else:
        S['o'].add(C)
        
def in_ngYes(P):
    """
    in_ngYes : Point -> Boolean
    """
    (x,y) = P
    return 320 <= x <=420 and 200 <= y <= 230

def in_ngNo(P):
    """
    in_ngNo : Point -> Boolean
    """
    (x,y) = P
    return 440 <= x <= 540 and 200 <= y <= 230

def about_to_win(P,S):
    """
    about_to_win : Player x State -> Boolean
    """
    return atw_diagonally(P,S) or atw_horizontally(P,S) or\
           atw_vertically(P,S)

def atw_diagonally(P,S):
    """
    atw_diagonally : Player x State -> Boolean
    """
    O = 'o' if P == 'x' else 'x'
    return {0,4} <= S[P] and not {8} <= S[O] or\
           {0,8} <= S[P] and not {4} <= S[O] or\
           {4,8} <= S[P] and not {0} <= S[O] or\
           {6,4} <= S[P] and not {2} <= S[O] or\
           {6,2} <= S[P] and not {4} <= S[O] or\
           {4,2} <= S[P] and not {6} <= S[O]
def atw_horizontally(P,S):
    """
    atw_horizonatlly : Player x State -> Boolean
    """
    O = 'o' if P == 'x' else 'x'
    return {0,1} <= S[P] and not {2} <= S[O] or\
           {0,2} <= S[P] and not {1} <= S[O] or\
           {1,2} <= S[P] and not {0} <= S[O] or\
           {3,4} <= S[P] and not {5} <= S[O] or\
           {3,5} <= S[P] and not {4} <= S[O] or\
           {4,5} <= S[P] and not {3} <= S[O] or\
           {6,7} <= S[P] and not {8} <= S[O] or\
           {6,8} <= S[P] and not {7} <= S[O] or\
           {7,8} <= S[P] and not {6} <= S[O]
def atw_vertically(P,S):
    """
    atw_vertically : Player x State -> Boolean
    """
    O = 'o' if P == 'x' else 'x'
    return {0,3} <= S[P] and not {6} <= S[O] or\
           {0,6} <= S[P] and not {3} <= S[O] or\
           {3,6} <= S[P] and not {0} <= S[O] or\
           {1,4} <= S[P] and not {7} <= S[O] or\
           {1,7} <= S[P] and not {4} <= S[O] or\
           {4,7} <= S[P] and not {1} <= S[O] or\
           {2,5} <= S[P] and not {8} <= S[O] or\
           {2,8} <= S[P] and not {5} <= S[O] or\
           {5,8} <= S[P] and not {2} <= S[O]

def get_block(P,S):
    """
    get_block : Player x State -> Cell
    """
    O = 'o' if P == 'x' else 'x'
    if({0,8} <= S[P] and not {4} <= S[O] or\
       {6,2} <= S[P] and not {4} <= S[O] or\
       {3,5} <= S[P] and not {4} <= S[O] or\
       {1,7} <= S[P] and not {4} <= S[O]):
        return 4
    if({4,8} <= S[P] and not {0} <= S[O] or\
       {1,2} <= S[P] and not {0} <= S[O] or\
       {3,6} <= S[P] and not {0} <= S[O]):
        return 0
    if({6,4} <= S[P] and not {2} <= S[O] or\
       {0,1} <= S[P] and not {2} <= S[O] or\
       {5,8} <= S[P] and not {2} <= S[O]):
        return 2
    if({0,4} <= S[P] and not {8} <= S[O] or\
       {6,7} <= S[P] and not {8} <= S[O] or\
       {2,5} <= S[P] and not {8} <= S[O]):
        return 8
    if({4,2} <= S[P] and not {6} <= S[O] or\
       {7,8} <= S[P] and not {6} <= S[O] or\
       {0,3} <= S[P] and not {6} <= S[O]):
        return 6
    if({0,2} <= S[P] and not {1} <= S[O] or\
       {4,7} <= S[P] and not {1} <= S[O]):
        return 1
    if({4,5} <= S[P] and not {3} <= S[O] or\
       {0,6} <= S[P] and not {3} <= S[O]):
        return 3
    if({3,4} <= S[P] and not {5} <= S[O] or\
       {2,8} <= S[P] and not {5} <= S[O]):
        return 5
    if({6,8} <= S[P] and not {7} <= S[O] or\
       {1,4} <= S[P] and not {7} <= S[O]):
        return 7
    
    return -1

def score(S):
    """
    score : State -> Score
    """
    return -10 if has_won('x',S) else\
           10 if has_won('o',S) else\
           0 

def minimax(S):
    """
    minimax : State -> Cell
    """
    if(has_won('x',S) or has_won('o',S) or tie(S)):
        return score(S)
    
    scores = []
    moves = []
    Z = deepcopy(S)
    for m in possible_moves(S):
        N = successor(m,Z)
        scores.append(minimax(N))
        moves.append(m)
    
    if len(S['x'] | S['o'])%2 != 0:
        max_score = max(scores)
        idx = scores.index(max_score)
        return moves[idx]
    else:
        min_score = min(scores)
        idx = scores.index(min_score)
        return moves[idx]

    
def possible_moves(S):
    """
    possible_moves : State -> Open Cells
    """
    return {0,1,2,3,4,5,6,7,8} - (S['o'] | S['x'])

def successor(C,S):
    """
    successor : Cell x State -> State
    """
    make_move(C,S)
    return S

run_game(game_title, initial_state, successor_state, game_over, images)
