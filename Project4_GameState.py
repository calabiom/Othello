# Mark Calabio 12488362
## This module creates the class, GameState, which mainly produces a dictionary
## of all the potential locations a player can place a piece.

NONE = 0
BLACK = 1
WHITE = 2

class GameState():
    def __init__(self, board: [[int]], current_turn: 'B or W'):
        self.board = board
        
        self.NONE = 0
        self.BLACK = 1
        self.WHITE = 2
        
        self.current_turn = current_turn
        self.current_num = None             # a number assigned to current turn
        self.opponent_num = None            # number assigned to opposite turn

        self.location = []                  # location of all the current player's pieces
                                            # on the board
                                            
                                            
        self.potential_dict = {"UP": None, "DOWN": None, "LEFT": None, "RIGHT": None,
                               "UP_RIGHT": None, "UP_LEFT": None, "DOWN_RIGHT": None,
                               "DOWN_LEFT": None}
        
        ## the following are lists that contain all potential moves for the
        ## current player
        
        self.valid_up = []
        self.valid_down = []
        self.valid_left = []
        self.valid_right = []
        self.valid_up_right = []
        self.valid_up_left = []
        self.valid_down_right = []
        self.valid_down_left = []


    def assign_current(self) -> int:
        '''Assigns a number to the current player for classication purposes'''
        
        if self.current_turn == 'B':
            self.current_num = 1

        if self.current_turn == 'W':
            self.current_num = 2

        return self.current_num

    def assign_opponent(self) -> int:
        '''Assigns a number to the opponent for classification purposes'''
        if self.current_turn == 'B':
            self.opponent_num = 2
            
        if self.current_turn == 'W':
            self.opponent_num = 1
            
        return self.opponent_num
    
    def location_of_current(self):
        '''Returns a list of coordinates of all the pieces of
        the current player'''
        
        if self.current_turn == 'B':
            for row in range(len(self.board)):
                for col in range(len(self.board[row])):
                    if self.board[row][col] == self.BLACK:
                        self.location.append((row, col))

        if self.current_turn == 'W':
            for row in range(len(self.board)):
                for col in range(len(self.board[row])):
                    if self.board[row][col] == self.WHITE:
                        self.location.append((row, col))

        return self.location

