# Mark Calabio 12488362
## This module builds the GUI game for Othello
## There are three classes: Othello_board -- takes input for the user and displays the actual board
## and updates everytime a move has been made -- and game_over -- displays a "Game Over" message
## -- and no_more_playing -- tells the user that the game is over and that they should exit the game.

import tkinter
import P4_gamelogic
from Project5_Othello_Options import *
from Project4_GameState import GameState
from Project4_flip_and_count import Flip
from Project4_flip_and_count import Count


class Othello_board:
    def __init__(self, data: list):
        self.board_data = gather_data

        self.rows = gather_data[0]
        self.columns = gather_data[1]               # these variables are similar to the game logic
        self.first_move = gather_data[2]
        self.top_left = gather_data[3]
        self.win_is_determined = gather_data[4]
        
        self.beginning_board = P4_gamelogic.center(P4_gamelogic.create_board(self.rows, self.columns),
                                 self.top_left)

        self.GS = GameState(self.beginning_board, self.first_move)
        self.current_player= self.GS.current_turn

        self.potential_list = self.GS.potential_moves_are()
        self.every_spot = {}        ## used in the function -- self.assign_every_space()

        self.the_switch = 'OFF'
        self.the_end_is_here = None
        
                                            ######## where tkinter stuff begins #######
        self._board_window = tkinter.Tk()

        self._canvas = tkinter.Canvas(master = self._board_window, width = 700,
                                      height = 650, highlightthickness = 0,
                                      background = '#C6EED6')
        
        self._canvas.bind('<Button-1>', self._mouse_clicked)
        self._canvas.bind('<Configure>', self._board_resized)
        
                                                        ### Display logo, turn, and score ###
        self._logo = tkinter.Label(master = self._board_window,
                                   font = ('Impact', 55, 'bold'),
                                   text = 'Othello | FULL', fg = '#B8D18E')

        self._score = tkinter.StringVar()
        self._score.set('Black: 2  White: 2')

        self._turn = tkinter.StringVar()
        self._turn.set('Turn: {}'.format(self.first_move))

        self.score_total = tkinter.Label(master = self._board_window,
                                         textvariable = self._score,
                                         font = ('Impact', 25, 'bold'),
                                         fg = 'black')
        
        self.display_turn = tkinter.Label(master = self._board_window,
                                         textvariable = self._turn,
                                         font = ('Impact', 25, 'bold'),
                                         fg = 'black')
        
                                                        ### Grid stuff happens here ###
        self._logo.grid(row = 0, column = 1, padx= 10,
                        sticky = tkinter.N + tkinter.S +tkinter.W + tkinter.E)
        
        self._canvas.grid(row = 2, column = 0, columnspan = 3, padx = 20, pady = 20,
                          sticky = tkinter.N + tkinter.S +tkinter.W + tkinter.E)

        self.score_total.grid(row = 0, column = 0, padx = 10,
                         sticky = tkinter.N + tkinter.S +tkinter.W + tkinter.E)
        
        self.display_turn.grid(row = 0, column = 2, padx = 20,
                               sticky = tkinter.N + tkinter.S +tkinter.W + tkinter.E)
        
        self._board_window.rowconfigure(0, weight = 1)        
        self._board_window.rowconfigure(1, weight = 1)
        self._board_window.rowconfigure(2, weight = 10)
        self._board_window.columnconfigure(1, weight =1)
        self._board_window.columnconfigure(0, weight = 10)

        self.x_coord = 0
        self.y_coord = 0

    def run_Othello(self):
        self._board_window.mainloop()

    def _board_resized(self, event: tkinter.Event) -> None:
        '''Whenever the board resizes, all the information on the board must remain the same'''
        self._canvas.delete(tkinter.ALL)
        self.set_up_rows()
        self.set_up_columns()
        self.set_up_center()
        self.change_pieces()

    def set_up_rows(self) -> None:
        '''Converts numbers to fractionals to pixels in order to set up the number of rows'''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        for i in range(self.rows):
            self._canvas.create_line(0,(canvas_height/(self.rows))+(canvas_height/(self.rows))*i,
                                     canvas_width,
                                     (canvas_height/(self.rows))+(canvas_height/(self.rows))*i,
                                     fill = 'black')

    def set_up_columns(self) -> None:
        '''Converts numbers to fractionals to pixels in order to set up the number of columns'''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        for i in range(self.columns):
            self._canvas.create_line((canvas_width/(self.columns))+(canvas_width/(self.columns))*i,
                                     0,
                                     (canvas_width/(self.columns))+(canvas_width/(self.columns))*i,
                                     canvas_height,
                                     fill = 'black')

    def set_up_center(self) -> None:
        '''Converts numbers to fractionals to pixels in order to set up center pieces'''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()


        if self.top_left == 'B':
            top_left_color = '#353535'
            opposite_color = 'White'

        if self.top_left == 'W':
            top_left_color = 'White'
            opposite_color = '#353535'


        self._canvas.create_oval((canvas_width/self.columns)*((self.columns/2)-1), (canvas_height/self.rows)*((self.rows/2)-1),
                                     (canvas_width/self.columns)*(self.columns/2),
                                     (canvas_height/self.rows)*(self.rows/2),
                                     outline = 'Black', fill = top_left_color) #####
            
        self._canvas.create_oval((canvas_width/self.columns)*((self.columns/2)), (canvas_height/self.rows)*((self.rows/2)),
                                     (canvas_width/self.columns)*((self.columns/2)+1),
                                     (canvas_height/self.rows)*((self.rows/2)+1),
                                     outline = 'Black', fill = top_left_color)
            
        self._canvas.create_oval((canvas_width/self.columns)*(self.columns/2), (canvas_height/self.rows)*((self.rows/2)-1),
                                     (canvas_width/self.columns)*((self.columns/2)+1),
                                     (canvas_height/self.rows)*(self.rows/2),
                                     outline = 'Black', fill = opposite_color)
        
        self._canvas.create_oval((canvas_width/self.columns)*((self.columns/2)-1), (canvas_height/self.rows)*((self.rows/2)),
                                     (canvas_width/self.columns)*((self.columns/2)),
                                     (canvas_height/self.rows)*((self.rows/2)+1),
                                     outline = 'Black', fill = opposite_color)


