from flask import Flask, render_template, request, session, redirect, url_for
import datetime
from flask_sqlalchemy import SQLAlchemy
from timer import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = "d#$hr^uvl)og*an(wil$so#n"

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(800), nullable=False)
    video_link = db.Column(db.String(200), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        hours = int(request.form.get("hour_input"))
        minutes = int(request.form.get("minute_input"))

        play_sound = str(request.form.get("play_alarm"))
        break_freq = int(request.form.get("break_freq"))

        print(hours)
        print(minutes)
        print(play_sound)
        print(break_freq)

        current_time = datetime.datetime.now()

        session['end_hour'] = ((current_time.hour + hours) % 24)
        session['end_minute'] = ((current_time.minute + minutes) % 60)
        session['end_second'] = (current_time.second)

        session['start_hour'] = (current_time.hour)
        session['start_minute'] = (current_time.minute)
        session['start_second'] = (current_time.second)

        session['duration_hours'] = hours
        session['duration_minutes'] = minutes

        session['break_hour'] = current_time.hour + 1 if current_time.hour + break_freq > 59 else current_time.hour
        session['break_minute'] = (current_time.minute + break_freq) % 60
        session['break_second'] = current_time.second

        return redirect('/session')

    return render_template('index.html')

@app.route('/session')
def session_page():
    current_time = datetime.datetime.now()

    if current_time.hour >= session['end_hour'] and current_time.minute >= session['end_minute'] and current_time.second >= session['end_second']:
        return "session is over, good job"

    if current_time.hour >= session['break_hour'] and current_time.minute >= session['break_minute'] and current_time.second >= session['break_second']:
        return render_template('session.html')

    time = long_timer(session['end_hour'], session['end_minute'], session['end_second'])
    short_time = short_timer(session['break_hour'], session['break_minute'], session['break_second'])
    return render_template('session.html', time=time, short_time=short_time)
    

if __name__ == "__main__":
   app.run(debug=True)