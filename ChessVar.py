# Author: Adam Spivak
# GitHub: Muzyka55
# Date: 1-10-23
# Description: A game that is a variant of chess. There is a board with 12 pieces on one side of the board, 6 white and
# 6 black, with a goal to reach the other side of the board. There are 4 knights (2 white and 2 black), 4 bishops (2
# white and 2 black), 2 Rooks (1 white and 1 black), and 2 kings (1 white and 1 black). Class ChessVar() is the main
# class of this program, as it where the game will be played. The class Game_piece is the base class for 4 inherited
# class, to represent each game piece on the board. The Super Class has position and color, and potential_positions.
# This is because each piece moves in their own direction, and the position move have to be calculated differently for
# each piece. Class Position is used to help keep track of the position on the board by creating a new object, versus
# trying to use a tuple for both a row and column in a 2D list, which is used to represent the chess board. In Class
# ChessVar, it initializes board using a 2D list, and the game pieces on the board using a list. It also has methods to
# move the game pieces on the board, check if game piece move is valid, and checking the state of the game.

class Position:
    """Class Position is used to store information on the position of each piece on the board. Makes it easier later
    when using a 2D list, where you can one object to self._position in Game_Piece instead of both a row and a column"""

    def __init__(self, pos_name, row, column):
        self._pos_name = pos_name
        self._row = row
        self._colum = column

    def get_pos_name(self):
        return self._pos_name

    def get_row(self):
        return self._row

    def get_column(self):
        return self._colum

    def set_pos_name(self, pos_name):
        self._pos_name = pos_name

    def set_row(self, row):
        self._row = row

    def set_colum(self, column):
        self._colum = column


class Game_Piece:
    """Game_Piece is a base class to represent the pieces on the board, and have attributes such as _name, _color,
     _position, _potential_positions, and _chess_board. It has a copy of the chess board so any piece will know
     information about the board, so it can calculate where it can move. The inherited classes have their own
     calc_potential_moves because they all move differently."""

    def __init__(self, name, color):
        self._name = name
        self._color = color
        self._position = None  # Will be a Position object
        self._potential_position = {}
        # [Row][Col]    Col:    0     1     2     3     4     5     6     7      Row:
        self._chess_board = [["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"],  # 0
                             ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],  # 1
                             ["A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3"],  # 2
                             ["A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4"],  # 3
                             ["A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5"],  # 4
                             ["A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6"],  # 5
                             ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],  # 6
                             ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"]]  # 7

    def check_color(self, row, column, pieces_on_board):
        """Uses row and column to find key, and uses key in pieces_on_board to get the pieces color"""
        game_piece_color = pieces_on_board[self._chess_board[row][column]].get_color()

        if self._color == game_piece_color:
            return True
        else:
            return False

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color

    def get_position(self):
        return self._position

    def get_potential_positions(self):
        return self._potential_position

    def set_position(self, pos_name, row, column):
        """Will be used later to set position"""
        self._position = Position(pos_name, row, column)