#########################################################################################
### These next functions cover the user-clicking -- meaning, they find where each    ####
### potential spot is and where the user can click. Some functions also handle the   ####
### placing of the current player's piece, as well as the flipping of the oponnent's ####
### pieces                                                                           ####


    def assign_every_space(self) -> dict:
        '''With the use of math, pixels, and fractionals, this function provides
        the create_oval coordinates for each spot on the game board'''
        
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        for row in range(len(self.GS.board)):
            for col in range(len(self.GS.board[row])):
                top_left = (col/(self.columns))*canvas_width
                top_right = (col+1)/(self.columns)*canvas_width
                bottom_left = (row/self.rows)* canvas_height
                bottom_right = ((row+1)/self.rows)*canvas_height
                self.every_spot["{},{}".format(row, col)] = (top_left, top_right, bottom_left, bottom_right)

        return self.every_spot

    def _mouse_clicked(self, event: tkinter.Event): ## essential function
        '''This function handles essentially the bulk of the game -- user-interaction
        and placing and flipping pieces'''
        
        self.x_coord = event.x
        self.y_coord = event.y  
        self.potential_clicks()
        the_move = self.click_valid()
        if self.the_end_is_here == None:
            try:
                if self.the_switch == 'ON':
                    updated_board = self.place_and_flip_pieces(the_move)
                    self.change_pieces()
                    self.flush_everything()

                        
            except TypeError:
                pass
            
        else:
            no_more_playing()
            print('Oops! The GAME is OVER! \n\n Either RESTART and PLAY AGAIN, or go outside and oberve nature and whatnot') # COUNT OCCURS HERE

        

    def potential_clicks(self):
        '''This function forms the potential pixel locations a player can click on'''
        
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        clicks = {}
        
        for a in self.potential_list:
            if self.potential_list[a] == None:
                continue
            for x,y in self.potential_list[a]:
                top_left = (y/(self.columns))*canvas_width
                top_right = (y+1)/(self.columns)*canvas_width
                bottom_left = (x/self.rows)* canvas_height
                bottom_right = ((x+1)/self.rows)*canvas_height
                clicks["{} , {}".format(x,y)] = (top_left,top_right, bottom_left, bottom_right)
        return clicks

    def click_valid(self):
        '''This function determines whether or not a user's location of a click
        is a valid spot for the placing of a piece. This function uses the dictionary
        from self.potential_clicks'''
        
        the_move = []
        clicks = self.potential_clicks()
##                                            print(self.x_coord, self.y_coord)
        for every in clicks:
            if clicks[every][0] <= self.x_coord <= clicks[every][1] and clicks[every][2] <= self.y_coord <= clicks[every][3]:
                    the_move.append(every.split())
                    self.the_switch = 'ON'
