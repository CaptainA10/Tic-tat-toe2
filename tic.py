import random
import tkinter as tk
from tkinter import messagebox

class Player:
    def __init__(self, symbol):
        self.symbol = symbol 

    def get_move(self, board):
        pass

class HumanPlayer(Player):
    def get_move(self, board):
        pass

class ComputerPlayer(Player):
    def get_move(self, board):
        pass

class Board:
    def __init__(self):
        # Initialize the board with numbers representing empty cells
        self.cells = [str(i) for i in range(1, 10)]

    def display(self):
        pass

    def update(self, move, symbol):
        pass

    def available_moves(self):
        pass

    def is_winner(self, symbol):
        pass

    def is_full(self):
        pass

class TicTacToe:
    def __init__(self, player_factory):
        # Initialize the game
        self.board = Board()  # Create the game board
        self.players = [player_factory.create_player('X'), player_factory.create_player('O')]  # Create players
        self.current_player_idx = 0  # Index of the current player
        self.root = tk.Tk()  # Create the main window
        self.root.title("Tic Tac Toe")  # Set window title

        # Create buttons for the game board
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                # Create a button with a command linked to on_button_click
                button = tk.Button(self.root, text="", width=10, height=3, font=("Helvetica", 24), command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)  # Position the button in the grid
                row.append(button)
            self.buttons.append(row)

        # Add the "Restart" button
        restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
        restart_button.grid(row=3, columnspan=3)  # Position the "Restart" button

    def on_button_click(self, i, j):
        # Handle click on a button in the game board
        button = self.buttons[i][j]
        if button["text"] == "":
            current_player = self.players[self.current_player_idx]
            button["text"] = current_player.symbol
            self.current_player_idx = (self.current_player_idx + 1) % 2

    def restart_game(self):
        # Reset the game
        self.board = Board()  # Reset the game board
        # Clear button texts
        for row in self.buttons:
            for button in row:
                button["text"] = ""

    def play(self):
        pass

    def show_message(self, message):
        messagebox.showinfo("Game Over", message)

def validate_move(func):
    def wrapper(self, i, j):
        button = self.buttons[i][j]
        if button["text"] == "":
            return func(self, i, j)
        else:
            messagebox.showwarning("Invalid Move", "This position is already occupied!")
    return wrapper

def show_game_over_message(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if result:
            self.show_message(result)
    return wrapper

class PlayerFactory:
    def create_player(self, symbol):
        pass

class HumanPlayerFactory(PlayerFactory):
    def create_player(self, symbol):
        return HumanPlayer(symbol)

class ComputerPlayerFactory(PlayerFactory):
    def create_player(self, symbol):
        return ComputerPlayer(symbol)

if __name__ == "__main__":
    human_player_factory = HumanPlayerFactory()
    computer_player_factory = ComputerPlayerFactory()
    game = TicTacToe(human_player_factory)
    game.root.mainloop()
