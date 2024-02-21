"""
Snekoban Game
"""

import json
import typing



direction_vector = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1),
}


def new_game(level_description):
    """
    Given a description of a game state, create and return a game
    representation of your choice.

    The given description is a list of lists of lists of strs, representing the
    locations of the objects on the board (as described in the lab writeup).

    For example, a valid level_description is:

    [
        [[], ['wall'], ['computer']],
        [['target', 'player'], ['computer'], ['target']],
    ]

    The exact choice of representation is up to you; but note that what you
    return will be used as input to the other functions.
    """
    height = len(level_description)
    width = len(level_description[0])

    # keys are items values are coords where they are
    coord_dict = {
        "computer": set(),
        "target": set(),
        "player": set(),
        "wall": set(),
        "height": height,
        "width": width,
    }

    num_rows = len(level_description)
    num_col = len(level_description[0])

    # create dictionary
    for x in range(num_rows):
        for y in range(num_col):
            items = level_description[x][y]
            for i in items:
                coord_dict[i].add((x, y))

    return coord_dict


def victory_check(game):
    """
    Given a game representation (of the form returned from new_game), return
    a Boolean: True if the given game satisfies the victory condition, and
    False otherwise.
    """
    # check for no computers or targets
    if len(game["computer"]) == 0:
        return False
    if len(game["target"]) == 0:
        return False
    # check if all targets and computers are in some loc
    return game["computer"] == game["target"]


def step_game(game, direction):
    """
    Given a game representation (of the form returned from new_game), return a
    new game representation (of that same form), representing the updated game
    after running one step of the game.  The user's input is given by
    direction, which is one of the following: {'up', 'down', 'left', 'right'}.

    This function should not mutate its input.
    """
    # create copy of game to not mutate
    update = {}
    for item in game:
        if item not in ("height", "width"):
            update[item] = game[item].copy()
        else:
            update[item] = game[item]

    # determine current, wanted, and additional loc
    player_loc = list(update["player"])[0]
    choice = direction_vector[direction]
    wanted_spot = (player_loc[0] + choice[0], player_loc[1] + choice[1])
    two_step = (wanted_spot[0] + choice[0], wanted_spot[1] + choice[1])

    # check if move is valid and update new game
    if wanted_spot in update["wall"]:
        return update
    elif wanted_spot in update["computer"]:
        if two_step in update["computer"]:
            return update
        elif two_step in update["wall"]:
            return update
        else:
            update["player"].remove(player_loc)
            update["player"].add(wanted_spot)
            update["computer"].remove(wanted_spot)
            update["computer"].add(two_step)
    else:
        update["player"].remove(player_loc)
        update["player"].add(wanted_spot)

    return update


def dump_game(game):
    """
    Given a game representation (of the form returned from new_game), convert
    it back into a level description that would be a suitable input to new_game
    (a list of lists of lists of strings).

    This function is used by the GUI and the tests to see what your game
    implementation has done, and it can also serve as a rudimentary way to
    print out the current state of your game for testing and debugging on your
    own.
    """

    final_game = []
    # generate nested list
    for _ in range(game["height"]):
        new_list = []
        for _ in range(game["width"]):
            extra_list = []
            new_list.append(extra_list)
        final_game.append(new_list)

    # add item to correct list in list of lists
    for item in game:
        if item not in ("width", "height"):
            for coord in game[item]:
                final_game[coord[0]][coord[1]].append(item)

    return final_game


def solve_puzzle(game):
    """
    Given a game representation (of the form returned from new game), find a
    solution.

    Return a list of strings representing the shortest sequence of moves ("up",
    "down", "left", and "right") needed to reach the victory condition.

    If the given level cannot be solved, return None.
    """

    # check if already won
    if victory_check(game):
        return []

    # get intial conditions
    player_loc = list(game["player"])[0]
    computer_locs = frozenset(game["computer"])
    initial = (player_loc, computer_locs)

    agenda = [(tuple(), game)]
    visited = {initial}  # current + computer location

    while agenda:
        this_path = agenda.pop(0)
        terminal_state = this_path[-1]

        # check each direction
        for direction in direction_vector:
            new_state = step_game(terminal_state, direction)
            # if win return path
            if victory_check(new_state):
                return list(this_path[0] + (direction,))
            current_spots = (
                list(new_state["player"])[0],
                frozenset(new_state["computer"]),
            )
            # update agenda and visited
            if current_spots not in visited:
                new_path = this_path[0] + (direction,)
                visited.add(current_spots)
                agenda.append((new_path, new_state))

    return None


if __name__ == "__main__":
    first = [
        [["wall"], ["wall"], ["wall"], ["wall"], ["wall"], [], [], [], [], []],
        [["wall"], [], [], [], ["wall"], ["wall"], ["wall"], ["wall"], ["wall"], []],
        [["wall"], [], [], [], [], [], [], [], ["wall"], []],
        [["wall"], ["wall"], ["wall"], [], ["wall"], [], ["wall"], [], ["wall"], []],
        [[], [], ["wall"], [], ["wall"], [], [], [], ["wall"], []],
        [
            [],
            ["wall"],
            ["wall"],
            ["player"],
            ["wall"],
            ["wall"],
            ["wall"],
            [],
            ["wall"],
            ["wall"],
        ],
        [
            [],
            ["wall"],
            [],
            ["target", "computer"],
            ["target", "computer"],
            ["target", "computer"],
            ["target", "computer"],
            ["target", "computer"],
            [],
            ["wall"],
        ],
        [[], ["wall"], [], [], [], [], [], [], [], ["wall"]],
        [
            [],
            ["wall"],
            [],
            ["wall"],
            ["wall"],
            ["wall"],
            [],
            ["wall"],
            ["wall"],
            ["wall"],
        ],
        [[], ["wall"], [], [], [], [], [], ["wall"], [], []],
        [
            [],
            ["wall"],
            ["wall"],
            ["wall"],
            ["wall"],
            ["wall"],
            ["wall"],
            ["wall"],
            [],
            [],
        ],
    ]
    better = new_game(first)
    # print(victory_check(better))
    pass