####### The following functions cover all eight directions and checks for
####### all potential locations of the current player's future move/piece
####### This covers: up, down, left, right, diagonal left-down, diagonal
####### right-down, diagonal right-up, and diagonal left-up

    def up(self):
        '''Checks for all the potential places the current player can move,
           each piece going in the upward direction'''
        
        for x,y in self.location:
            for i in range(x+1):
                if i != 0:
                    
                    if self.board[x-i][y] == self.current_num:
                        break  

                    if self.board[x-i][y] == 0:
                        break
                        
                    if self.board[x-i][y] == self.opponent_num:
                        
                        for num in range((x-i) + 1):
                            if self.board[(x-i)-num][y] == self.current_num:
                                break
                            elif self.board[(x-i)-num][y] == 0:
                                self.valid_up.append(((x-i)-num, y))
                                break
                            
        if len(self.valid_up) != 0:
            self.potential_dict["UP"] = self.valid_up

    def down(self):
        '''Checks for all the potential places the current player can move,
           each piece going in the downward direction'''
        
        for x,y in self.location:
            for i in range((len(self.board)-x)):
                if i != 0: 

                    if self.board[x+i][y] == self.current_num:
                        break
                    
                    if self.board[x+i][y] == 0:
                        break

                    if self.board[x+i][y] == self.opponent_num:
                        
                        for num in range((len(self.board)-x) -1):
                            if num+i+x <= (len(self.board)-1):
                                if self.board[x+i+num][y] == self.current_num:
                                    break
                                
                                elif self.board[x+i+num][y] == 0:
                                    self.valid_down.append((x+i+num, y))
                                    break
                                
        if len(self.valid_down) != 0:
            self.potential_dict["DOWN"] = self.valid_down                        # break?
                        

    def left(self):
        '''Checks for all the potential places the current player can move,
           each piece going in the leftward direction'''
        
        for x, y in self.location:
            for i in range(y+1):
                if i != 0: 
                    if self.board[x][y-i] == self.current_num:
                        break

                    if self.board[x][y-i] == 0:
                        break

                    if self.board[x][y-i] == self.opponent_num:
                        
                        for num in range((y-i) + 1):
                            if self.board[x][(y-i)-num] == self.current_num:
                                break
                            elif self.board[x][(y-i)-num] == 0:
                                self.valid_left.append((x,(y-i-num)))
                                break
                            
        if len(self.valid_left) != 0:
            self.potential_dict["LEFT"] = self.valid_left

    def right(self):
        '''Checks for all the potential places the current player can move,
           each piece going in the rightward direction'''
        
        for x, y in self.location:
            for i in range((len(self.board[x])-y)):
                if i != 0: 
                    if self.board[x][y+i] == self.current_num:
                        break

                    if self.board[x][y+i] ==0:
                        break    

                    if self.board[x][y+i] == self.opponent_num:

                        for num in range((len(self.board[x])-y) - 1):
                            if num+i+y <= (len(self.board[x])-1):

                                if self.board[x][(y+i)+num] == self.current_num:
                                    break
                                elif self.board[x][(y+i)+num] == 0:

                                    self.valid_right.append((x,(y+i+num)))
                                    break
                                
        if len(self.valid_right) != 0:
            self.potential_dict["RIGHT"] = self.valid_right

    def _is_up_left_invalid(self, x, y): ## only serves self.up_left()
        '''Returns True if either coordinate has a zero in it. This function
        serves to only the self.up_left function'''
        if x == 0 or y == 0:
            return True

    
    def up_left(self):
        '''Checks for all the potential places the current player can move,
           each piece going in the leftward-diagonal direction'''
        
        for x, y in self.location:
            if not self._is_up_left_invalid(x,y):
            
                for i in range(2):
                    if i != 0:
                        
                        if self.board[x-i][y-i] == self.current_num:
                            break

                        if self.board[x-i][y-i] == 0:
                            break

                        if self.board[x-i][y-i] == self.opponent_num:
                                                
                            for num in range(x+1):
                                if self.board[x-i-num][y-i-num] == self.current_num:
                                    break

                                if self.board[x-i-num][y-i-num] == self.opponent_num:
                                    if self._is_up_left_invalid(x-i-num,y-i-num):
                                        break
                                           
                                elif self.board[x-i-num][y-i-num] == 0:
                                    self.valid_up_left.append((x-i-num,(y-i-num)))
                                    break
                                    
        if len(self.valid_up_left) != 0:
            self.potential_dict["UP_LEFT"] = self.valid_up_left

    def _is_up_right_invalid(self, x, y): # only serves self.up_right()
        '''Returns True if either coordinate has a zero in it. This function
        serves to only the self.up_left function'''
        if x == 0 or y == (len(self.board[x]) -1):
            return True
                        
    
    def up_right(self):
        '''Checks for all the potential places the current player can move,
           each piece going in the rightward-diagonal direction'''
        
        for x, y in self.location: 
            if not self._is_up_right_invalid(x,y):
                
                for i in range(2):
                    if i != 0:
                        
                        if self.board[x-i][y+i] == self.current_num:
                            break

                        if self.board[x-i][y+i] == 0:
                            break    

                        if self.board[x-i][y+i] == self.opponent_num:
                            for num in range(x+1):
 
                                if self.board[x-i-num][y+i+num] == self.current_num:
                                    break

                                if self.board[x-i-num][y+i+num] == self.opponent_num:
                                    if self._is_up_right_invalid(x-i-num, y+i+num):
                                        break
                                                       
                                elif self.board[x-i-num][y+i+num] == 0:
                                    self.valid_up_right.append((x-i-num, y+i+num))
                                    break
                                
            if len(self.valid_up_right) != 0:
                self.potential_dict["UP_RIGHT"] = self.valid_up_right

    def _is_down_left_invalid(self, x, y)-> bool: # only serves self.down_left
        '''Returns True if either coordinate has a zero in it. This function
        serves to only the self.up_left function'''
        if x == (len(self.board)-1) or y == 0:
            return True
                        
    
    def down_left(self):
        '''Checks for all the potential places the current player can move,
           each piece going in the down-leftward-diagonal direction'''
        
        for x,y in self.location: #len(self.board[x])-x
            if not self._is_down_left_invalid(x,y):
                for i in range(2):
                    if i != 0:
                        
                        if self.board[x+i][y-i] == self.current_num:
                            break
                        if self.board[x+i][y-i] == 0:
                            break
                        if self.board[x+i][y-i] == self.opponent_num:

                            for num in range(len(self.board)-x):

                                if self.board[x+i+num][y-i-num] == self.current_num:
                                    break

                                if self.board[x+i+num][y-i-num] == self.opponent_num:
                                    if self._is_down_left_invalid(x+i+num,y-i-num):
                                        break
                                    
                                if self.board[x+i+num][y-i-num] == 0:
                                    self.valid_down_left.append((x+i+num, y-i-num))
                                    break

        if len(self.valid_down_left) != 0:
            self.potential_dict["DOWN_LEFT"] = self.valid_down_left

    def _is_down_right_invalid(self, x,y) -> bool:
        '''Returns True if either coordinate has a zero in it. This function
        serves to only the self.down_right function'''
        if x == (len(self.board)-1) or y == (len(self.board[x])-1):
            return True
        
    
    def down_right(self):
        '''Checks for all the potential places the current player can move,
           each piece going in the down-rightward-diagonal direction'''
        
        for x, y in self.location: #len(self.board[x])-(x+y)
            if not self._is_down_right_invalid(x,y):
                for i in range(2):
                    if i != 0:

                        if self.board[x+i][y+i] == self.current_num:
                            break
                        
                        if self.board[x+i][y+i] == 0:
                            break
                        
                        if self.board[x+i][y+i] == self.opponent_num:
                            
                            for num in range(len(self.board)-x):
                                
                                if self.board[x+i+num][y+i+num] == self.current_num:
                                    break
                                    
                                if self.board[x+i+num][y+i+num] == self.opponent_num:
                                    if self._is_down_right_invalid(x+i+num, y+i+num):
                                        break
                                        
                                elif self.board[x+i+num][y+i+num] == 0:
                                    self.valid_down_right.append((x+i+num, y+i+num))
                                    break
                                    
        if len(self.valid_down_right) != 0:
            self.potential_dict["DOWN_RIGHT"] = self.valid_down_right

    def potential_moves_are(self) -> dict:
        '''This function goes through all eight directions for each piece for
        the current player, and returns a dictionary specifying which location
        and direction the pieces can be placed'''

        self.assign_current()
        self.assign_opponent()
        self.location_of_current()
        
        self.up()
        self.down()
        self.right()
        self.left()
        self.up_left()
        self.up_right()
        self.down_left()
        self.down_right()

        return(self.potential_dict)
    
