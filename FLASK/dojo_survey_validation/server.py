from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)

app.secret_key = "l;xcl;adsf;lkjewipjjajsdf;;jasdioinhuuh43haisdnnv"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():



    # validate: name can not be blank
    if len(request.form['name']) < 1 :
        flash('Name can not be blank')
        name = ""

    else:
        name = request.form['name']

    # validate: comment can not be more than 120 characters
    if len(request.form['comment']) > 120:
        flash('Your comment was: {} characters long.  Please shorten your comment to be less than 120 characters'.format(len(request.form['comment'])))
        comment = ""
        for num in range(121):
            comment+=request.form['comment'][num]

        comment+="..."

    else:
        comment = request.form['comment']

    dojo = request.form['dojo']
    language = request.form['language']

    # store form date before rendering
    return render_template('result.html', name=name, dojo=dojo, language=language, comment=comment)

app.run(debug=True)