##                                                    print(the_move)
                    return the_move
    
    def place_and_flip_pieces(self, the_move: list):
        '''This function places a piece on the 2D LIST, and flips other's pieces on that 2D LIST'''
        
        place_row = int(the_move[0][0]) + 1
        place_column = int(the_move[0][2]) + 1
        direction_list = P4_gamelogic.valid_move_list(place_row, place_column, self.GS)        
        self.GS.board = P4_gamelogic.place_piece(self.GS, place_row, place_column)
        self.GS.board = P4_gamelogic.officially_flip_captured_pieces(self.GS.board, self.GS, direction_list,
                                                                     place_row, place_column)

        return self.GS.board

    def change_pieces(self):
        '''This function reads from the newly updated 2D LIST, and creates ovals on the
        newly updated board, placing and flipping pieces'''
        
        all_pieces = self.assign_every_space()
        for row in range(len(self.GS.board)):
            for col in range(len(self.GS.board[row])):
                if self.GS.board[row][col] == 1:
                    self._canvas.create_oval(all_pieces["{},{}".format(row, col)][0], all_pieces["{},{}".format(row, col)][2],
                                     all_pieces["{},{}".format(row, col)][1],all_pieces["{},{}".format(row, col)][3],
                                             outline = 'Black', fill = '#353535')

                elif self.GS.board[row][col] == 2:
                    self._canvas.create_oval(all_pieces["{},{}".format(row, col)][0], all_pieces["{},{}".format(row, col)][2],
                                     all_pieces["{},{}".format(row, col)][1],all_pieces["{},{}".format(row, col)][3],
                                             outline = 'Black', fill = 'White')                   
        

 ## I say "flush_everything" because this function basically creates a new gamestate and keeps the game going until the end 
                    
    def flush_everything(self):    
        '''This function creates a new GameState and decides whether the game should end
        or not'''
        C = Count(self.GS, self.win_is_determined)
        C.is_game_board_filled()

        if C.game_over == None:
            print('GAME BOARD IS FILLED UP')
            C.count()
            display = C.display_dis_count()
            self._score.set(display)
            self._turn.set("WINNER: {}".format(C.win_with_count()))
            game_is_over()
            self.the_end_is_here = 'THE END IS HERE'
            
        else:
            self.GS = P4_gamelogic.return_fresh_gamestate(self.GS)
            the_count = P4_gamelogic.check_if_current_player_has_moves(self.GS)
            if the_count == 8:
                self.GS = P4_gamelogic.return_fresh_gamestate(self.GS)
                other_count = P4_gamelogic.check_if_current_player_has_moves(self.GS)
                if other_count != 8:                                                    ## case in which players switch
                    print("SWITCH TURNS..CURRENT TURN: ", self.GS.current_turn)
                    self.current_player= self.GS.current_turn
                    self.potential_list = self.GS.potential_moves_are()
                    self.the_switch = 'OFF'                                    
                else:
                    C.count()
                    display = C.display_dis_count()
                    self._score.set(display)
                    self._turn.set("WINNER: {}".format(C.win_with_count()))
                    game_is_over() ## game ends early, time to head to the end
                    self.the_end_is_here = 'THE END IS HERE' 
            else:
                self._turn.set("Turn: {}".format(self.GS.current_turn))
                C.count()
                display = C.display_dis_count()
                self._score.set(display)
                self.current_player = self.GS.current_turn
                self.potential_list = self.GS.potential_moves_are()
                self.the_switch = 'OFF' 




class game_is_over: ## this function displays the 'GAME OVER' message after the game is over
    def __init__(self):
        self.root_window = tkinter.Tk()

        self.game_over_message = tkinter.Message(master = self.root_window,
                text = ('GAME OVER!'),
                               font = ('Impact', 55))


        self.game_over_message.pack()

class no_more_playing: ## this function displays a window anytime a player makes a move after a game has ended
    def __init__(self):
        self.root_window = tkinter.Tk()

        self.no_more = tkinter.Message(master = self.root_window,
                                       text = 'Game is already over! \n Please exit out of this game!',
                                       font = ('Impact', 25))

        self.no_more.pack()

        


        

if __name__ == '__main__': ## they don't want you to execute this program
    o = othello_introduction()
    
    try:
        o.display_introduction()

        the_game = Othello_board(gather_data)
        the_game.run_Othello()
    except:
        print('Goodbye!')
