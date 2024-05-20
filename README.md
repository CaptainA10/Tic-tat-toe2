Coursework Paper


1. Introduction


In the context of this coursework, the main objective is to explore and put into practice the concepts of object-oriented programming through the development of a classic game: tic-tac-toe, also known as noughts and crosses. This simple yet engaging game provides an excellent playground for understanding fundamental programming principles such as object modeling, state management, and user interaction.

a.Topic Description 

Tic-tac-toe is a two-player board game where the goal is to align three of one's symbols (X or O) on a 3x3 grid. Players take turns placing their symbol in an empty cell each turn. The first player to align three of their symbols horizontally, vertically, or diagonally wins the game. If the grid fills up without either player achieving three in a row, the game is declared a draw.

In this project, we have implemented the tic-tac-toe game using the Python programming language. We have adopted an object-oriented approach to structure our code, with distinct classes to represent the game board, human players, computer players, and the game itself.

b. How to run the program?

To run the program, ensure you have Python installed on your system. Then, simply execute the Python script using the following command in your terminal:


Make sure you are in the directory where the Python file is located. This will launch the game and open a graphical window where you can play tic-tac-toe.

c. How to use the program?

Once the game is launched, you will see a 3x3 game grid with empty cells. You will play against the computer as the X player. Click on an empty cell to place your symbol. The computer will then make its move as the O player. Alternate your moves with the computer until one player aligns three of their symbols or the grid fills up. If a player wins, a dialog box will appear to announce the result of the game. You can also restart the game at any time by clicking the "Restart" button.

2. Body/Analysis
a.Explanation of functional requirements
The program implements the core functionalities of a tic-tac-toe game, including allowing two players to take turns placing their symbols, determining the winner or a draw, providing a graphical user interface for user interaction, and supporting single-player gameplay against a computer opponen

Program Structure

The program follows a modular structure, utilizing object-oriented programming (OOP) principles to organize its components. The key classes include:

- Board: Represents the game board and handles operations related to the board, such as displaying the board, updating cell values, checking for a winner, and determining if the board is full.
- Player: An abstract class representing a player in the game, with subclasses for HumanPlayer and ComputerPlayer, each implementing their own logic for making moves.
- TicTacToe: Manages the game flow, including player turns, user interface, and game state management.
- PlayerFactory: A factory class for creating different types of players based on the input symbol.

Implementation Overview

Object-Oriented Design

The program effectively utilizes OOP concepts to encapsulate data and behavior within classes. This promotes code reusability, maintainability, and readability. For example, the separation of concerns between the Board class and the Player classes allows for clear and modular implementation of game logic.

Graphical User Interface (GUI)

The program employs the Tkinter library to create a graphical user interface for the tic-tac-toe game. Buttons are used to represent the game board, providing an intuitive way for players to interact with the game. The GUI enhances the user experience and facilitates gameplay.

Player Logic

The program implements both human and computer players, allowing for single-player gameplay against an AI opponent. Human players interact with the GUI to make moves by clicking on the game board, while computer players employ algorithms to make intelligent moves based on the current game state.

Game State Management

The program includes functionality for saving and loading the game state using JSON serialization. This feature allows players to save their progress and resume gameplay at a later time, enhancing the overall user experience and adding replayability to the game.

Code Snippets
Example 1: Board Class (board.py)

class Board:
    def __init__(self):
        self.cells = [str(i) for i in range(1, 10)]

    def display(self):
        # Code to display the game board
        pass

    def update(self, move, symbol):
        # Code to update the board with a player's move
        Pass


Example : TicTacToe Class (tic_tac_toe.py)
class TicTacToe:
    def __init__(self, player_factory):
        self.board = Board()
        self.players = [player_factory.create_player('X'), player_factory.create_player('O')]
        self.current_player_idx = 0
        # Code for GUI initialization and event handling

    def play(self):
        # Main game loop
        pass

    def restart_game(self):
        # Code to reset the game state
        pass

Sure! Let's go through the key object-oriented programming (OOP) pillars with examples from your Tic Tac Toe game code, along with brief explanations on how each pillar is used.

About the usage of POO piliars:

