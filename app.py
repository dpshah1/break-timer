from flask import Flask, render_template, request, session
import datetime

app = Flask(__name__)

@app.route('/session')
def session():
    return render_template('session.html')

@app.route('/break')
def break_time():
    return render_template('break.html')

app.secret_key = b'dh%$*ruvloga!^)nwils&on('

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        hours = int(request.form["hour_input"])
        minutes = int(request.form["minute_input"])

        play_sound = str(request.form["play_alarm"])
        break_freq = int(request.form["break_freq"])

        print(hours)
        print(minutes)
        print(play_sound)
        print(break_freq)

        current_time = datetime.datetime.now()

        session['end_hour'] = (current_time.hour + hours) % 24
        session['end_minute'] = (current_time.minute + minutes) % 60
        session['end_second'] = (current_time.second)

        session['start_hour'] = (current_time.hour)
        session['start_minute'] = (current_time.minute)
        session['start_second'] = (current_time.second)

        session['duration_hours'] = hours
        session['duration_minutes'] = minutes

        return f"Current time {current_time} \n Task will end at {session['end_hour']} : {session['end_minute']} : {session['end_second']}"

    return render_template('index.html')

if __name__ == "__main__":
   app.run(debug=True)