from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'ThisIsASecret'

@app.route('/')
def index():

    # if no counter has been set up, create it and set equal to 1
    if 'counter' not in session:
        session['counter'] = 1

    else:

        try:
            # check if need to add 2 to counter
            if session['add'] == 2:
                session['counter'] += session['add']
                session['add'] = 0 # reset this to 0

            # check if need to reset counter
            elif session['reset'] == True:
                session['counter'] = 1
                session['reset'] = False # reset this to False

            else:
                session['counter'] += 1 # if regular visit to site, just add 1

        except:
            session['counter'] += 1 # exception, regular visit to site, just add 1 to counter

    return render_template('index.html')


@app.route('/add_counter', methods=['POST'])
def add():

    session['add'] = 2

    return redirect('/')


@app.route('/reset_counter', methods=['POST'])
def reset():

    session['reset'] = True

    return redirect('/')

app.run(debug=True)
