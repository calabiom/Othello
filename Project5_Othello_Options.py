# Mark Calabio 12488362
## This module builds the "Options" menu and creates the board with input from the user's
## input/clicking of their board settings/preferences

### NOTES (6:37PM, 3/11/16): This, in all honesty, is perhaps the worst way I could build the options
### menu. There is lot of duplicated code and unecessary classes and functions in this module.
### I absolutely know there's a better way of going about this, yet due to the limited
### time I had, creating the options/menu was the least of my worries! 

import tkinter

gather_data = []

class othello_introduction(): ## this essentially, is the class that handles all the options for the user
    def __init__(self):
        self.window = tkinter.Tk()
        
    def display_introduction(self):
        
        options_message = tkinter.Message(master = self.window,
                                          font = ('Verdana', 20),
                                          pady = 100, fg = 'Green',
                                          text = 'Welcome to Othello!')

        lets_play = tkinter.Button(master = self.window, text = 'Let\'s play!',
                                   font = ('Verdana', 15), pady = 20, padx = 20,
                                          width = 15, command = self._button_play)
        
        options_message.grid(row = 0, column = 0, columnspan = 2, sticky =
                             tkinter.N + tkinter.W + tkinter.E + tkinter.S)
        lets_play.grid(row = 1, column = 0, sticky =
                       tkinter.N + tkinter.W + tkinter.E + tkinter.S)

        self.window.rowconfigure(0, weight = 1)
        self.window.rowconfigure(1, weight = 1)
        self.window.columnconfigure(0, weight = 1)

        self.window.mainloop()

    def _button_play(self):
        print('Okay let\'s play then!') ###leads to options of setting up board
        self.window.destroy()
        row_options().display_row_options()


#################################################################

class row_options(): 
    def __init__(self):
        self.options_row = tkinter.Tk()

    def display_row_options(self):
        row_options = tkinter.Message(master = self.options_row,
                                      text = 'Choose the number of rows on the board',
                                      font = ('Verdana', 20), padx = 30, pady = 30, fg = 'Green')

        row_options.pack(expand = tkinter.TRUE)

        choose_four = tkinter.Button(master = self.options_row,
                            text = '4', font = ('Helvetica', 15), width = 15,
                            command = self.four_clicked)

        choose_six = tkinter.Button(master = self.options_row,
                            text = '6', font = ('Helvetica', 15), width = 15,
                            command = self.six_clicked)

        choose_eight = tkinter.Button(master = self.options_row,
                            text = '8', font = ('Helvetica', 15), width = 15,
                            command = self.eight_clicked)

        choose_ten = tkinter.Button(master = self.options_row,
                            text = '10', font = ('Helvetica', 15), width = 15,
                            command = self.ten_clicked)

        choose_twelve = tkinter.Button(master = self.options_row,
                            text = '12', font = ('Helvetica', 15), width = 15,
                            command = self.twelve_clicked)

        choose_fourteen = tkinter.Button(master = self.options_row,
                            text = '14', font = ('Helvetica', 15), width = 15,
                            command = self.fourteen_clicked)

        choose_sixteen = tkinter.Button(master = self.options_row,
                            text = '16', font = ('Helvetica', 15), width = 15,
                            command = self.sixteen_clicked)

        choose_four.pack()
        choose_six.pack()
        choose_eight.pack()
        choose_ten.pack()
        choose_twelve.pack()
        choose_fourteen.pack()
        choose_sixteen.pack()

    def four_clicked(self):
        gather_data.append(4)
        self.options_row.destroy()
        col_options().display_column_options()

    def six_clicked(self):
        gather_data.append(6)
        self.options_row.destroy()
        col_options().display_column_options()

    def eight_clicked(self):
        gather_data.append(8)
        self.options_row.destroy()
        col_options().display_column_options()
        
    def ten_clicked(self):
        gather_data.append(10)
        self.options_row.destroy()
        col_options().display_column_options()
        
    def twelve_clicked(self):
        gather_data.append(12)
        self.options_row.destroy()
        col_options().display_column_options()
        
    def fourteen_clicked(self):
        gather_data.append(14)
        self.options_row.destroy()
        col_options().display_column_options()
        
    def sixteen_clicked(self):
        gather_data.append(16)
        self.options_row.destroy()
        col_options().display_column_options()

    def start_everything(self):
        self.options_row.mainloop()

##############################################################################

