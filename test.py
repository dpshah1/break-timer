import datetime

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
    pass
    
    
    
    
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def total_seconds(self):
        return (self.hour * 3600 + self.minute * 60 + self.second)
    

print(long_timer(6, 30, 30))
print(short_timer(12, 70, 30))

