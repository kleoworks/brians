from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():

    name = request.form['name']
    dojo = request.form['dojo']
    language = request.form['language']
    comment = request.form['comment']

    # store form date before rendering
    return render_template('result.html', name=name, dojo=dojo, language=language, comment=comment)

    # return redirect('/')

app.run(debug=True)