1. Classes and Objects

Definition:
- Class: A blueprint for creating objects that defines a set of attributes and methods.
- Object: An instance of a class.

Usage in the code:
In the Tic Tac Toe game, classes are used to represent the game, the board, and players. Objects are instances of these classes created to start and manage the game.

Code Example:


class TicTacToe:
    def __init__(self, player_factory):
        self.board = Board()
        self.players = [player_factory.create_player('X'), player_factory.create_player('O')]
        self.current_player_idx = 0
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

# Creating objects (instances of the class)
human_player_factory = HumanPlayerFactory()
game = TicTacToe(human_player_factory)
```

Here, `TicTacToe` is a class, and `game` is an object (instance) of the `TicTacToe` class.

2. Encapsulation and Access Control

Definition:
- Encapsulation: Bundling data with methods that operate on that data.
- Access Control: Restricting access to certain components using access specifiers like private, protected, and public.

Usage in the code:
Encapsulation is used to hide the internal representation of the board and control access to it via methods.

Code Example:


class Board:
    def __init__(self):
        self.__grid = [['' for _ in range(3)] for _ in range(3)]  # Private attribute

    def reset(self):
        self.__grid = [['' for _ in range(3)] for _ in range(3)]

    def get_grid(self):
        return self.__grid

    def set_cell(self, x, y, value):
        if self.__grid[x][y] == '':
            self.__grid[x][y] = value
        else:
            print("Cell already occupied")

board = Board()
board.set_cell(0, 0, 'X')
print(board.get_grid())


The `__grid` attribute is encapsulated within the `Board` class, and access to it is controlled through methods like `set_cell` and `get_grid`.

3. Method Overloading and Overriding

Definition:
- Method Overloading: Defining multiple methods in a class with the same name but different parameters.
- Method Overriding: Redefining a method in a subclass that is already defined in its superclass.

Usage in the code:
Method overriding is used to provide specific implementations for the `make_move` method in `HumanPlayer` and `ComputerPlayer` classes.

Code Example


class Player:
    def make_move(self, board):
        pass

class HumanPlayer(Player):
    def make_move(self, i, j, board):
        if board.get_grid()[i][j] == '':
            board.set_cell(i, j, self.symbol)

class ComputerPlayer(Player):
    def make_move(self, board):
        for i in range(3):
            for j in range(3):
                if board.get_grid()[i][j] == '':
                    board.set_cell(i, j, self.symbol)
                    return

human_player = HumanPlayer()
computer_player = ComputerPlayer()


In this example, `make_move` is overridden in both `HumanPlayer` and `ComputerPlayer` to provide specific behavior for each type of player.

4. Composition and Aggregation

Definition:
- Composition: A strong form of association where the composed objects cannot exist independently.
- Aggregation: A weaker form of association where the aggregated objects can exist independently.

Usage in the code:
Composition is used to indicate that a `TicTacToe` game consists of a `Board` and players, while aggregation is used to indicate that `PlayerFactory` and its subclasses create players that can exist independently of the game.

Code Example:


# Composition
class TicTacToe:
    def __init__(self, player_factory):
        self.board = Board()  # Composition
        self.players = [player_factory.create_player('X'), player_factory.create_player('O')]
        self.current_player_idx = 0
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

# Aggregation
class PlayerFactory:
    def create_player(self, symbol):
        pass

class HumanPlayerFactory(PlayerFactory):
    def create_player(self, symbol):
        return HumanPlayer(symbol)

class HumanPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

# Here, HumanPlayerFactory and HumanPlayer exist independently but are used together in TicTacToe


5. Polymorphism and Interfaces

Definition:
- Polymorphism: The ability of different objects to be treated as instances of the same class through a common interface.
- Interfaces: A group of related methods with empty bodies.

Usage in the code:
Polymorphism is used to treat different types of players (human or computer) through a common interface defined by the `Player` class.

**Code Example:**

Polymorphism
class Player:
    def make_move(self, board):
        pass

class HumanPlayer(Player):
    def make_move(self, board):
        print("Human player makes a move")

class ComputerPlayer(Player):
    def make_move(self, board):
        print("Computer player makes a move")

players = [HumanPlayer(), ComputerPlayer()]

for player in players:
    player.make_move(None)  # Output will be different based on the type of player

# Interface (abstract base class)
from abc import ABC, abstractmethod

class PlayerFactory(ABC):
    @abstractmethod
    def create_player(self, symbol):
        pass

class HumanPlayerFactory(PlayerFactory):
    def create_player(self, symbol):
        return HumanPlayer(symbol)

class ComputerPlayerFactory(PlayerFactory):
    def create_player(self, symbol):
        return ComputerPlayer(symbol)
```

