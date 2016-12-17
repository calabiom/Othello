# Mark Calabio #12488362
## This module implements the game logic necessary for Othello

from Project4_GameState import GameState
from Project4_flip_and_count import Flip
from Project4_flip_and_count import Count

NONE = 0
BLACK = 1
WHITE = 2

################################################################################
## Creates the game board, and does anything relating to the game board ########

def create_board(rows: int, cols: int) -> list:
    larger_list = []

    for row in range(rows):
        larger_list.append([])
        for col in range(cols):
            larger_list[-1].append(0)

    return larger_list

def center(board: list, who_is_top_left: str) -> list:
    '''Sets up the board in the very beginning, with who is on the top left'''
    if who_is_top_left == 'B':
        top_left = int(len(board)/2)
        parts = board[top_left]
        length = int(len(parts)/2)
        
        parts[length - 1] += 2
        parts[length] += 1

        board[top_left - 1][length - 1] += 1
        board[top_left - 1][length] += 2    
     
    if who_is_top_left == 'W':
        top_left = int(len(board)/2)
        parts = board[top_left]
        length = int(len(parts)/2)
        
        parts[length - 1] += 1
        parts[length] += 2

        board[top_left - 1][length - 1] += 2
        board[top_left - 1][length] += 1

    return board

def printb(board: list):
    for rows in range(len(board)):
        print(board[rows])
        
def copy(board: [[int]]) -> list:
    copy_of_board = []

    for cols in range(len(board)):
        copy_of_board.append([])
        for rows in range(len(board[cols])):
            copy_of_board[-1].append(board[cols][rows])

    return copy_of_board


##############################################################################
## The actual functions the game uses (AKA I don't really know where to place#
## them/organize them)                                                  ######

def new_game(board: [[int]], first_move: str) -> GameState:
    '''Returns a GS when a new game starts'''
    return GameState(board, first_move)

def display_turn(current_turn: str) -> str:
    '''Returns a message that specifies whose turn it is'''
    return 'TURN: {}'.format(current_turn)

def _opposite_turn(turn: str):  
    '''This function alternates between players after a move is made
    on the board...OR there are no available moves for a certain player'''
    
    if turn == 'B':
        return 'W'
    else:
        return 'B'

#############################################################################
### These functions check if the player has any moves to play ###############

# PHASE I: "Oh Dear God, Can I Even Attack?"

def check_if_current_player_has_moves(gs: GameState)-> int:
    '''This function returns the opponent\'s turn if the GameState dictionary
    for the current player has no potential moves'''
    
    gs.potential_moves_are()
    
    count = 0
    for a in gs.potential_dict:
        if gs.potential_dict[a] == None:
            count += 1
    return count


def switch_turns(gs: GameState) -> GameState:
    '''This function returns a new GameState when the current player has no
    available moves, and when the game is still going on'''
    copy_of_board = copy(gs.board)
    now_the_opponent_has_a_turn = _opposite_turn(gs.current_turn)

    return GameState(copy_of_board, now_the_opponent_has_a_turn)


################################################################################
### These functions check if the player's input of their move is valid #########
### These functions happen if the player passed through PHASE I        #########

# PHASE II: "Give Me the Chance to Attack, Sir..."

def valid_move_list(row: int, col: int, gs: GameState) -> list:
    '''This function checks if the row and column specified by the user
    is a valid place for the player to place a piece. The function takes
    the row and column numbers and run it through the GameState dictionary,
    and returns a list of directions that reference opponent\'s pieces that
    can be captured'''
    
    directions_list = []
      
    for a in gs.potential_dict:
        if gs.potential_dict[a] == None:
            continue
            
        if (row-1, col-1) in gs.potential_dict[a]: #...row-1, col-1...
            directions_list.append(a)
              
    return directions_list


def is_it_valid(direction_list: list) -> bool:
    '''This function checks if the move is actually valid by checking how
    many elements there are in a list of directions'''
    
    if len(direction_list) > 0:
        return True

 ### ^ if this move is invalid, it should print 'INVALID', and the user interface
 ### should prompt the user again to make another move

######################################################################################
### These functions, after Phase I and Phase II passed successfully, place the #######
### desired piece in the desired spot, and flips the 'captured' pieces ###############

# PHASE III: "The One Who Attacks also Captures"
    
def place_piece(gs: GameState, row: int, col: int) -> [[int]]:
    '''This functions takes the board, and after evaluations from whether or not
    the user\'s input was valid, if it is VALID (TRUE), then the row and column
    specified by the user is placed onto the board'''
    if gs.current_turn == 'B':
        gs.board[row-1][col-1] = 1
    if gs.current_turn == 'W':
        gs.board[row-1][col-1] = 2
        
    return gs.board    

def officially_flip_captured_pieces(game_board: [[int]], gs: GameState,
                                   valid_direction_list: list,
                                   row: int, col: int):
    '''This function uses a class called Flip to flip the opponent's pieces
    after the current player has placed his/her piece'''
    flip = Flip(gs.current_turn, game_board, valid_direction_list, row, col)

    updated_game_board = flip.handle_flips()

    return updated_game_board

def return_fresh_gamestate(gs: GameState) -> GameState:
    '''Returns a new GameState for the next player, after a play has been made'''
    copy_of_played_board = copy(gs.board)
    new_turn = _opposite_turn(gs.current_turn)

    return GameState(copy_of_played_board, new_turn)

    
##############################################################################################
### These functions determine who the winner is by the amount of pieces each player has ######

# PHASE IV: "After All is Said and Done..."

#### Most of these functions are in the Project4_flip_and_count.py under
#### the class, Count.

def winner_message(winner: str) -> str:
    '''Displays who the winner of Othello is'''
    return 'WINNER: {}'.format(winner)

##############################################################################
### The following are exceptions that represent error conditions

class AttemptAfterGameOver(Exception):
    '''Raised when a player attempts to make a move after the game is over'''
    pass

class InvalidMoveError(Exception):
    '''Only raised when an invalid move is made'''
    pass
    
