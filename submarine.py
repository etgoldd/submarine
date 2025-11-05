from random import randint


INTRO_TEXT = """
Welcome to submarine game!
Somewhere on a 10x10 grid a submarine has appeared!
You get infinite guesses to guess where the sub is!
Guesses are of the form \"X,Y\" (without the quotes)
Good luck!

"""
BAD_FORMAT_TEXT = "Guesses are of the form \"X,Y\" where X and Y are the corresponding integer coordinates, try again!"
BOARD_START = 1
BOARD_END = 10
CLOSE_DISTANCE = 1


class GuessException(Exception):
    pass


def get_player_guess() -> tuple[int, int]:
    """
    Handles user input and returns the corresponding vector.
    If failed to do so, returns an error value.
    """
    player_input = input("Take your shot!\n")
    player_coords_str = player_input.split(",")
    if len(player_coords_str) != 2:
        raise GuessException
    try:
        player_guess = (int(player_coords_str[0]), int(player_coords_str[1]))
    except Exception:
        raise GuessException
    x, y = player_guess[0], player_guess[1]
    if BOARD_START <= x <= BOARD_END and BOARD_START <= y <= BOARD_END:
        return player_guess
    raise GuessException


def get_abs_diff(coords1: tuple[int, int], coords2: tuple[int, int]) -> tuple[int, int]:
    """
    Gets the distance vector between the two given coordinates
    """
    return abs(coords1[0] - coords2[0]), abs(coords1[1] - coords2[1])


def is_close(coords1: tuple[int, int], coords2: tuple[int, int]) -> bool:
    """
    Returns True if the two vectors are within <CLOSE_DISTANCE> squares (including diagonally) of each other
    """
    diff_x, diff_y = get_abs_diff(coords1, coords2)
    return diff_x <= CLOSE_DISTANCE and diff_y <= CLOSE_DISTANCE


def is_aligned(coords1: tuple[int, int], coords2: tuple[int, int]) -> bool:
    """
    Returns True if the two vectors share a coordinate
    """
    diff_x, diff_y = get_abs_diff(coords1, coords2)
    return diff_x == 0 or diff_y == 0


def main() -> None:
    guesses = 1
    sub_loc = (randint(BOARD_START, BOARD_END), randint(BOARD_START, BOARD_END))
    print(INTRO_TEXT)
    while True:
        try:
            guess = get_player_guess()
        except GuessException:
            print(BAD_FORMAT_TEXT)
            continue
        if guess == sub_loc:
            print("Right on!")
            break
        if is_close(guess, sub_loc):
            print("Close")
        elif is_aligned(guess, sub_loc):
            print("Interesting...")
        else:
            print("Keep thinking")
        guesses += 1
    print(f"You win!!! You hit the sub after: {guesses} guesses")


if __name__ == '__main__':
    main()
