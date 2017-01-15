from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)

app.secret_key = "someSecretKeysdfasdf"

@app.route('/')
def index():

    # start with 0 gold
    if 'gold' not in session:
        session['gold'] = 0

    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process_money():

    if request.form['building'] == 'farm':

        gold = random.randint(10,20)
        session['gold'] += gold
        text = ("Earned {} golds from the farm! ({})".format(gold, datetime.now().strftime('%Y/%m/%d %I:%M %p').lower()), 'green')

    elif request.form['building'] == 'cave':

        gold = random.randint(5,10)
        session['gold'] += gold
        text = ("Earned {} golds from the cave! ({})".format(gold, datetime.now().strftime('%Y/%m/%d %I:%M %p').lower()), 'green')

    elif request.form['building'] == 'house':

        gold = random.randint(2,5)
        session['gold'] += gold
        text = ("Earned {} golds from the house! ({})".format(gold, datetime.now().strftime('%Y/%m/%d %I:%M %p').lower()), 'green')

    elif request.form['building'] == 'casino':

        gamble = random.randint(0,1)

        if gamble == 0: # you loose gold
            gold = random.randint(0,50)
            session['gold'] -= gold
            text = ("Entered a casino and lost {} golds... Ouch.. ({})".format(gold, datetime.now().strftime('%Y/%m/%d %I:%M %p').lower()), 'red')

        else: # you win gold

            gold = random.randint(0,50)
            session['gold'] += gold
            text = ("Entered a casino and won {} golds... Yea.. ({})".format(gold, datetime.now().strftime('%Y/%m/%d %I:%M %p').lower()), 'green')


    # try to append tuple (text, css styling red or green) to activities list
    try:
        session['activities'].append(text)


    # if no activities list yet, create the list and then append the tuple
    except:
        session['activities'] = []
        session['activities'].append(text)

    # create a copy of the activities list and reverse it for display to user (most current time and activity listed at top)
    session['reverse_activities'] = list(session['activities'])
    session['reverse_activities'].reverse()

    return redirect('/')


app.run(debug=True)
