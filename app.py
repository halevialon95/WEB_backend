from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


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


@app.route('/')
def home():
    return render_template('CV1.html')


@app.route('/contact_us_page')
def contact_us():
    return render_template('CV2.html')


@app.route('/Assignment8')
def assignment_8_page():
    first_name = 'Alon'
    last_name = 'Halevi'
    return render_template('assignment8.html', name=first_name, family_name=last_name,
                           hobbies=('Cheering for Phili76ers', 'Playing Basketball`', 'Hearing Music'))



if __name__ == '__main__':
    app.run(debug=True)