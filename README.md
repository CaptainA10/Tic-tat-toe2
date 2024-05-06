Coursework Paper


1. Introduction


In the context of this coursework, the main objective is to explore and put into practice the concepts of object-oriented programming through the development of a classic game: tic-tac-toe, also known as noughts and crosses. This simple yet engaging game provides an excellent playground for understanding fundamental programming principles such as object modeling, state management, and user interaction.

a.Topic Description 

Tic-tac-toe is a two-player board game where the goal is to align three of one's symbols (X or O) on a 3x3 grid. Players take turns placing their symbol in an empty cell each turn. The first player to align three of their symbols horizontally, vertically, or diagonally wins the game. If the grid fills up without either player achieving three in a row, the game is declared a draw.

In this project, we have implemented the tic-tac-toe game using the Python programming language. We have adopted an object-oriented approach to structure our code, with distinct classes to represent the game board, human players, computer players, and the game itself.

b. How to run the program?

To run the program, ensure you have Python installed on your system. Then, simply execute the Python script using the following command in your terminal:
```

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


Example 2: TicTacToe Class (tic_tac_toe.py)
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

