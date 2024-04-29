import json

def save_game_state(board_cells, current_player_idx):
    game_state = {
        "board_cells": board_cells,
        "current_player_idx": current_player_idx
    }
    with open("game_state.json", "w") as file:
        json.dump(game_state, file)

def load_game_state():
    try:
        with open("game_state.json", "r") as file:
            game_state = json.load(file)
            return game_state["board_cells"], game_state["current_player_idx"]
    except FileNotFoundError:
        return None, None
