import unittest
from tictactoe import Board, TicTacToe, HumanPlayerFactory

class TestTicTacToe(unittest.TestCase):

    def test_board_update(self):
        board = Board()
        board.update(0, 0, 'X')
        self.assertEqual(board.cells[0][0], 'X')

    def test_board_is_winner(self):
        board = Board()
        board.cells = [['X', 'X', 'X'], ['', '', ''], ['', '', '']]
        self.assertTrue(board.is_winner('X'))

    def test_board_is_full(self):
        board = Board()
        board.cells = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
        self.assertTrue(board.is_full())

    def test_on_button_click(self):
        game = TicTacToe(HumanPlayerFactory())
        game.on_button_click(0, 0)
        self.assertEqual(game.buttons[0][0]["text"], "X")

    def test_restart_game(self):
        game = TicTacToe(HumanPlayerFactory())
        game.on_button_click(0, 0)
        game.restart_game()
        self.assertEqual(game.buttons[0][0]["text"], "")

    def test_validate_move(self):
        game = TicTacToe(HumanPlayerFactory())
        @validate_move
        def mock_on_button_click(self, i, j):
            return "Clicked"
        result = mock_on_button_click(game, 0, 0)
        self.assertEqual(result, "Clicked")

    def test_show_game_over_message(self):
        game = TicTacToe(HumanPlayerFactory())
        @show_game_over_message
        def mock_game_over(self, message):
            return "Game Over"
        result = mock_game_over(game, "Player X wins!")
        self.assertEqual(result, "Game Over")

if __name__ == '__main__':
    unittest.main()

