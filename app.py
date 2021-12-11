from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def helloWorld():  # put application's code here
    return 'Hey everyone!'


@app.route('/homepage')
def comeHome():
    return redirect('/home')


@app.route('/articles')
def goToArticles():
    return 'This is the articles page'


@app.route('/AlonHalevi')
def halevialon():
    return redirect(url_for('goToArticles'))


if __name__ == '__main__':
    app.run(debug=True)