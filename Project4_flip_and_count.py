# Mark Calabio 12488362
## This module contains classes responsible for flipping pieces and
## counting pieces

from Project4_GameState import GameState

class Flip():
    def __init__(self, current_turn: str, board: [[int]], valid_direction_list: list,
                 row: int, col: int):
        
        self.current_turn = current_turn
        self.board = board
        self.valid_direction_list = valid_direction_list

        self.current_num = None
        self.opponent_num = None
        
        self.input_row = row - 1
        self.input_column = col - 1

    def assign_current(self) -> int:
        if self.current_turn == 'B':
            self.current_num = 1

        if self.current_turn == 'W':
            self.current_num = 2

        return self.current_num

    def assign_opponent(self) -> int:
        if self.current_turn == 'B':
            self.opponent_num = 2

        if self.current_turn == 'W':
            self.opponent_num = 1

        return self.opponent_num

    def capture_down(self):
        '''All pieces are captured by the current player who is below these captured
        pieces (this is for the UP direction)'''
        for i in range(18):
            if i != 0:
                
                if self.board[self.input_row + i][self.input_column] == self.opponent_num:
                    self.board[self.input_row + i][self.input_column] = self.current_num

                elif self.board[self.input_row + i][self.input_column] == self.current_num:
                    return

    def capture_up(self):
        '''For the DOWN direction'''
        for i in range(18):

            if i != 0:

                if self.board[self.input_row - i][self.input_column] == self.opponent_num:
                    self.board[self.input_row - i][self.input_column] = self.current_num

                elif self.board[self.input_row - i][self.input_column] == self.current_num:
                    return

    def capture_right(self):
        '''For the LEFT direction'''
        
        for i in range(18):
            
            if i != 0:
                
                if self.board[self.input_row][self.input_column + i] == self.opponent_num:
                    self.board[self.input_row][self.input_column + i] = self.current_num

                elif self.board[self.input_row][self.input_column + i] == self.current_num:
                    return

    def capture_left(self):
        '''For the RIGHT direction'''
        for i in range(18):
            
            if i != 0:
                
                if self.board[self.input_row][self.input_column - i] == self.opponent_num:
                    self.board[self.input_row][self.input_column - i] = self.current_num

                elif self.board[self.input_row][self.input_column - i] == self.current_num:
                    return

    def capture_down_right(self):
        '''For the UP_LEFT direction'''
        for i in range(18):

            if i != 0:

                if self.board[self.input_row + i][self.input_column + i] == self.opponent_num:
                    self.board[self.input_row + i][self.input_column + i] = self.current_num

                elif self.board[self.input_row + i][self.input_column + i] == self.current_num:
                    return

    def capture_down_left(self):
        '''For the UP_RIGHT direction'''
        for i in range(18):

            if i != 0:

                if self.board[self.input_row + i][self.input_column - i] == self.opponent_num:
                    self.board[self.input_row + i][self.input_column - i] = self.current_num

                elif self.board[self.input_row + i][self.input_column - i] == self.current_num:
                    return

    def capture_up_right(self):
        '''For the DOWN_LEFT direction'''
        for i in range(18):

            if i != 0:

                if self.board[self.input_row - i][self.input_column + i] == self.opponent_num:
                    self.board[self.input_row - i][self.input_column + i] = self.current_num

                elif self.board[self.input_row - i][self.input_column + i] == self.current_num:
                    return

    def capture_up_left(self):
        '''For the DOWN_RIGHT direction'''
        for i in range(18):

            if i != 0:

                if self.board[self.input_row - i][self.input_column - i] == self.opponent_num:
                    self.board[self.input_row - i][self.input_column - i] = self.current_num

                elif self.board[self.input_row - i][self.input_column - i] == self.current_num:
                    return
                
    def handle_flips(self):
        '''Handles all the captured pieces and functions in the Flip class'''
        self.assign_current()
        self.assign_opponent()

        for direction in self.valid_direction_list:
            
            if direction == 'UP':
                self.capture_down()
            if direction == 'DOWN':
                self.capture_up()
            if direction == 'LEFT':
                self.capture_right()
            if direction == 'RIGHT':
                self.capture_left()
            if direction == 'UP_LEFT':
                self.capture_down_right()
            if direction == 'UP_RIGHT':
                self.capture_down_left()
            if direction == 'DOWN_LEFT':
                self.capture_up_right()
            if direction == 'DOWN_RIGHT':
                self.capture_up_left()

        return self.board
##        
test4 = [[1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
         [2, 0, 2, 0, 2, 2, 0, 2, 2, 0],
         [1, 0, 2, 2, 2, 2, 2, 0, 2, 0],
         [2, 2, 2, 2, 0, 2, 0, 0, 2, 0],
         [2, 2, 0, 2, 1, 2, 0, 0, 2, 0],
         [1, 2, 2, 2, 2, 1, 0, 0, 2, 0],
         [2, 2, 2, 2, 2, 1, 0, 0, 2, 0],
         [2, 0, 1, 0, 0, 2, 0, 0, 2, 0],
         [2, 0, 0, 0, 0, 0, 2, 0, 2, 0],
         [1, 0, 0, 0, 0, 0, 0, 2, 1, 0]]



##########################################################################################
#### This class counts how many pieces each player has, and later determines the #########
#### winner of Othello                                                           #########

### THE BOARD MUST BE COPIED BEFORE THIS CLASS STARTS COUNTING ####

### WIN_WITH_COUNT ONLY OCCURS WHEN THE GAME IS FINISHED

class Count():
    def __init__(self, gs: GameState, winning_method: '> or <'):
        self.board = gs.board
        self.win_method = winning_method

        self.BLACK = 1
        self.WHITE = 2
        self.NONE = 0

        self.any_zeroes = 0
        self.game_over = None
    
        self.black_count = 0
        self.white_count = 0

        self.count_dictionary = {'BLACK': None, 'WHITE': None}
        
    def count(self):
        '''This function counts the number of pieces each player has, and returns
        a dictionary indicating each amount'''
            
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                    
                if self.board[row][col] == self.BLACK:
                    self.black_count += 1
                        
                if self.board[row][col] == self.WHITE:
                    self.white_count += 1
                        
        self.count_dictionary['BLACK'] = self.black_count
        self.count_dictionary['WHITE'] = self.white_count

    def display_dis_count(self):
        '''This function displays the amount of pieces of each player'''
        return('Black: {}  White: {}'.format(self.count_dictionary['BLACK'],
                                    self.count_dictionary['WHITE']))

    def is_game_board_filled(self):
        '''This function determines if the gameboard has no more moves'''

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                    
                if self.board[row][col] == 0:
                    self.any_zeroes += 1

        if self.any_zeroes != 0:
            self.game_over = 'NOT OVER'

        return self.game_over
                    

    def win_with_count(self): ### only used at the END
        '''This function determines the winner by count, and this can only be used at
        the very end of the game, when neither player can make a move'''
        
        if self.count_dictionary['BLACK'] == self.count_dictionary['WHITE']:
            return 'NONE'
        
        else:
        
            if self.win_method == '>': ##most pieces win
                if self.count_dictionary['BLACK'] > self.count_dictionary['WHITE']:
                    return 'BLACK'
                else:
                    return 'WHITE'

            if self.win_method == '<': ##fewest pieces win
                if self.count_dictionary['BLACK'] > self.count_dictionary['WHITE']:
                    return 'WHITE'
                else:
                    return 'BLACK'



        
