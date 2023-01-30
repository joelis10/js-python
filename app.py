from flask import Flask, request, render_template
import tictactoe

app = Flask(__name__)

@app.route('/')
def main():
    input = request.args.get("input", "")
    return (
        """
        <form method="get">
            <input type="text" name="input" placeholder="Enter a name">
        </form>
        """ + "Hello, " + input
    )


@app.route('/tictactoe/')
def ttt():

    board = tictactoe.initialiseState()
    freeSpaces = tictactoe.calculateSpaces(board)
    turns = 4

    while len(freeSpaces):
        input = request.args.get("input", "")

        if input:
            tictactoe.enterMove(board, input)
            render_template('python.html', board=board, freeSpaces=freeSpaces, input=input, overallWinner=overallWinner)
        else:
            return render_template('python.html', board=board, freeSpaces=freeSpaces, input=input)
