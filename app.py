from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('index.html', current_time = '05 : 30 : 29')

@app.route('/session')
def session():
    return render_template('session.html')


def timer(end_hour, end_min, end_sec):
    # code to calculate hours, minutes, and seconds left
    print("hello world")

if __name__ == "__main__":
   app.run(debug=True)