"""
TPGE DEMO - Tiny Python Game Engine Demo

This module defines a very simple interactive game whose purpose
is to demonstrate the use of TPGE to write elementary games.

LICENSE: This is open-source software released under the terms of the
BSD 2-Clause License (http://opensource.org/licenses/BSD-2-Clause).

PLATFORMS: This module assumes that both the Tiny Python Game Engine and
John Zelle's Graphics Library are present.

INSTALLATION: Put this file somewhere where Python can see it. The Tiny
Python Game Engine must also be present.

OVERVIEW: The demo game enables a user to move a blue square from one
box to another by clicking inside the boxes.

The data model used by this game is described as follows: A Cell is either
the integer 1 or 2, denoting the left, or right box respectively. A State
is a pair (C,N) where C is a cell, and N is a natural number in the interval
[0,MAX_TURNS] denoting the number of turns the player has taken.
"""

from tpge import *

MAX_TURNS = 10
LEFT = 1
RIGHT = 2

def game_title():
    """
    game_title : String
    Returns the name of the game which is "TPGE DEMO".
    """
    return "TPGE DEMO"

def initial_state():
    """
    initial_state : State
    Returns the initial state of the game which is the pair
    (LEFT, 0).
    """
    return (LEFT, 0)

def images(S):
    """
    images : State -> Image List
    If S is a State, then images(S) is the list of Images that need to be
    drawn to the screen in order to present the state S to the user. For
    this game the images that need to be drawn are the background and
    the contents of the cells.
    """
    return background() + contents(S)

def background():
    """
    background : Image List
    Returns the Image List needed to display the background for the game.
    """
    LEFT_BORDER = (220, 190, 220, 290)
    RIGHT_BORDER = (420, 190, 420, 290)
    DIVIDER = (320, 190, 320, 290)
    TOP_BORDER = (220, 290, 420, 290)
    BOTTOM_BORDER = (220, 190, 420, 190)
    return [LEFT_BORDER, DIVIDER, RIGHT_BORDER, TOP_BORDER, BOTTOM_BORDER]

def contents(S):
    """
    contents : State -> Image List
    If S is a state, then contents(S) is the list of Images needed to
    draw the contents of the cells in S.
    """
    Cell = S[0]
    if Cell == LEFT:
        return [(230,200,310,280, BLUE)]
    elif Cell == RIGHT:
        return [(330,200,410,280, BLUE)]

def game_over(State):
    """
    game_over : State -> Boolean
    If S is a State, then game_over(S) is True if and only if the maximum
    number of turns has been reached in S.
    """
    return State[1] == MAX_TURNS

def successor_state(S, P):
    """
    successor_state : State x Point -> State
    If S is a state and P is a Point, then successor_state(S,P) is the State
    obtained by clicking on P in S.
    """
    Turn = S[1] + 1
    if in_left_cell(P):
        Cell = LEFT
    elif in_right_cell(P):
        Cell = RIGHT
    else:
        Cell = S[0]
    return (Cell,Turn)

def in_left_cell(P):
    """
    in_left_cell : Point -> Boolean
    If P is a point, then in_left_cell(P) is True if and only if P
    is within the left cell.
    """
    (X,Y) = P
    return 220 <= X <= 320 and 190 <= Y <= 290

def in_right_cell(P):
    """
    in_right_cell : Point -> Boolean
    If P is a point, then in_right_cell(P) is True if and only if P
    is within the right cell.
    """
    (X,Y) = P
    return 320 <= X <= 420 and 190 <= Y <= 290

if __name__ == "__main__":
    run_game(game_title, initial_state, successor_state, game_over, images)