In this example, polymorphism allows us to use the `make_move` method on any `Player` object, regardless of whether it is a `HumanPlayer` or `ComputerPlayer`.

6. Design Patterns

Definition:
- Design patterns are typical solutions to common problems in software design. They are like blueprints that can be customized to solve particular design problems in your code.

Decorator

Decorator: Allows behavior to be added to an individual object, dynamically, without affecting the behavior of other objects from the same class.

Usage in the code:
A decorator is used to add functionality for showing game-over messages.

Code Example:


def show_game_over_message(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if result:
            self.show_message(result)
    return wrapper

class TicTacToe:
    def __init__(self, player_factory):
        # Initialization code...
        pass

    @show_game_over_message
    def check_winner(self):
        # Code to check for a winner
        pass

    def show_message(self, message):
        messagebox.showinfo("Game Over", message)


In this example, the `show_game_over_message` decorator adds the functionality to display a message when the game is over.

By using these pillars of OOP and design patterns, the Tic Tac Toe game code is structured, maintainable, and extendable.
Meeting Objectives and Requirements

The program effectively meets the defined objectives and functional requirements by implementing the core functionalities of a tic-tac-toe game, including:

- Allowing two players to take turns placing their symbols on the game board.
- Implementing game logic to determine the winner or a draw.
- Providing a graphical user interface for user interaction.
- Supporting single-player gameplay against an AI opponent.
- Including functionality for saving and loading game state.

The modular and object-oriented design of the program promotes extensibility and maintainability, allowing for easy modification or extension of features in the future.
*





3. Results and Summary

a. Results
The implementation of the tic-tac-toe game achieved the desired functionality, with players able to play against each other or against a computer opponent. Challenges were faced during the implementation of the computer player's logic and ensuring smooth integration between the GUI and the game logic.
b. Summary (Conclusions)
In conclusion, the coursework successfully achieved its objectives of implementing a tic-tac-toe game and providing a playable user interface. Future prospects for the program include implementing additional features such as multiplayer functionality, and optimizing the user interface for different platforms.

c. Future Prospects

- The implementation of the tic-tac-toe game achieved the desired functionality, allowing players to play against each other or against a computer opponent.
- Challenges were encountered during the implementation of the computer player's logic, particularly in designing an efficient algorithm for making intelligent moves.
- The graphical user interface (GUI) provided an intuitive way for players to interact with the game, but ensuring smooth integration between the GUI and the underlying game logic required careful consideration and testing.
- Overall, the implementation successfully met the objectives of the coursework, although refining the AI player's strategy and optimizing the GUI for better user experience could be areas for further improvement.


Conclusions

In conclusion, this coursework has successfully achieved its objectives of implementing a tic-tac-toe game using object-oriented programming principles and providing a graphical user interface for player interaction. The program allows players to enjoy the classic game either against each other or against a computer opponent. Through the implementation process, key insights were gained into the application of OOP concepts in game development, as well as the challenges involved in designing efficient player strategies and integrating them with a user-friendly interface.

Key Findings and Outcomes

- The program provides an effective demonstration of object-oriented design principles, modular code organization, and graphical user interface development.
- The resulting program offers a playable and enjoyable tic-tac-toe experience, fulfilling the coursework objectives.
- Future prospects for the program include potential enhancements such as refining the computer player's AI algorithm to improve gameplay experience, implementing additional features such as multiplayer online functionality, and optimizing the user interface for different platforms and devices.

Overall, this coursework has provided valuable hands-on experience in software development, reinforcing concepts learned in class and enhancing skills in programming, problem-solving, and project management.