class King(Game_Piece):
    """An inherited class that represents the King pieces on the board. Calc_potential_positions looks for potential
    positions going 1 space Up, Down, Left, Right, Up Right, Up Left, Down Left, and Down Right.  If a piece is on the
    potential path for the current piece, it stops looking through the board for new potential positions. If it's the
    opposite color it adds the piece to the potential_position so that it can be taken off the board."""

    def __init__(self, name, color):
        super().__init__(name, color)

    def calc_potential_position(self, pieces_on_board):
        """Calculates the potential positions """
        chess_board = self._chess_board
        game_pieces = pieces_on_board
        position = self._position

        row = position.get_row()
        column = position.get_column()

        # Checks if each move is within the limits of the board, and creates a position object for each move
        if column - 1 >= 0:  # Left
            left = column - 1
            left_pos = Position(chess_board[row][left], row, left)
            if chess_board[row][left] not in game_pieces:
                self._potential_position[chess_board[row][left]] = left_pos
            elif chess_board[row][left] in game_pieces:
                if not self.check_color(row, left, pieces_on_board):
                    self._potential_position[chess_board[row][left]] = left_pos

        if column + 1 < 8:  # Right
            right = column + 1
            right_pos = Position(chess_board[row][right], row, right)
            if chess_board[row][right] not in game_pieces:
                self._potential_position[chess_board[row][right]] = right_pos
            elif chess_board[row][right] in game_pieces:
                if not self.check_color(row, right, pieces_on_board):
                    self._potential_position[chess_board[row][right]] = right_pos

        if row - 1 >= 0:  # Down
            down = row - 1
            down_pos = Position(chess_board[down][column], down, column)
            if chess_board[down][column] not in game_pieces:
                self._potential_position[chess_board[down][column]] = down_pos
            elif chess_board[down][column] in game_pieces:
                if not self.check_color(down, column, pieces_on_board):
                    self._potential_position[chess_board[down][column]] = down_pos

        if row + 1 < 8:  # Up
            up = row + 1  # It's going up since A1 is at row 0
            up_pos = Position(chess_board[up][column], up, column)
            if chess_board[up][column] not in game_pieces:
                self._potential_position[chess_board[up][column]] = up_pos
            elif chess_board[up][column] in game_pieces:
                if not self.check_color(row, right, pieces_on_board):
                    self._potential_position[chess_board[row][right]] = up_pos

        if row+1 < 8 and column+1 < 8:  # Up one, One Right
            upOne_OneRight = Position(chess_board[row+1][column+1], row+1, column+1)
            if chess_board[row+1][column+1] not in game_pieces:
                self._potential_position[chess_board[row+1][column+1]] = upOne_OneRight
            else:
                if not self.check_color(row+1, column+1, pieces_on_board):
                    self._potential_position[chess_board[row+1][column+1]] = upOne_OneRight

        if row+1 < 8 and column-1 >= 0:  # Up one, One Left
            upOne_OneLeft = Position(chess_board[row+1][column-1], row+1, column-1)
            if chess_board[row+1][column-1] not in game_pieces:
                self._potential_position[chess_board[row+1][column-1]] = upOne_OneLeft
            else:
                if not self.check_color(row+1, column-1, pieces_on_board):
                    self._potential_position[chess_board[row+1][column-1]] = upOne_OneLeft

        if row-1 >= 0 and column+1 < 8:  # Down one, One Right
            downOne_OneRight = Position(chess_board[row-1][column+1], row-1, column+1)
            if chess_board[row-1][column+1] not in game_pieces:
                self._potential_position[chess_board[row-1][column+1]] = downOne_OneRight
            else:
                if not self.check_color(row-1, column+1, pieces_on_board):
                    self._potential_position[chess_board[row-1][column+1]] = downOne_OneRight

        if row-1 >= 0 and column-1 >= 0:  # Down one, One Left
            downOne_OneLeft = Position(chess_board[row-1][column-1], row-1, column-1)
            if chess_board[row-1][column-1] not in game_pieces:
                self._potential_position[chess_board[row-1][column-1]] = downOne_OneLeft
            else:
                if not self.check_color(row-1, column-1, pieces_on_board):
                    self._potential_position[chess_board[row-1][column-1]] = downOne_OneLeft


