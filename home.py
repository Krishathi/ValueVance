from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def run_app():
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

thread = Thread(target=run_app)
thread.start()

print("Flask app is running! Open http://127.0.0.1:5000 in your browser.")