##test = [[1, 0, 0, 1, 0, 1, 0, 2],
##        [0, 2, 0, 0, 0, 0, 2, 2],
##        [0, 0, 0, 0, 0, 1, 2, 0],
##        [1, 0, 0, 2, 2, 2, 0, 0],
##        [0, 0, 0, 2, 1, 0, 0, 0],
##        [2, 0, 0, 2, 0, 0, 0, 2],
##        [0, 2, 2, 0, 0, 0, 2, 0],
##        [1, 0, 0, 0, 0, 1, 0, 1]]
##
##test1 = [[1, 0, 2, 1, 0, 1, 1, 1],
##         [2, 2, 2, 1, 2, 1, 0, 1],
##         [1, 2, 1, 2, 1, 0, 2, 2],
##         [1, 0, 0, 2, 2, 1, 1, 0]]
##
##test2 = [[1, 0, 0, 1, 0, 0, 0, 1],
##         [0, 0, 0, 0, 0, 0, 0, 1],
##         [0, 2, 0, 0, 0, 0, 0, 2],
##         [0, 0, 2, 0, 0, 1, 2, 0],
##         [1, 0, 0, 1, 2, 2, 0, 0],
##         [0, 0, 0, 2, 1, 0, 0, 0],
##         [0, 0, 2, 0, 1, 0, 0, 0],
##         [0, 2, 0, 0, 1, 2, 0, 0],
##         [2, 0, 1, 2, 1, 0, 2, 0],
##         [1, 2, 0, 0, 0, 0, 0, 0]]
##
##test4 = [[2, 1, 2, 1],
##         [1, 1, 1, 2],
##         [2, 2, 1, 1],
##         [1, 1, 0, 2]]


##for i in range(len(test)):
##    print(test[i])
##gs = GameState(test, 'B')
