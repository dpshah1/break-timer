import datetime
import time

def long_timer(end_hour, end_min, end_sec):
    cur_time = datetime.datetime.now()
    
    if end_hour < cur_time.hour:
        hours = 24 - cur_time.hour + end_hour
    else:
        hours = end_hour - cur_time.hour
    
    time_remaining = (hours) * 3600 + (end_min - cur_time.minute) * 60 + (end_sec - cur_time.second)
    return (f"{int(time_remaining / 3600):02d} : {int(time_remaining % 3600 / 60):02d} : {int(time_remaining % 3600 % 60):02d}")
    
def short_timer(end_hour, end_min, end_sec):
    cur_time = datetime.datetime.now()
    time_remaining = (end_hour - cur_time.hour) * 3600 + (end_min - cur_time.minute) * 60 + (end_sec - cur_time.second)
    return (f"{int(time_remaining % 3600 / 60):02d} : {int(time_remaining % 3600 % 60):02d}")

def timer_percentage(start_time, cur_time, end_time):
    start_time = datetime.datetime.now() - datetime.timedelta(hours = 2)
    end_time = datetime.datetime.now() + datetime.timedelta(hours = 4) 

def percent(total_hours, total_minutes, start_time):
    current_time = datetime.datetime.now()
    current_time_seconds = current_time.hour * 3600 + current_time.minute * 60 + current_time.second

    difference = current_time_seconds - start_time.total_seconds()
    duration = total_hours * 3600 + total_minutes * 60

    return int(((difference / duration)) * 100)

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def total_seconds(self):
        return (self.hour * 3600 + self.minute * 60 + self.second)
    

# print(long_timer(6, 30, 30))
# print(short_timer(12, 70, 30))
# print(percent(4, 30, Time(18, 0, 0)))







