from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/settings/', methods=['POST'])
def render_settings() -> str:
    return str(render_template('settings.html', the_title='数字当てゲームの初期設定'))


@app.route('/entry/')
def render_entry() -> str:
    return str(render_template('entry.html', the_title='数字当てゲームスタート！'))


@app.route('/result_right/')
def render_result_right() -> str:
    return str(render_template('result_right.html', the_title='正解！'))


@app.route('/result_continue/')
def render_result_continue() -> str:
    return str(render_template('result_continue.html', the_title='再チャレンジ！'))


@app.route('/result_finally/')
def render_result_finally() -> str:
    return str(render_template('result_finally.html', the_title='答え合わせ'))


@app.route('/entry_on_the_text/')
def render_entry_on_the_text() -> str:
    return str(render_template('entry_on_the_text.html', the_title='動作確認'))


app.run(debug=True)
