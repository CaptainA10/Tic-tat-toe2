import csv
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

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
        self.cells = [['' for _ in range(3)] for _ in range(3)]

    def update(self, i, j, symbol):
        if self.cells[i][j] == '':
            self.cells[i][j] = symbol
            return True
        return False

    def is_winner(self, symbol):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(self.cells[i][j] == symbol for j in range(3)) or all(self.cells[j][i] == symbol for j in range(3)):
                return True
        if all(self.cells[i][i] == symbol for i in range(3)) or all(self.cells[i][2 - i] == symbol for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(self.cells[i][j] != '' for i in range(3) for j in range(3))

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
            self.save_game(result)
            self.disable_buttons()
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

class TicTacToe:
    def __init__(self, player_factory):
        self.board = Board()
        self.players = [player_factory.create_player('X'), player_factory.create_player('O')]
        self.current_player_idx = 0
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text="", width=10, height=3, font=("Helvetica", 24), command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
        restart_button.grid(row=3, columnspan=3)

        # Create CSV file if it doesn't exist
        with open("tictactoe_games.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Game State", "Winner"])

    @validate_move
    @show_game_over_message
    def on_button_click(self, i, j):
        current_player = self.players[self.current_player_idx]
        if self.board.update(i, j, current_player.symbol):
            self.buttons[i][j]["text"] = current_player.symbol
            if self.board.is_winner(current_player.symbol):
                return f"{current_player.symbol} is the winner"
            elif self.board.is_full():
                return "Draw"
            self.current_player_idx = (self.current_player_idx + 1) % 2
        return None

    def restart_game(self):
        self.board = Board()
        for row in self.buttons:
            for button in row:
                button["text"] = ""
                button["state"] = tk.NORMAL

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button["state"] = tk.DISABLED

    def show_message(self, message):
        messagebox.showinfo("Game Over", message)

    def save_game(self, result):
        with open("tictactoe_games.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), "Game Over", result])

if __name__ == "__main__":
    human_player_factory = HumanPlayerFactory()
    game = TicTacToe(human_player_factory)
    game.root.mainloop()