class Bishop(Game_Piece):
    """An inherited class from Game_Piece that represents the Bishop pieces on the board. In its
    calc_potential_positions, it looks diagonally across the board for each possible position. If a piece
    is on the potential path for the current piece, it stops looking through the board for new potential positions. If
    it's the opposite color it adds the piece to the potential_position so that it can be taken off the board"""
    def __init__(self, name, color):
        super().__init__(name, color)

    def calc_potential_position(self, pieces_on_board):
        """Calculates paths by looking diagonally across the board"""
        chess_board = self._chess_board
        game_pieces = pieces_on_board
        position = self._position

        # Calculates to the Up Right Corner
        row = position.get_row() + 1
        column = position.get_column() + 1
        while row < 8 and column < 8:  # While still on Chessboard
            up_right = Position(chess_board[row][column], row, column)

            if chess_board[row][column] not in game_pieces:  # If there is another piece in that pos
                self._potential_position[chess_board[row][column]] = up_right
            else:
                # Stops calculating the potential positions if there is a piece blocking its path
                if not self.check_color(row, column, pieces_on_board):
                    self._potential_position[chess_board[row][column]] = up_right
                row = 8

            row += 1
            column += 1

        # Calculates to the Down Right Corner
        row = position.get_row() - 1
        column = position.get_column() + 1
        while row >= 0 and column < 8:  # While still on Chessboard
            down_right = Position(chess_board[row][column], row, column)

            if chess_board[row][column] not in game_pieces:   # If there is another piece in that pos
                self._potential_position[chess_board[row][column]] = down_right
            else:
                # Stops calculating the potential positions if there is a piece blocking its path
                if not self.check_color(row, column, pieces_on_board):
                    self._potential_position[chess_board[row][column]] = down_right
                row = -1

            row -= 1
            column += 1

        # Calculates to the Down Left Corner
        row = position.get_row() - 1
        column = position.get_column() - 1
        while row >= 0 and column >= 0:  # While still on Chessboard
            down_left = Position(chess_board[row][column], row, column)

            if chess_board[row][column] not in game_pieces:  # If there is another piece in that pos
                self._potential_position[chess_board[row][column]] = down_left
            else:
                # Stops calculating the potential positions if there is a piece blocking its path
                if not self.check_color(row, column, pieces_on_board):
                    self._potential_position[chess_board[row][column]] = down_left
                row = -1

            row -= 1
            column -= 1

        # Calculates to the Up Left Corner
        row = position.get_row() + 1
        column = position.get_column() - 1
        while row < 8 and column >= 0:  # While still on Chessboard
            up_left = Position(chess_board[row][column], row, column)

            if chess_board[row][column] not in game_pieces:  # If there is another piece in that pos
                self._potential_position[chess_board[row][column]] = up_left
            else:
                # Stops calculating the potential positions if there is a piece blocking its path
                if not self.check_color(row, column, pieces_on_board):
                    self._potential_position[chess_board[row][column]] = up_left
                column = -1

            row += 1
            column -= 1


class Rook(Game_Piece):
    """An inherited class from Game_Piece that represents the Rook on the board. In its
    calc_potential_positions, it looks Up, Down, Left, and Right across the board for each possible position. If a piece
    is on the potential path for the current piece, it stops looking through the board for new potential positions. If
    it's the opposite color it adds the piece to the potential_position so that it can be taken off the board"""
    def __init__(self, name, color):
        super().__init__(name, color)

    def calc_potential_position(self, pieces_on_board):
        """Calculates the potential path of the rook by looking to each end of the board"""
        chess_board = self._chess_board
        game_pieces = pieces_on_board
        position = self._position

        # Calculates to the top of the board
        row = position.get_row() + 1
        column = position.get_column()
        while row < 8:  # While still on Chessboard
            up_pos = Position(chess_board[row][column], row, column)

            if chess_board[row][column] not in game_pieces:  # If there is another piece in that pos
                self._potential_position[chess_board[row][column]] = up_pos
            else:
                # Stops calculating the potential positions if there is a piece blocking its path
                if not self.check_color(row, column, pieces_on_board):
                    self._potential_position[chess_board[row][column]] = up_pos
                row = 8

            row += 1

        # Calculates to the bottom of the board
        row = position.get_row() - 1
        column = position.get_column()
        while row >= 0:  # While still on Chessboard
            down_pos = Position(chess_board[row][column], row, column)

            if chess_board[row][column] not in game_pieces:  # If there is another piece in that pos
                self._potential_position[chess_board[row][column]] = down_pos
            else:
                # Stops calculating the potential positions if there is a piece blocking its path
                if not self.check_color(row, column, pieces_on_board):
                    self._potential_position[chess_board[row][column]] = down_pos
                row = -1

            row -= 1

        # Calculates to the left of the board
        row = position.get_row()
        column = position.get_column() - 1
        while column >= 0:  # While still on Chessboard
            left_pos = Position(chess_board[row][column], row, column)

            if chess_board[row][column] not in game_pieces:  # If there is another piece in that pos
                self._potential_position[chess_board[row][column]] = left_pos
            else:
                # Stops calculating the potential positions if there is a piece blocking its path
                if not self.check_color(row, column, pieces_on_board):
                    self._potential_position[chess_board[row][column]] = left_pos
                column = -1

            column -= 1

        # Calculates to the right of the board
        row = position.get_row()
        column = position.get_column() + 1
        while column < 8:  # While still on Chessboard
            right_pos = Position(chess_board[row][column], row, column)

            if chess_board[row][column] not in game_pieces:  # If there is another piece in that pos
                self._potential_position[chess_board[row][column]] = right_pos
            else:
                # Stops calculating the potential positions if there is a piece blocking its path
                if not self.check_color(row, column, pieces_on_board):
                    self._potential_position[chess_board[row][column]] = right_pos
                column = 9

            column += 1


