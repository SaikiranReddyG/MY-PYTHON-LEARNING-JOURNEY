import time
import threading
import tkinter as tk

class Alarm:
    def __init__(self, hours, minutes, label):
        self.hours = hours
        self.minutes = minutes
        self.label = label
        self.snooze_count = 0


    def __str__(self):
        return f'{self.label}:{self.hours : 02d} : {self.minutes : 02d}'

    def set_snooze(self):
        self.snooze_count += 1
        self.minutes += 10
        if self.minutes >= 60:
            self.hours += 1
            self.minutes -= 60

    def clear_snooze(self):
        self.snooze_count = 0

    def check_alarm(self):
        now = time.localtime()
        if now.tm_hour == self.hours and now.tm_min ==self.minutes:
            if self.snooze_count == 0:
                return True
            else:
                self.set_snooze()
                return False

        else:
            return False

class Alarmclock:
    def __init__(self):
        self.alarms = []

    def add_alarms(self, hours, minuts, label):
        alarm = Alarm(hours, minuts, label)
        self.alarms.append(alarm)

    def remove_alarm(self, alarm):
        self.alarms.remove(alarm)

    def snooze_alarm(self, alarm):
        alarm.set_snooze()

    def clear_snooze(self, alarm):
        alarm.clear_snooze()

    def start(self):
        while True:
            for alarm in self.alarms:
                if alarm.check_alarm():
                    print(f'Alarm {alarm.label} is going OFFF!!!!')

            time.sleep(60)

class AlarmGUI:
    def __init__(self, alarm_clock):
        self.alarm_clock = alarm_clock
        self.window = tk.Tk()
        self.window.title('Alarmclock')
        self.window.geometry('300*200')

        self.alarm_listbox = tk.Listbox(self.window)
        self.alarm_listbox.pack(side='left', fill='both', expand=True)

        self.add_button = tk.Button(self.window, text='Add Alarm', command=self.add_alarm)
        self.add_button.pack()

        self.remove_button = tk.Button(self.window, text='Remove Alarm', command=self.remove_alarm)
        self.remove_button.pack()

        self.snooze_button = tk.Button(self.window, text='snooze', command=self.snooze_alarm)
        self.snooze_button.pack()

        self.clear_snooze_button = tk.Button(self.window, text='clear snooze', command=self.clear_snooze)
        self.clear_snooze_button.pack()

        self.update_alarm_listbox()

    def add_alarm(self):
        alarm_window = tk.Toplevel(self.window)
        alarm_window.title('add Alarm')
        alarm_window.geometry("200*100")

        hours_label = tk.Label(alarm_window, text='hours:')
        hours_label.pack()
        hours_entry = tk.Entry(alarm_window)
        hours_entry.pack()

        minutes_label = tk.Label(alarm_window, text='minutes:')
        minutes_label.pack()
        minutes_entry = tk.Entry(alarm_window)
        minutes_entry.pack()

        label_label = tk.Label(alarm_window, text='label:')
        label_label.pack()
        label_entry = tk.Entry(alarm_window)
        label_entry.pack()

        save_button = tk.Button(alarm_window, text='save', command=lambda: self.save_alarm(hours_entry, minutes_entry, label_entry, alarm_window))
        save_button

