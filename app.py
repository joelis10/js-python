from flask import Flask, render_template, flash, redirect, render_template, request, session, url_for
import ttt

app = Flask(__name__)


@app.route('/', methods=("GET", "POST"))
def tictactoe():
    """Display board for given state and move"""
    input = request.args.get("input", "")
    cur_board = request.args.get("state", "")

    board = ttt.initialise_state(cur_board)
    free = ttt.make_list_of_free_fields(board)
    result = None

    if len(free) == 9:
        # New game, so computer goes first, player has not taken a turn yet
        board = ttt.comp_turn(board)
    else:
        # Player takes a turn
        if input:
            board = ttt.player_move(input, board)
            result = ttt.check_result(board)

        if input and result is None:
            board = ttt.comp_turn(board)
            result = ttt.check_result(board)

    template = '/new/form.html'
    if result == ttt.GAME_TIE:
        template = '/new/tie.html'
    elif result:
        template = '/new/win.html'

    return render_template(
        template,
        board=board,
        state=ttt.board_to_str(board),
        free=free,
        input=input,
        result=result
    )
