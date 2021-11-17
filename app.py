from flask import Flask, render_template
import game_of_life

app = Flask(__name__)


@app.route('/')
def index_page():
    game_of_life.GameOfLife(width=20, height=20)
    return render_template('index.html')


@app.route('/live')
def live_page():
    game = game_of_life.GameOfLife()
    if game.counter:
        game.form_new_generation()
    game.counter += 1
    return render_template('live.html', game=game)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
