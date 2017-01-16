from flask import Flask, render_template, redirect

app = Flask(__name__)

show_images=['blue','orange','red','purple']

@app.route('/')
def index():

    # show text, no ninja's here
    return render_template('index.html');


@app.route('/ninja')
def ninja():

    # show all ninja turtles
    return render_template('ninja.html', show_images=show_images)

@app.route('/ninja/<argument>')
def process(argument):

    # show turtle based on color used in url argument
    # if not a valid color (blue, orange, red, purple) then show JUNK
    if argument.lower() not in show_images:
        return render_template('ninja.html', show_images=['junk'])

    elif argument.lower() == "blue":
        return render_template('ninja.html', show_images=['blue'])

    elif argument.lower() == "orange":
        return render_template('ninja.html', show_images=['orange'])

    elif argument.lower() == "red":
        return render_template('ninja.html', show_images=['red'])

    elif argument.lower() == "purple":
        return render_template('ninja.html', show_images=['purple'])

    else:
        return redirect('/')

@app.route('/ninja/')
def invalid_route():

    return redirect('/')

app.run(debug=True)
