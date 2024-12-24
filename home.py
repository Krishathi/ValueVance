from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def welcome():
    return render_template('index.html')
app.run(host='0.0.0.0', debug=True)