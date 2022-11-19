from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        hours = request.form("hour_input")
        minutes = request.form("minute_input")

        play_sound = request.form("play_alarm")
        break_freq = request.form("break_freq")

        print(hours)
        print(minutes)
        print(play_sound)
        print(break_freq)

    return render_template('index.html')


def timer(end_hour, end_min, end_sec):
    # code to calculate hours, minutes, and seconds left
    print("hello world")

if __name__ == "__main__":
   app.run(debug=True)