class Knight(Game_Piece):
    """An inherited class from Game_Piece that represents the Rook on the board. In its
    calc_potential_positions, it looks in L-Shapes across the board for each possible position. If
    it's the opposite color it adds the piece to the potential_position so that it can be taken off the board"""

    def __init__(self, name, color):
        super().__init__(name, color)

    def calc_potential_position(self, pieces_on_board):
        """The Knight can move in 8 different direction, all of which are calculated in this function. It does this by
        checking if the change in position is still within the limits of the board. From there, it checks if there is
        another piece on the board with that position. If there is a Piece in that position, it checks if it's the
        opposite color, so it may take the piece later on."""
        chess_board = self._chess_board
        game_pieces = pieces_on_board
        position = self._position

        row = position.get_row()
        column = position.get_column()

        if row+1 < 8 and column-2 >= 0:  # Up one, Two Left
            upOne_twoLeft = Position(chess_board[row+1][column-2], row+1, column-2)
            if chess_board[row+1][column-2] not in game_pieces:
                self._potential_position[chess_board[row+1][column-2]] = upOne_twoLeft
            else:
                if not self.check_color(row+1, column-2, pieces_on_board):
                    self._potential_position[chess_board[row + 1][column - 2]] = upOne_twoLeft

        if row+1 < 8 and column+2 < 8:  # Up one, Two Right
            upOne_twoRight = Position(chess_board[row+1][column+2], row+1, column+2)
            if chess_board[row+1][column+2] not in game_pieces:
                self._potential_position[chess_board[row+1][column+2]] = upOne_twoRight
            else:
                if not self.check_color(row+1, column+2, pieces_on_board):
                    self._potential_position[chess_board[row + 1][column + 2]] = upOne_twoRight

        if row+2 < 8 and column+1 < 8:  # Up Two, One Right
            upTwo_oneRight = Position(chess_board[row+2][column+1], row+2, column+1)
            if chess_board[row+2][column+1] not in game_pieces:
                self._potential_position[chess_board[row+2][column+1]] = upTwo_oneRight
            else:
                if not self.check_color(row+2, column+1, pieces_on_board):
                    self._potential_position[chess_board[row + 2][column + 1]] = upTwo_oneRight

        if row+2 < 8 and column-1 < 8:  # Up Two, One Left
            upTwo_oneLeft = Position(chess_board[row+2][column-1], row+2, column-1)
            if chess_board[row+2][column-1] not in game_pieces:
                self._potential_position[chess_board[row+2][column-1]] = upTwo_oneLeft
            else:
                if not self.check_color(row+2, column-1, pieces_on_board):
                    self._potential_position[chess_board[row + 2][column - 1]] = upTwo_oneLeft

        if row-1 >= 0 and column+2 < 8:  # Down One, Two Right
            print("ERROR HERE:", row-1, column+2)
            downOne_twoRight = Position(chess_board[row-1][column+2], row-1, column+2)
            if chess_board[row-1][column+2] not in game_pieces:
                self._potential_position[chess_board[row-1][column+2]] = downOne_twoRight
            else:
                if not self.check_color(row-1, column+2, pieces_on_board):
                    self._potential_position[chess_board[row - 1][column + 2]] = downOne_twoRight

        if row-1 >= 0 and column-2 >= 0:  # Down One, Two Left
            downOne_twoLeft = Position(chess_board[row-1][column-2], row-1, column-2)
            if chess_board[row-1][column-2] not in game_pieces:
                self._potential_position[chess_board[row-1][column-2]] = downOne_twoLeft
            else:
                if not self.check_color(row-1, column-2, pieces_on_board):
                    self._potential_position[chess_board[row - 1][column - 2]] = downOne_twoLeft

        if row-2 >= 0 and column+1 < 8:  # Down Two, One Right
            downTwo_oneRight = Position(chess_board[row-2][column+1], row-2, column+1)
            if chess_board[row-2][column+1] not in game_pieces:
                self._potential_position[chess_board[row-2][column+1]] = downTwo_oneRight
            else:
                if not self.check_color(row-2, column+1, pieces_on_board):
                    self._potential_position[chess_board[row - 2][column + 1]] = downTwo_oneRight

        if row-2 >= 0 and column-1 >= 0:  # Down Two, One Left
            downTwo_oneLeft = Position(chess_board[row-2][column-1], row-2, column-1)
            if chess_board[row-2][column-1] not in game_pieces:
                self._potential_position[chess_board[row-2][column-1]] = downTwo_oneLeft
            else:
                if not self.check_color(row-2, column-1, pieces_on_board):
                    self._potential_position[chess_board[row - 2][column - 1]] = downTwo_oneLeft


