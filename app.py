from flask import Flask, render_template, request, session, redirect, url_for
import datetime
from flask_sqlalchemy import SQLAlchemy
from timer import *
import random
from sqlalchemy import create_engine, MetaData, Table, Column, select, insert, and_, update, delete
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = "d#$hr^uvl)og*an(wil$so#n"

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(800), nullable=False)
    video_link = db.Column(db.String(200), nullable=False)

@app.before_first_request
def create_tables():
    db.create_all()

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

        session['work_duration'] = break_freq

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
        session['poses_done'] = 0
        return redirect('/break')

    time = long_timer(session['end_hour'], session['end_minute'], session['end_second'])
    short_time = short_timer(session['break_hour'], session['break_minute'], session['break_second'])
    return render_template('session.html', time=time, short_time=short_time, long_percentage=percent(session['duration_hours'], session['duration_minutes'], Time(session['start_hour'], session['start_minute'], session['start_second'])))

@app.route('/break')    
def break_page():
    all_entries = [["Childs pose","Kneel on a yoga mat with legs together and slowly sit back onto heels. Extend torso up and bend forward from the hips so your chest rests on your thighs and your forehead rests on the ground in front of you. Let shoulders curl around and rest hands next to your feet with your palms up. Hold this position for 5 6 breaths.","https://www.youtube.com/watch?v=qYvYsFrTI0U&ab_channel=ViveHealth"],
["Standing forward fold pose","From your standing position bend your knees and hinge forward from your hips reaching your hands for your toes. Remember to exhale as you fold to get a better stretch. Hold this position for 5 breaths then slowly rise back up.","https://www.youtube.com/watch?v=oy2AfcI1CXA&ab_channel=OnnitAcademy"],
["Eagle pose","Garudasana (Eagle Pose) requires careful focus. You must bend your knees cross your left thigh over your right hook the top of your foot behind your right calf spread the scapula and snug your right elbow into the crook of your left bring your palms to touch lift your elbows and stretch your fingers towards the ceiling.","https://www.youtube.com/watch?v=fC9XQWc6ukk&ab_channel=Howcast"]]
    current_time = datetime.datetime.now()

    if(int(session['poses_done']) >= 2):
        session['poses_done'] = 0
        session['break_hour'] = current_time.hour + 1 if current_time.hour + int(session['work_duration']) > 59 else current_time.hour
        session['break_minute'] = (current_time.minute + int(session['work_duration'])) % 60
        session['break_second'] = current_time.second
        return redirect('/session')
        
    
    yoga_id = random.randint(0, 2)
    print(yoga_id)
    yoga1 = all_entries[yoga_id]

    session['poses_done'] = int(session['poses_done']) + 1

    print(yoga1)
    return render_template('break.html', yoga1=yoga1, pose = yoga1[0], description=yoga1[1], video_link=yoga1[2])

if __name__ == "__main__":
   app.run(debug=True)