from flask import Flask, render_template, flash, redirect, render_template, request, session, url_for
import ttt

app = Flask(__name__)


@app.route('/')
def tictactoe():
    """Display board for given state and move"""
    input = request.args.get("input", "")
    cur_board = request.args.get("state", "")

    board = ttt.initialise_state(cur_board)
    free = ttt.make_list_of_free_fields(board)

    if len(free) == 9:
        winner = ttt.comp_turn(board)
        return render_template('/ttt.html', board=board, free=free, input=input, state=ttt.board_to_str(board), winner=winner)

    if input:
        board = ttt.player_move(input, board)
        winner = ttt.winner_checker(board, 'O') # TODO Use the PLAYER_* constants

    if input and winner is None:
        winner = ttt.comp_turn(board)

    return render_template('/ttt.html', board=board, state=ttt.board_to_str(board), free=free, input=input, winner=winner)
