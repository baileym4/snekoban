# Snekoban Game

Welcome to the Snekoban Game, a Python implementation. This game involves moving the player through a maze to reach the victory condition while strategically avoiding obstacles and completing the objectives. The player reaches the victory condition when they have collected all of the computers on the board while avoiding the walls. 

## Description

This Python script implements the Snekoban Game. The game state is represented by a dictionary containing the locations of various objects on the board. The game involves a player, computers, targets, and walls. The goal is to move the player to achieve victory by reaching the target locations.
The main code is located in the lab.py file. 

## Functions

### `new_game(level_description)`

**Purpose:** Create a new game representation based on the provided level description.


### `victory_check(game)`

**Purpose:** Check if the current game state satisfies the victory condition.


### `step_game(game, direction)`

**Purpose:** Move the player one step in the specified direction, updating the game state.


### `dump_game(game)`

**Purpose:** Convert the current game state into a level description suitable for new_game.


### `solve_puzzle(game)`

**Purpose:** Find a solution to the puzzle and return the shortest sequence of moves. This function utilizes a BFS algorithm. 

## Usage
To visualize and play the Snekoban game the user can run server.py. This file creates a local server that the user can naviagte to and play on. 

## Testing
The test.py file contains test cases developed by me and the 6.101 MIT course staff. The puzzles, test_inputs, test_levels, test_outputs, and ui folders are used to run the test cases and the server. 
