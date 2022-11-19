from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', current_time = '05 : 30 : 29')

if __name__ == "__main__":
   app.run(debug=True)