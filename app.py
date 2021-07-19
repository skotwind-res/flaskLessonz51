from flask import Flask


app = Flask(__name__)
temp = """
'<a href="/">Main</a>'
'<a href="/start">Start</a>'
"""

@app.route('/')  # 127.0.0.1:5000
def hello_world():
    return '<h2>Main!!</h2>' + temp

@app.route('/start')
def main_page():
    return '<h2>start</h2>' + temp

@app.route('/hello/<name>')
def hello_name(name):
  return 'Hello %s!' % name


if __name__ == '__main__':
    app.run()
