"""Simple tests for Tictactoe functions.

Use pytest to run these tests.
"""
import ttt


BOARD_BLANK = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

BOARD_FINAL_X = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 'X'],
]

BOARD_FINAL_ALTERNATES = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['X', 'O', 'X'],
]


def test_initialise_board():
    """Test that a blank board has the right content."""
    assert ttt.initialise_state() == BOARD_BLANK, "Expect a blank board"


def test_board_to_str_blank():
    assert ttt.board_to_str(BOARD_BLANK) == "123456789"


def test_str_to_board_empty_string():
    assert ttt.str_to_board("") == BOARD_BLANK


def test_str_to_board_blank():
    assert ttt.str_to_board("123456789") == BOARD_BLANK


def test_str_to_board_gibberish():
    assert ttt.str_to_board("Ilovecatsbutnotdogs") == BOARD_BLANK


def test_str_to_board_x9():
    assert ttt.str_to_board("        X") == BOARD_FINAL_X


def test_str_to_board_alternates():
    assert ttt.str_to_board("XOXOXOXOX") == BOARD_FINAL_ALTERNATES


def test_get_move():
    assert ttt.get_move(BOARD_BLANK, 1) == 1

def test_get_move_2():
    assert ttt.get_move(BOARD_BLANK, 2) == 2
