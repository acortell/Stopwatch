import tkinter as tk
from datetime import datetime, timedelta


class Timer:
    def __init__(self, parent):
        self.active = False
        self.previous_time = timedelta(0)
        self.time_start = datetime.now()
        self.frame = tk.Frame(parent)
        self.frame.pack(side='bottom')
        self.entry = tk.Entry(self.frame)
        self.entry.pack(side='left')
        self.label = tk.Label(self.frame, text="0:00:00", font=('calibri', 20, 'bold'))
        self.label.pack(side='left')
        self.label.after(1000, self.refresh_label)
        self.delete_button = tk.Button(self.frame, text="Delete", font=('calibri', 20), fg="blue",
                                       command=self.frame.destroy)
        self.delete_button.pack(side='right')
        self.reset_button = tk.Button(self.frame, text="Reset", font=('calibri', 20), fg="blue", command=self.reset)
        self.reset_button.pack(side='right')
        self.stop_button = tk.Button(self.frame, text="Stop", font=('calibri', 20), fg="blue", command=self.stop)
        self.stop_button.pack(side='right')
        self.start_button = tk.Button(self.frame, text="Start", font=('calibri', 20), fg="blue", command=self.start)
        self.start_button.pack(side='right')

    def stop(self):
        self.previous_time = datetime.now() - self.time_start + self.previous_time
        self.active = False

    def reset(self):
        self.previous_time = timedelta(0)
        self.active = False

    def start(self):
        self.time_start = datetime.now()
        self.active = True

    def time(self):
        if self.active:
            elapsed = datetime.now() - self.time_start + self.previous_time
        else:
            elapsed = self.previous_time
        return str(elapsed).split('.')[0]

    def refresh_label(self):
        self.label.config(text=self.time())
        self.label.after(1000, self.refresh_label)
