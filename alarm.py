from datetime import datetime
import time
import threading
from playsound import playsound

class AlarmClock:
    def __init__(self, alarm_time: str):
        """Initialize alarm clock with the given alarm time (HH:MM format)."""
        self.alarm_time = alarm_time.strip()

    def check_if_alarm_time(self) -> bool:
        """Check if the current time matches the alarm time."""
        return datetime.now().strftime("%H:%M") == self.alarm_time

def start_alarm(alarm_time):
    """Continuously checks the time and plays the alarm sound when the time matches."""
    alarm = AlarmClock(alarm_time)
    
    while True:
        if alarm.check_if_alarm_time():
            playsound('alarm.mp3')
            break
        time.sleep(10)  # Check every 10 seconds
