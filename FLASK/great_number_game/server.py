from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)

app.secret_key = 'MySecret'

@app.route('/')
def index():

    # set the initial random number per session
    if 'random_num' not in session:
        session['random_num'] = random.randint(1,101)

    try:
        # check the user guess
        # set session['hint'] to display hint to user for help with their next guess
        # if user guessed the correct number, set session['won'] to True, and give the user an option to play again
        if session['guess'] < session['random_num']:
            session['hint'] = 'Too low!'
        elif session['guess'] > session['random_num']:
            session['hint'] = 'Too high!'
        elif session['guess'] == session['random_num']:
            session['won'] = True
    except:
        pass

    return render_template('index.html')


@app.route('/button', methods=['POST'])
def button():


    if 'guess_form' in request.form:

        try:
            # set user guess
            session['guess'] = int(request.form['guess'])

        except:
            # if user submitted no guess (blank submit) or some other non-num input, set guess to 0 which is outside of random num range
            session['guess'] = 0

    elif 'play_again_form' in request.form:
        # user has clicked button to play again, pop all values from session and start all over
        session.pop('guess')
        session.pop('won')
        session.pop('random_num')
        if 'hint' in session:
            session.pop('hint')

    return redirect('/')


app.run(debug=True)