class ChessVar:
    """The class the represents the chessboard and game actions. In the initializers, it initializes the Chessboard as a
     2D array, an empty list for the game pieces on the board, whose turn it is, and the game state. Underneath
     initializing those variables, it initializes the game pieces and sets their positions on the board"""
    
    def __init__(self):
        """Initializes the chess board, the pieces on the board, whose turn it is , and the state of the game"""
        # [Row][Col]    Col:    0     1     2     3     4     5     6     7      Row:
        self._chess_board = [["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"],  # 0
                             ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],  # 1
                             ["A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3"],  # 2
                             ["A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4"],  # 3
                             ["A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5"],  # 4
                             ["A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6"],  # 5
                             ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],  # 6
                             ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"]]  # 7

        # [Row][Col]          Col:     0      1      2      3      4      5      6      7      Row:
        self._empty_chess_board = [["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],  # 0
                                   ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],  # 1
                                   ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],  # 2
                                   ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],  # 3
                                   ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],  # 4
                                   ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],  # 5
                                   ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],  # 6
                                   ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]]  # 7

        self._colors_turn = "WHITE"  # Starts as white and swaps colors with each game call
        self._game_state = "UNFINISHED"  # UNFINISHED, WHITE_WON, BLACK_WON, TIE

        self._game_pieces = {"A1": King("WK ", "WHITE"),
                             "H1": King("BK ", "BLACK"),
                             "B1": Bishop("WB1", "WHITE"),
                             "B2": Bishop("WB2", "WHITE"),
                             "G1": Bishop("BB1", "BLACK"),
                             "G2": Bishop("BB2", "BLACK"),
                             "A2": Rook("WR ", "WHITE"),
                             "H2": Rook("BR ", "BLACK"),
                             "C1": Knight("WK1", "WHITE"),
                             "C2": Knight("WK2", "WHITE"),
                             "F1": Knight("BK1", "BLACK"),
                             "F2": Knight("BK2", "BLACK")}

        # Sets the locations of the game pieces on the board
        self._game_pieces["A1"].set_position(self._chess_board[0][0], 0, 0)
        self._game_pieces["H1"].set_position(self._chess_board[0][7], 0, 7)
        self._game_pieces["B1"].set_position(self._chess_board[0][1], 0, 1)
        self._game_pieces["B2"].set_position(self._chess_board[1][1], 1, 1)
        self._game_pieces["G1"].set_position(self._chess_board[0][6], 0, 6)
        self._game_pieces["G2"].set_position(self._chess_board[1][6], 1, 6)
        self._game_pieces["A2"].set_position(self._chess_board[1][0], 1, 0)
        self._game_pieces["H2"].set_position(self._chess_board[1][7], 1, 7)
        self._game_pieces["C1"].set_position(self._chess_board[0][2], 0, 2)
        self._game_pieces["C2"].set_position(self._chess_board[1][2], 1, 2)
        self._game_pieces["F1"].set_position(self._chess_board[0][5], 0, 5)
        self._game_pieces["F2"].set_position(self._chess_board[1][5], 1, 5)

    def get_chess_board(self):
        return self._chess_board

    def get_empty_chess_board(self):
        return self._empty_chess_board

    def get_game_pieces(self):
        return self._game_pieces

    def get_game_state(self):
        return self._game_state

    def get_color(self):
        return self._colors_turn

    def change_color(self):
        """Updates game color turn, and swaps between white and black"""
        if self._colors_turn == "WHITE":
            self._colors_turn = "BLACK"
        elif self._colors_turn == "BLACK":
            self._colors_turn = "WHITE"

    def update_chess_board(self):
        """Updates the empty chessboard with every call and changes the positions of the pieces on the board for a
        visual representation of the game"""
        row = 0
        column = 0
        while row < 8:
            while column < 8:
                self._empty_chess_board[row][column] = "   "
                column += 1
            column = 0
            row += 1

        for positions in self._game_pieces:
            pieces_position = self._game_pieces[positions].get_position()
            name = self._game_pieces[positions].get_name()
            row = pieces_position.get_row()
            column = pieces_position.get_column()

            self._empty_chess_board[row][column] = name

    def update_game_state(self):
        """Updates the _game_state depending on conditions, such as if the move is BLACK, and if King is in
        the last row. If the move is not BLACK, the game cannot be finished. If the move is BLACK, check for King
        in the last row, and then determine who won based on color"""
        end_row = ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"]
        white_piece = None
        black_piece = None

        if self._colors_turn == "BLACK":  # Game ends on blacks move
            for row_8 in end_row:  # Last move in the game
                if row_8 in self._game_pieces:  # If there is a piece in this row
                    if self._game_pieces[row_8] is isinstance(self._game_pieces[row_8], King):  # If the piece in that row is a King
                        color = self._game_pieces[row_8].get_color()  # Checks for the color of the piece that is in this row
                        if color == "BLACK":
                            black_piece = self._game_pieces[row_8]
                        elif color == "WHITE":
                            white_piece = self._game_pieces[row_8]

            if black_piece is not None and white_piece is not None:
                self._game_state = "TIE"
            elif white_piece is not None:
                self._game_state = "WHITE_WON"
            elif black_piece is not None:
                self._game_state = "BLACK_WON"
            else:
                return "UNFINISHED"

        else:
            self._game_state = "UNFINISHED"  # Game cannot be finished if white is the current move

    def make_move(self, current_pos, new_pos):
        """make_move does a few things: It updates and checks the status of the game, checks which color move the game
         is on, checks if the current piece is putting the king into check or not. Returns true if move can be made, but
         returns false otherwise"""
        if self._game_state == "UNFINISHED":
            print("UNFINISHED")
            current_position = current_pos[0].upper() + current_pos[1]  # Makes sure the call to change position is capital
            new_position = new_pos[0].upper() + new_pos[1]  # Makes sure the call to change position is capital
            pieces_on_board = self._game_pieces

            if pieces_on_board[current_position] is isinstance(pieces_on_board[current_position], King):  # Checks if current piece is a king
                for positions in pieces_on_board:  # checks if any pieces potential position will land on the same position as the kings new position
                    pieces_on_board[positions].calc_potential_position()
                    print("TEST 1, King cannot move")
                    if new_position in pieces_on_board[positions].get_potential_positions() and pieces_on_board[new_position].get_color() != pieces_on_board[positions].get_color():
                        return False

                if new_position in pieces_on_board:  # Checks if new_position key is in pieces_on_board dict, if a piece is already there
                    print("TEST 2")
                    if new_position in pieces_on_board[new_position].get_potential_positions():  #
                        return False

            if current_position in pieces_on_board:  # If the current position is the position of a game piece
                if self._game_pieces[current_position].get_color() != self._colors_turn:
                    print("Not the right Color")
                    return False
                print("TEST 3")
                pieces_on_board[current_position].calc_potential_position(pieces_on_board)  # Calculate the potential positions of that piece
                potential_positions = pieces_on_board[current_position].get_potential_positions()  # Gets potential position dict
                print("TEST 3.5, Pot Pos", potential_positions)
                if new_position in potential_positions:  # If new_position is in potential_positions
                    row = 0
                    column = 0
                    while row < 8:
                        while column < 8:
                            if new_position == self._chess_board[row][column]:  # Finds the row and column of new_position
                                print("TEST 4, new_position found")
                                if new_position in pieces_on_board:  # Checks if another piece has this location
                                    # Checks if new_position will land on a king, if so it cannot make the move
                                    if pieces_on_board[new_position] is isinstance(pieces_on_board[current_position], King):
                                        print("Test 5, Landed on a King")
                                        return False
                                    # Checks if colors do not match, and takes piece, Capture
                                    elif not pieces_on_board[current_position].check_color(row, column, pieces_on_board):
                                        print("Test 6, Capture")
                                        set_new_pos = self._chess_board[row][column]
                                        pieces_on_board[current_position].set_position(set_new_pos, row, column)
                                        pieces_on_board[new_position] = pieces_on_board[current_position]
                                        pieces_on_board.pop(current_position)
                                        print("TEST 6.5, PIECES ON BOARD", self._game_pieces)
                                        self.update_chess_board()
                                        self.update_game_state()
                                        self.change_color()
                                        return True
                                    else:
                                        return False
                                else:  # If new pos is empty of piece
                                    print("TEST 7, Move to an empty space on the board")
                                    set_new_pos = self._chess_board[row][column]
                                    pieces_on_board[current_position].set_position(set_new_pos, row, column)
                                    pieces_on_board[new_position] = pieces_on_board[current_position]
                                    pieces_on_board.pop(current_position)
                                    print("TEST 7.5, PIECES ON BOARD", self._game_pieces)
                                    self.update_chess_board()
                                    self.update_game_state()
                                    self.change_color()
                                    return True

                                # Stop loop
                                row = 8
                                column = 8
                            else:
                                column += 1
                        column = 0
                        row += 1
                else:
                    return False
            else:
                print("Piece is not on board")
                return False
        else:
            return False


def main():
    """Main function of program to play game and check functionality"""
    game = ChessVar()
    game.update_chess_board()

    while game.get_game_state() == "UNFINISHED":
        print(game.get_empty_chess_board(), "\n")
        print(game.get_color() + "'s turn")
        input_1 = str(input("What location would you like to move?\n"))
        input_2 = str(input("Where would you like to move it?\n"))
        print(game.make_move(input_1, input_2))


if __name__ == "__main__":
    main()
