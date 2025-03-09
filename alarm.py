from datetime import datetime
import time
from playsound import playsound

class AlarmClock:
    def __init__(self, alarm_time):
        self.alarm_time = alarm_time.strip()

    def check_if_alarm_time(self):
        return datetime.now().strftime("%H:%M") == self.alarm_time

def start_alarm(alarm_time):
    alarm = AlarmClock(alarm_time)
    
    while True:
        if alarm.check_if_alarm_time():
            playsound('alarm.mp3')
            break
        time.sleep(10)