class col_options():
    
    def __init__(self):
        self.options_col = tkinter.Tk()

    def display_column_options(self):
        col_options = tkinter.Message(master = self.options_col,
                                      text = 'Choose the number of columns on the board',
                                      font = ('Verdana', 20), padx = 30, pady = 30, fg = 'Green')

        col_options.pack(expand = tkinter.TRUE)

        choose_four = tkinter.Button(master = self.options_col,
                            text = '4', font = ('Helvetica', 15), width = 15,
                            command = self.four_clicked)

        choose_six = tkinter.Button(master = self.options_col,
                            text = '6', font = ('Helvetica', 15), width = 15,
                            command = self.six_clicked)

        choose_eight = tkinter.Button(master = self.options_col,
                            text = '8', font = ('Helvetica', 15), width = 15,
                            command = self.eight_clicked)

        choose_ten = tkinter.Button(master = self.options_col,
                            text = '10', font = ('Helvetica', 15), width = 15,
                            command = self.ten_clicked)

        choose_twelve = tkinter.Button(master = self.options_col,
                            text = '12', font = ('Helvetica', 15), width = 15,
                            command = self.twelve_clicked)

        choose_fourteen = tkinter.Button(master = self.options_col,
                            text = '14', font = ('Helvetica', 15), width = 15,
                            command = self.fourteen_clicked)

        choose_sixteen = tkinter.Button(master = self.options_col,
                            text = '16', font = ('Helvetica', 15), width = 15,
                            command = self.sixteen_clicked)

        choose_four.pack()
        choose_six.pack()
        choose_eight.pack()
        choose_ten.pack()
        choose_twelve.pack()
        choose_fourteen.pack()
        choose_sixteen.pack()

    def four_clicked(self):
        gather_data.append(4)
        self.options_col.destroy()
        first_move().display_options()

    def six_clicked(self):
        gather_data.append(6)
        self.options_col.destroy()
        first_move().display_options()

    def eight_clicked(self):
        gather_data.append(8)
        self.options_col.destroy()
        first_move().display_options()
        
    def ten_clicked(self):
        gather_data.append(10)
        self.options_col.destroy()
        first_move().display_options()
        
    def twelve_clicked(self):
        gather_data.append(12)
        self.options_col.destroy()
        first_move().display_options()
        
    def fourteen_clicked(self):
        gather_data.append(14)
        self.options_col.destroy()
        first_move().display_options()
        
    def sixteen_clicked(self):
        gather_data.append(16)
        self.options_col.destroy()
        first_move().display_options()

##############################################################################

class first_move():
    def __init__(self):
        self.options_move = tkinter.Tk()

    def display_options(self):
        first_move = tkinter.Message(master = self.options_move,
                                     text = 'Who plays first?',
                                     font = ('Verdana', 20), padx = 30, pady = 30, fg = 'Green')

        first_move.pack(expand = tkinter.TRUE)

        play_black = tkinter.Button(master = self.options_move, fg = 'Black',
                                      font = ('Verdana', 20, 'bold'),
                                      text= 'Black', width = 15, command = self._choose_black)
        play_white = tkinter.Button(master = self.options_move, text = 'White',
                                font = ('Verdana', 20, 'bold'),
                                fg = 'White', width = 15, command = self._choose_white)

        play_black.pack()
        play_white.pack()

    def _choose_black(self):
        gather_data.append('B')
        self.options_move.destroy()
        top_left_arrangement().display_options()

    def _choose_white(self):
        gather_data.append('W')
        self.options_move.destroy()
        top_left_arrangement().display_options()

class top_left_arrangement():
    def __init__(self):
        self.arrange = tkinter.Tk()

    def display_options(self):
        top_left = tkinter.Message(master = self.arrange,
                                   text = 'Who is on the top left on the center of the board?',
                                   font = ('Verdana', 20), padx = 10, pady = 30, fg = 'Green')
        top_left.pack(expand = tkinter.TRUE)

        is_it_black = tkinter.Button(master = self.arrange, fg = 'Black',
                                      font = ('Verdana', 20, 'bold'),
                                      text= 'Black', width = 15, command = self._choose_black)

        is_it_white = tkinter.Button(master = self.arrange, fg = 'White',
                                      font = ('Verdana', 20, 'bold'),
                                      text= 'White', width = 15, command = self._choose_white)

        is_it_black.pack()
        is_it_white.pack()
        
    def _choose_black(self):
        gather_data.append('B')
        self.arrange.destroy()
        win_is_determined().display_options()

    def _choose_white(self):
        gather_data.append('W')
        self.arrange.destroy()
        win_is_determined().display_options()

class win_is_determined():
    def __init__(self):
        self.win_window = tkinter.Tk()

    def display_options(self):
        win_method = tkinter.Message(master = self.win_window,
                                     text = 'How is the win determined?', font = ('Verdana', 20),
                                     padx = 10, pady = 30, fg = 'Green')
        win_method.pack(expand = tkinter.TRUE)

        most_pieces = tkinter.Button(master = self.win_window, fg = 'Black',
                                      font = ('Verdana', 15, 'bold'),
                                      text= 'Player wins by most amount of pieces', width = 40, command = self._choose_most)
        
        least_pieces = tkinter.Button(master = self.win_window, fg = 'Black',
                                      font = ('Verdana', 15, 'bold'),
                                      text= 'Player wins by least amount of pieces', width = 40, command = self._choose_black)

        most_pieces.pack()
        least_pieces.pack()

    def _choose_most(self):
        gather_data.append('>')
        print(gather_data)
        self.win_window.destroy()

    def _choose_black(self):
        gather_data.append('<')
        print(gather_data)
        self.win_window.destroy()

        
        
