from flask import Flask, render_template, request, session
import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

@app.route('/session')
def session():
    return render_template('session.html')

@app.route('/break')
def break_time():
    return render_template('break.html')

app.secret_key = b'dh%$*ruvloga!^)nwils&on('

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(800), nullable=False)
    video_link = db.Column(db.String(200), nullable=False)

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

def insert():
    e = Exercise("Childs pose", "Kneel on a yoga mat with legs together and slowly sit back onto heels. Extend torso up and bend forward from the hips so your chest rests on your thighs and your forehead rests on the ground in front of you. Let shoulders curl around and rest hands next to your feet with your palms up. Hold this position for 5 – 6 breaths.", "https://www.youtube.com/watch?v=qYvYsFrTI0U&ab_channel=ViveHealth")

if __name__ == "__main__":
   app.run(debug=True)