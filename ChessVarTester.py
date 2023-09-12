from ChessVar import *
import unittest


class TestChessVar(unittest.TestCase):
    """A test class wrote simultaneously as Program ChessVar is written. This test class is used check the
    initialization of the game pieces, the board, and tests the position changes for each game piece. This class will
    also test for the status of the game, and if the moves are valid, and whose turn it is"""

    def test_1(self):
        """Tests the initialization of Position"""
        pos = Position(3, 4)
        self.assertEqual(pos.get_row(), 3)
        self.assertEqual(pos.get_column(), 4)

    def test_2(self):
        """Tests ChessVar self._chess_board, a 2D list that represents the chessboard. This is to make sure there is an
        understanding of how to access the index and cell info"""
        chess_board_init = ChessVar()
        chess_board = chess_board_init.get_chess_board()
        self.assertEqual(chess_board[7][0], "A1")
        self.assertEqual(chess_board[7][7], "H1")

    def test_3(self):
        """Tests class King calc_potential_position and make_move"""
        chess_board_init = ChessVar()
        game_pieces = chess_board_init.get_game_pieces()
        # print(game_pieces[0].get_position().get_pos_name())
        game_pieces["A1"].set_position("D6", 5, 3)
        game_pieces["D6"] = game_pieces["A1"]
        game_pieces.pop("A1")
        game_pieces["D6"].calc_potential_position()
        potential_pos_1 = game_pieces["D6"].get_potential_positions()
        print("TEST 1", potential_pos_1)

        # REMOVE OR REDO TESTS
        # Doesn't execute on purpose because in the start position the piece is surrounded by other pieces
        for key in potential_pos_1:
            if key == "D5":  # Doesn't execute on purpose
                self.assertEqual(potential_pos_1[key].get_pos_name(), "D5")
            elif key == "C6":
                self.assertEqual(potential_pos_1[key].get_pos_name(), "C6")

    def test_4(self):
        """Tests class Bishop calc_potential_position and make_move"""
        chess_board_init = ChessVar()
        game_pieces = chess_board_init.get_game_pieces()

        game_pieces["G2"].calc_potential_position()
        potential_pos_1 = game_pieces["G2"].get_potential_positions()
        print(potential_pos_1)
        for key in potential_pos_1:
            if key == "H8":
                self.assertEqual(potential_pos_1[key].get_pos_name(), "H8")

        print("POTENTIAL POSITIONS")
        for key in potential_pos_1:
            print(potential_pos_1[key].get_pos_name())

    def test_5(self):
        """Tests class Rook calc_potential_position and make_move"""
        chess_board_init = ChessVar()
        game_pieces = chess_board_init.get_game_pieces()

        game_pieces["A2"].calc_potential_position(game_pieces)
        potential_pos_1 = game_pieces["A2"].get_potential_positions()
        print(potential_pos_1)
        for key in potential_pos_1:
            if key == "A8":
                self.assertEqual(potential_pos_1[key].get_pos_name(), "A8")

        move_piece = chess_board_init.make_move("A2", "B8")
        self.assertEqual(move_piece, False)

        print("POTENTIAL POSITIONS")
        for key in potential_pos_1:
            print(potential_pos_1[key].get_pos_name())
